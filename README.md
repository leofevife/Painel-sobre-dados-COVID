# Dashboard COVID-19 🦠

Uma aplicação web em camadas desenvolvida para visualização e análise profunda dos microdados referentes à pandemia de COVID-19.

A aplicação utiliza um **backend analítico em Python (Streamlit)** dedicado à mastigação e cruzamento de dados de um arquivo CSV pesado, enquanto expõe os painéis resultantes em um **frontend reativo e dinâmico em Vue.js 3 + Tailwind CSS**, usando de uma temática *Dark Mode* moderna e polida.

---

## 🏗️ Arquitetura do Projeto

*   `/backend`: API Visual geradora dos Painéis via Streamlit (Python, Pandas, Matplotlib, Numpy).
*   `/frontend`: Interface centralizadora e menu de ancoragem construído com Vite + Vue 3 e estilizado usando Tailwind CSS v4.
*   `MICRODADOS.csv`: Arquivo raiz com a massa de dados que alimenta os dashboards (precisa obrigatoriamente estar na pasta raiz do repositório).

---

## 🚀 Como Executar Localmente

Você precisará iniciar ambos os servidores (Front e Back) simultaneamente em terminais diferentes.

### 1. Iniciar o Backend (Streamlit)

O Backend é onde os dados são processados. Siga os passos:

1. Abra um terminal na pasta raiz do repositório.
2. Navegue até a pasta `backend`:
   ```bash
   cd backend
   ```
3. Ative o ambiente virtual (se estiver no Windows):
   ```bash
   venv\Scripts\activate.bat
   ```
4. Execute o servidor do Streamlit fixando a porta 8501 e desativando a proteção CORS para permitir o uso em Iframes do Vue:
   ```bash
   streamlit run app.py --server.port 8501 --server.enableCORS=false --server.enableXsrfProtection=false
   ```

*O terminal ficará travado executando o servidor. Mantenha-o aberto.*

### 2. Iniciar o Frontend (Vue.js)

O Frontend é a interface visual onde o usuário interage. 

1. Abra um **segundo/novo** terminal na pasta raiz do repositório.
2. Navegue até a pasta `frontend`:
   ```bash
   cd frontend
   ```
3. Instale as dependências caso ainda não tenha feito:
   ```bash
   npm install
   ```
4. Suba o servidor de desenvolvimento do Vite:
   ```bash
   npm run dev
   ```

### 3. Acessar a Aplicação

Com ambos os terminais rodando, abra o seu navegador e acesse:
👉 **[http://localhost:5173](http://localhost:5173)**

Você verá a página inicial de introdução e o menu suspenso para navegar por todas as 10 métricas analisadas.
