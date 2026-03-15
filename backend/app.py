import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: transparent !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    cols_to_use = [
        'DataNotificacao', 'Classificacao', 'Evolucao', 'Municipio', 
        'FaixaEtaria', 'Sexo', 'Febre', 'DificuldadeRespiratoria', 
        'Tosse', 'Coriza', 'DorGarganta', 'Diarreia', 'Cefaleia',
        'ComorbidadePulmao', 'ComorbidadeCardio', 'ComorbidadeRenal',
        'ComorbidadeDiabetes', 'ComorbidadeTabagismo', 'ComorbidadeObesidade'
    ]
    
    dtypes = {
        'Classificacao': 'category',
        'Evolucao': 'category',
        'FaixaEtaria': 'category',
        'Sexo': 'category',
        'Febre': 'category',
        'DificuldadeRespiratoria': 'category',
        'Tosse': 'category',
        'Coriza': 'category',
        'DorGarganta': 'category',
        'Diarreia': 'category',
        'Cefaleia': 'category',
        'ComorbidadePulmao': 'category',
        'ComorbidadeCardio': 'category',
        'ComorbidadeRenal': 'category',
        'ComorbidadeDiabetes': 'category',
        'ComorbidadeTabagismo': 'category',
        'ComorbidadeObesidade': 'category',
        'Municipio': 'category'
    }
    
    df = pd.read_csv('../MICRODADOS.csv', sep=';', dtype=dtypes, usecols=lambda x: x in cols_to_use or x not in cols_to_use, low_memory=False, encoding='latin1')
    for col in dtypes.keys():
        if col in df.columns:
            df[col] = df[col].astype('category')
            
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    st.stop()

query_params = st.query_params
view = query_params.get("view", "1")

plt.style.use("dark_background")
fig_bg_color = "#1E1E2E"
text_color = "#CDD6F4"
accent_color = "#CBA6F7"

def conf_ax(ax):
    ax.set_facecolor(fig_bg_color)
    ax.tick_params(colors=text_color)
    for spine in ax.spines.values():
        spine.set_color('#313244')
    ax.xaxis.label.set_color(text_color)
    ax.yaxis.label.set_color(text_color)
    ax.title.set_color(text_color)

def create_fig(figsize=(7, 4)):
    fig, ax = plt.subplots(figsize=figsize)
    fig.patch.set_facecolor(fig_bg_color)
    conf_ax(ax)
    return fig, ax

if view == "1":
    st.subheader("Visão Geral do Dataset")
    col1, col2 = st.columns(2)
    col1.metric("Total de Registros", f"{df.shape[0]:,}")
    col2.metric("Total de Colunas", f"{df.shape[1]}")
    
    st.write("Tipos de Dados:")
    st.dataframe(df.dtypes.astype(str).reset_index().rename(columns={'index': 'Coluna', 0: 'Tipo'}))
    
    null_counts = df.isnull().sum()
    null_counts = null_counts[null_counts > 0]
    if not null_counts.empty:
        null_df = pd.DataFrame({
            'Quantidade Nulos': null_counts,
            'Percentual (%)': (null_counts / df.shape[0]) * 100
        }).sort_values('Quantidade Nulos', ascending=False)
        st.write("Valores Nulos por Coluna:")
        st.dataframe(null_df)
    else:
        st.success("Não há valores nulos no dataset.")

elif view == "2":
    st.subheader("Distribuição por Classificação")
    if 'Classificacao' in df.columns:
        counts = df['Classificacao'].value_counts()
        percs = df['Classificacao'].value_counts(normalize=True) * 100
        
        stat_df = pd.DataFrame({'Quantidade': counts, 'Percentual (%)': percs})
        st.dataframe(stat_df)
        
        fig, ax = create_fig()
        counts.sort_values().plot(kind='barh', ax=ax, color=accent_color)
        ax.set_title("Frequência Absoluta por Classificação")
        ax.set_xlabel("Quantidade")
        st.pyplot(fig)

elif view == "3":
    st.subheader("Top 10 Municípios com Mais Notificações")
    if 'Municipio' in df.columns:
        top10 = df['Municipio'].value_counts().head(10)
        
        fig, ax = create_fig()
        top10.sort_values().plot(kind='barh', ax=ax, color='#F38BA8')
        ax.set_title("Top 10 Municípios")
        ax.set_xlabel("Notificações")
        st.pyplot(fig)
        
        lider = top10.index[0]
        qtd = top10.iloc[0]
        st.markdown(f"O município que lidera em notificações é **{lider}**, com **{qtd:,}** registros.")

elif view == "4":
    st.subheader("Distribuição por Sexo")
    if 'Sexo' in df.columns:
        counts = df['Sexo'].value_counts()
        
        fig, ax = plt.subplots(figsize=(6, 6))
        fig.patch.set_facecolor(fig_bg_color)
        ax.set_facecolor(fig_bg_color)
        wedges, texts, autotexts = ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90,
               colors=['#89B4FA', '#F5C2E7', '#A6E3A1', '#F9E2AF'])
        for text in texts + autotexts:
            text.set_color(text_color)
        ax.set_title("Distribuição por Sexo", color=text_color)
        st.pyplot(fig)
        
        maior_sexo = counts.idxmax()
        st.markdown(f"O sexo que concentra mais notificações é o **{maior_sexo}**.")

elif view == "5":
    st.subheader("Casos por Faixa Etária")
    if 'FaixaEtaria' in df.columns:
        counts = df['FaixaEtaria'].value_counts()
        sorted_index = sorted(counts.index.astype(str))
        counts = counts.reindex(sorted_index)
        
        fig, ax = create_fig((8, 4))
        counts.plot(kind='bar', ax=ax, color='#89DCEB')
        ax.set_title("Notificações por Faixa Etária")
        ax.set_ylabel("Quantidade")
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)
        
        maior_faixa = counts.idxmax()
        st.markdown(f"A faixa etária que concentra o maior volume é **{maior_faixa}**.")

