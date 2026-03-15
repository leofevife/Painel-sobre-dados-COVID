# 🚀 Guia Prático para Deploy do Dashboard COVID

Você está prestes a hospedar o projeto de forma dividida para garantir performance: o painel React/Vue ficará no Vercel, enquanto o processamento do Python (e do CSV imenso) ficará no Render.

---

## Passo 1: Publicando o Backend na Nuvem Render

A Render (https://render.com) é excelente para aplicações Python pesadas porque oferece 512MB RAM grátis e lida bem com dependências longas do Pandas.

1. Acesse o **[Render](https://render.com/)** e faça login com a conta do GitHub onde nós subimos o código.
2. Clique em **New** > **Web Service**.
3. Selecione o repositório **Painel-sobre-dados-COVID**.
4. Configure assim a página que vai abrir:
   - **Name**: `covid-backend-analysis` (ou o que desejar)
   - **Env**: `Python`
   - **Root Directory**: `backend` *(MUITO IMPORTANTE! O render precisa focar só nessa pasta)*
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.enableCORS=false --server.enableXsrfProtection=false`
5. Clique em **Create Web Service**. 
6. Quando o console de log terminar de rodar, guarde e copie a URL que eles te deram lá no topo esquerdo (exemplo: `https://covid-backend.onrender.com`).

---

## Passo 2: Publicando o Frontend no Vercel

Agora, a cereja do bolo que é as animações suaves em Vue irão girar gratuitamente na Vercel (https://vercel.com):

1. Crie uma conta ou entre no **[Vercel](https://vercel.com)** também usando seu Github.
2. Clique em **Add New...** > **Project** e importe o `Painel-sobre-dados-COVID`.
3. Na seção "Build and Output Settings", preste atenção nisso:
   - **Framework Preset**: `Vite`
   - **Root Directory**: Mude clicando em edit, e selecione `frontend`.
4. Expanda a janela inferior **Environment Variables** e crie uma variável apontando para a Render:
   - **Name**: `VITE_API_URL`
   - **Value**: Aquele link gigantão que você pegou do RENDER logo acima! (Exemplo `https://covid-backend.onrender.com`)
5. Clique em **Deploy**.

> ✨ Fim! Aguarde 1 minuto, o Vercel te dará um link super bonito onde sua web app inteira vai estar disponível pro mundo todo e já linkada pra sempre no seu python.
