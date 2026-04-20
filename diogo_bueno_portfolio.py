import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Portfólio | BI & Data", layout="wide")

# 2. CSS para Centralização Global e Alinhamento de Texto
st.set_page_config(page_title="Seu Portfólio", layout="centered")

st.markdown("""
    <style>
    /* 1. RESET DE VARIÁVEIS E LARGURA CENTRAL */
    :root {
        --max-width: 800px; /* Altere para 700px se quiser MAIS espaço nas laterais */
    }

    /* Força o container principal a centralizar e respeitar a largura */
    [data-testid="stAppViewBlockContainer"] {
        max-width: var(--max-width) !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
        padding-top: 3rem !important;
    }

    /* 2. FUNDO E CORES GERAIS */
    .stApp {
        background-color: #0A0A0A;
    }

    h1, h2, h3 {
        color: #8B5CF6 !important;
        text-align: center;
        margin-bottom: 20px !important;
    }
    
    p, span, li {
        color: #F5F5F5 !important;
        font-size: 18px !important;
        line-height: 1.8;
    }

    /* 3. CENTRALIZAÇÃO E ESTILO DAS ABAS */
    /* Estilização Moderna das Abas (Navegação) */
    div[data-testid="stTabs"] [role="tablist"] {
        background-color: #1A1A1A !important; /* Fundo do menu ligeiramente mais claro que o site */
        padding: 8px !important;
        border-radius: 50px !important; /* Formato de pílula */
        border: 1px solid #333333 !important;
        margin-bottom: 30px !important;
        gap: 10px !important;
    }

    button[data-baseweb="tab"] {
        border-radius: 40px !important; /* Botões internos arredondados */
        padding: 10px 25px !important;   
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        border: none !important;
        background-color: transparent !important;
    }

    /* Aba Selecionada (Destaque) */
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #FFFFFF !important; /* Roxo vibrante */
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3) !important; /* Brilho suave */
    }

    button[data-baseweb="tab"][aria-selected="true"] p {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    /* Efeito de Hover nas Abas */
    button[data-baseweb="tab"]:hover {
        background-color: rgba(139, 92, 246, 0.1) !important;
        transform: translateY(-2px) !important; /* Leve subida */
    }

    /* Remove a linha original do Streamlit que fica embaixo */
    div[data-baseweb="tab-highlight"] {
        display: none !important;
    }

    button[data-baseweb="tab"] {
        color: #FFFFFF !important;
        font-size: 18px !important;
        background-color: transparent !important;
    }
    
    button[data-baseweb="tab"][aria-selected="true"] p {
        color: #8B5CF6 !important;
        font-weight: bold !important;
    }

    div[data-baseweb="tab-highlight"] {
        background-color: #8B5CF6 !important;
    }

    /* 4. BOTÕES: ESTADO NORMAL E HOVER (LETRA ROXA) */
    div.stButton > button, div.stLinkButton > a {
        background-color: #8B5CF6 !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        font-weight: bold !important;
        text-decoration: none !important;
        width: 100%;
        display: block;
        text-align: center;
    }

    /* O ajuste que você pediu: Fundo branco e Letra Roxa ao passar o mouse */
    div.stButton > button:hover, 
    div.stLinkButton > a:hover,
    div.stLinkButton > a:hover p {
        background-color: #FFFFFF !important;
        color: #8B5CF6 !important;
        -webkit-text-fill-color: #8B5CF6 !important;
        transform: scale(1.02) !important;
    }

    /* Divisor */
    hr {
        border-color: #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Navegação
#👤🧪📊📩
aba_bio, aba_ds, aba_pbi, aba_contato = st.tabs([
    "Quem sou eu", 
    "Projetos Data Science", 
    "Projetos Power BI", 
    "Contato"
])

# 4. Conteúdo
with aba_bio:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    st.title("Especialista em BI & Inteligência de Dados")
    
    st.markdown("""
    Profissional com mais de **7 anos de experiência** em Planejamento e Business Intelligence em grandes empresas. 
    Especializado em transformar dados complexos em decisões estratégicas, atuando em todo o ciclo de BI: 
    desde a **modelagem** até a entrega de **dashboards, analises e relatórios para tomada de decisão**.
    """)
    
    st.divider()
    
    st.subheader("O que eu entrego:")
    
    st.markdown("""
    * **🔍 Inteligência:** Análises que identificam oportunidades e previnem riscos para o negócio.
    * **📊 Visualização de Dados:** Dashboards End-to-End: modelagem, visualização e storytelling para suporte à diretoria.
    * **🤖 Automação de análises:** Otimização de rotinas de dados e automação de relatórios para ganho de escala.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# As demais abas seguem o mesmo padrão de container para manter o menu no lugar
with aba_ds:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    st.title("🧪 Projetos Data Science")
    st.markdown("Uma seleção de projetos de Data Science, criados em âmbito de estudos.")
    st.markdown("<br>", unsafe_allow_html=True)

    # --- CSS Customizado para os Cards e Botões Roxos ---
    st.markdown("""
        <style>
        /* Card de Projeto */
        .project-card {
            background-color: #1A1A1A;
            padding: 25px;
            border-radius: 15px;
            border: 1px solid #333333;
            margin-bottom: 25px;
        }

        /* Estilização do Botão (simulando o estilo do Streamlit com suas cores) */
        div.stButton > button, div.stLinkButton > a {
            background-color: #8B5CF6 !important;
            color: #FFFFFF !important;
            border: none !important;
            padding: 10px 20px !important;
            border-radius: 8px !important;
            transition: all 0.3s ease !important;
            font-weight: bold !important;
            text-decoration: none !important;
            display: inline-block !important;
        }

        /* Efeito de Hover (Passar o mouse) - Forçando a cor no texto interno */
            div.stButton > button:hover, 
            div.stLinkButton > a:hover,
            div.stLinkButton > a:hover p {
            background-color: #FFFFFF !important;
            color: #8B5CF6 !important; /* ROXO FORÇADO */
            -webkit-text-fill-color: #8B5CF6 !important; /* Força em navegadores Chrome/Safari */
            transform: scale(1.05) !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Exemplo de como aplicar em um dos projetos (repita a estrutura para os outros)
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("🛒 Análise de Performance: Vendas Walmart")
        st.image("https://eu-images.contentstack.com/v3/assets/blt58a1f8f560a1ab0e/blt2043a8ed80a75292/693b270fc6eb9d7f0dded72a/Walmart_exterior.webp?width=1280&auto=webp&quality=80&disable=upscale", 
            width=200,
            use_container_width=True)
        st.write("""       
        Análise exploratória utilizando dados históricos para identificar padrões sazonais. 
        O projeto responde a perguntas críticas como o impacto de feriados e inflação nas vendas.
        """)
        st.link_button("Acessar GitHub", "https://github.com/diogobueno-analytics/walmart-sales")
        st.markdown('</div>', unsafe_allow_html=True)

    # Repita para Rossmann, Churn e Olist...
    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("📈 Forecast de Vendas: Redes Rossmann com Machine Learning")
        st.image("https://sopotcentrum.com.pl/images/shopsPhotos/img_42_DSC_0111.jpg", 
            width=200,
            use_container_width=True)
        st.write("Desenvolvimento de um modelo de séries temporais para prever o faturamento de mais de 3.000 farmácias.")
        st.link_button("Acessar GitHub", "https://github.com/diogobueno-analytics/sales_forecast_rossmann")
        st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("📉 Previsão de Churn: IBM Telco com Machine Learning")
        st.image("https://www.frontline-consultancy.com/wp-content/uploads/2025/07/AdobeStock_1496894737_Editorial_Use_Only-scaled.jpeg", 
            width=200,
            use_container_width=True)
        st.write("Modelo focado em retenção de clientes através da identificação antecipada de perfis com risco de cancelamento.")
        st.link_button("Acessar GitHub", "https://github.com/diogobueno-analytics/churn-prediction-ibm-telco")
        st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        st.subheader("💰 Elasticidade de Preço: Olist E-commerce")
        st.image("https://mercadoeconsumo.com.br/wp-content/uploads/2021/04/olist-divulgalcao.jpg", 
            width=200,
            use_container_width=True)
        st.write("Estudo estatístico para medir a sensibilidade da demanda em relação às variações de preço no varejo digital.")
        st.link_button("Acessar GitHub", "https://github.com/diogobueno-analytics/preco-elasticidade-olist")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with aba_pbi:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.write("Neste momento estou focado em desenvolver estudos de Data Science, que é um tema que tenho estudado atualmente," \
    " como Power BI é algo que já atuo a mais de 5 anos, trarei alguns projetos posteriormente.")
    st.markdown("</div>", unsafe_allow_html=True)

with aba_contato:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    st.title("📩 Vamos conversar?")
    st.markdown("""
        Se você tem interesse em discutir projetos de dados, oportunidades de colaboração 
        ou quer trocar ideias e experiências, sinta-se à vontade para se conectar comigo!
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # Criando colunas para os botões de contato ficarem lado a lado
    col_ln, col_gh = st.columns(2)

    with col_ln:
        st.markdown("""
            <div style="text-align: center;">
                <p>Para conexões profissionais e networking:</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("🔗 Acessar meu LinkedIn", "https://www.linkedin.com/in/diogobuenodarosa/", use_container_width=True)

    with col_gh:
        st.markdown("""
            <div style="text-align: center;">
                <p>Para explorar meus códigos e repositórios:</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("💻 Acessar meu GitHub", "https://github.com/diogobueno-analytics", use_container_width=True)

    st.divider()

    # Rodapé simples
    st.markdown("""
        <div style="text-align: center; opacity: 0.6; font-size: 14px;">
            <p>Desenvolvido com Python e Streamlit</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)