elif view == "6":
    st.subheader("Taxa de Letalidade")
    if 'Classificacao' in df.columns and 'Evolucao' in df.columns:
        confirmados = df[df['Classificacao'] == 'Confirmados']
        total_confirmados = len(confirmados)
        st.write(f"Total de Confirmados: {total_confirmados:,}")
        
        if total_confirmados > 0:
            evolucoes = confirmados['Evolucao'].value_counts()
            obitos_covid = evolucoes.get('Óbito pelo COVID-19', 0)
            obitos_outras = evolucoes.get('Óbito por outras causas', 0)
            cura = evolucoes.get('Cura', 0)
            ignorado = evolucoes.get('Ignorado', 0)
            
            st.metric("Óbito pelo COVID-19", f"{obitos_covid:,}")
            st.metric("Óbito por outras causas", f"{obitos_outras:,}")
            st.metric("Cura", f"{cura:,}")
            st.metric("Ignorado", f"{ignorado:,}")
            
            taxa_letalidade = (obitos_covid / total_confirmados) * 100
            st.markdown(f"### Taxa de Letalidade: **{taxa_letalidade:.2f}%**")

elif view == "7":
    st.subheader("Sintomas mais Frequentes")
    sintomas = ['Febre', 'DificuldadeRespiratoria', 'Tosse', 'Coriza', 'DorGarganta', 'Diarreia', 'Cefaleia']
    contagens = {}
    for s in sintomas:
        if s in df.columns:
            contagens[s] = (df[s] == 'Sim').sum()
            
    if contagens:
        s_df = pd.Series(contagens).sort_values()
        
        fig, ax = create_fig()
        s_df.plot(kind='barh', ax=ax, color='#F9E2AF')
        ax.set_title("Sintomas (Apenas 'Sim')")
        ax.set_xlabel("Frequência")
        st.pyplot(fig)

elif view == "8":
    st.subheader("Comorbidades nos Óbitos por COVID")
    if 'Evolucao' in df.columns:
        obitos = df[df['Evolucao'] == 'Óbito pelo COVID-19']
        comorbidades = ['ComorbidadePulmao', 'ComorbidadeCardio', 'ComorbidadeRenal', 
                        'ComorbidadeDiabetes', 'ComorbidadeTabagismo', 'ComorbidadeObesidade']
        contagens = {}
        for c in comorbidades:
            if c in obitos.columns:
                contagens[c] = (obitos[c] == 'Sim').sum()
                
        if contagens:
            c_df = pd.Series(contagens).sort_values()
            
            fig, ax = create_fig()
            c_df.plot(kind='barh', ax=ax, color='#FAB387')
            ax.set_title("Frequência de Comorbidades nos Óbitos")
            ax.set_xlabel("Quantidade")
            st.pyplot(fig)
            
            max_c = c_df.idxmax()
            st.markdown(f"A comorbidade mais presente nos óbitos é **{max_c}**.")

elif view == "9":
    st.subheader("Evolução Temporal das Notificações")
    if 'DataNotificacao' in df.columns:
        df_temp = df.copy()
        df_temp['DataNotificacao'] = pd.to_datetime(df_temp['DataNotificacao'], errors='coerce')
        df_temp = df_temp.dropna(subset=['DataNotificacao'])
        df_temp['AnoMes'] = df_temp['DataNotificacao'].dt.to_period('M')
        
        agrupado = df_temp.groupby('AnoMes').size()
        agrupado.index = agrupado.index.astype(str)
        
        fig, ax = create_fig((8, 4))
        agrupado.plot(kind='line', ax=ax, color='#A6E3A1', marker='o')
        ax.set_title("Notificações por Mês/Ano")
        ax.set_ylabel("Quantidade")
        plt.xticks(rotation=45, ha='right')
        st.pyplot(fig)
        
        picos = agrupado.nlargest(3)
        picos_str = ", ".join([f"{idx} ({val:,})" for idx, val in picos.items()])
        st.markdown(f"Os períodos de pico (ondas da pandemia) foram: **{picos_str}**.")

elif view == "10":
    st.subheader("Tabela Cruzada e Letalidade por Município")
    if 'Municipio' in df.columns and 'Evolucao' in df.columns and 'Classificacao' in df.columns:
        confirmados = df[df['Classificacao'] == 'Confirmados']
        top5_muni = confirmados['Municipio'].value_counts().head(5).index
        df_top5 = confirmados[confirmados['Municipio'].isin(top5_muni)]
        
        df_top5['Municipio'] = df_top5['Municipio'].cat.remove_unused_categories()
        
        tabela = pd.crosstab(df_top5['Municipio'], df_top5['Evolucao'])
        st.write("Tabela Cruzada (Top 5 Municípios com mais confirmados x Evolução):")
        st.dataframe(tabela)
        
        taxas = {}
        for muni in top5_muni:
            if muni in tabela.index:
                total = tabela.loc[muni].sum()
                obitos = tabela.loc[muni].get('Óbito pelo COVID-19', 0)
                if total > 0:
                    taxas[muni] = (obitos / total) * 100
                else:
                    taxas[muni] = 0
                    
        taxas_df = pd.Series(taxas).sort_values(ascending=False)
        st.write("Taxa de Letalidade por Município (%):")
        st.dataframe(taxas_df)
        
        maior_taxa = taxas_df.idxmax()
        st.markdown(f"O município com a maior taxa de letalidade entre os 5 é **{maior_taxa}**.")
