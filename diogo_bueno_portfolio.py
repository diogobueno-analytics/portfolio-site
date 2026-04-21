import streamlit as st
import base64
import os
from PIL import Image

# 1. Configuração da página
st.set_page_config(page_title="Portfólio | BI & Data", layout="wide")

# ─── Curriculo Download Helper ───
curriculo_pdf = "Diogo Bueno - Currículo.pdf"

def gerar_link_pdf(caminho, texto_link):
    if os.path.exists(caminho):
        with open(caminho, "rb") as f:
            pdf_bytes = f.read()
        b64 = base64.b64encode(pdf_bytes).decode()
        # IMPORTANTE: A classe aqui deve ser btn-primary
        return f'<a href="data:application/pdf;base64,{b64}" download="Diogo_Bueno_Curriculo.pdf" class="btn-primary">📄 {texto_link}</a>'
    else:
        return ""

link_curriculo = gerar_link_pdf(curriculo_pdf, "Baixar meu currículo")

# 2. CSS para Centralização Global e Alinhamento de Texto
st.set_page_config(page_title="Diogo Bueno - Portfólio", layout="centered")

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
        
/* Container do Título Principal */
.hero-container {
    text-align: center;
    padding: 20px 0;
    margin-bottom: 2rem;
}
/* Nome Principal - GIGANTE */
.hero-name {
    text-align: left !important;
    margin: 0 !important;
    padding: 0 !important;
    line-height: 0.9 !important;
}
.hero-name .highlight {
    /* Tamanho baseado na largura da tela para garantir que fique grande */
    text-align: left !important;
    margin-bottom: 0px !important; 
    padding-bottom: 0px !important;
    font-size: 3vw !important; 
    font-weight: 900 !important;
    letter-spacing: -3px !important;
    
    /* Efeito de Degradê */
    background: linear-gradient(135deg, #CFFAFE 0%, #A78BFA 45%, #7C3AED 100%) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    display: inline-block !important;
}
/* Subtítulo - MENOR e SEM degradê */
.hero-subtitle {
    font-size: 1.3rem !important; /* Tamanho fixo menor */
    margin-top: -10px !important;
    color: #CCCCCC !important;    /* Cor sólida (cinza claro) */
    font-weight: 400 !important;
    margin-top: 10px !important;
    display: block !important;
    background: none !important;  /* Garante que não tenha degradê */
    -webkit-text-fill-color: initial !important; /* Reseta a transparência */
}   

/* Botões - Quem sou eu */
:root {
--accent: #8B5CF6;
--radius-sm: 8px;
--glass: rgba(255, 255, 255, 0.05);
--glass-border: rgba(255, 255, 255, 0.1);
}
.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.75rem 1.6rem;
    /* Usei o seu roxo no gradiente */
    background: linear-gradient(135deg, #8B5CF6 0%, #4299e1 100%);
    color: white !important; /* Cor do texto */
    border-radius: var(--radius-sm);
    font-size: 0.875rem;
    font-weight: 700;
    text-decoration: none !important;
    transition: all 0.25s;
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.35);
    letter-spacing: 0.2px;
    border: none;
}
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 30px rgba(139, 92, 246, 0.55);
    color: white !important;
    text-decoration: none;
}
.hero-cta {
    display: flex;
    gap: 0.75rem;
    margin-top: 25px;
}      
/* Container que organiza os grupos de skills em colunas */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}
Estilo de cada "card" de grupo */
    .skill-group {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }

    .skill-group:hover {
        transform: translateY(-5px);
        border-color: #8B5CF6;
        background: rgba(139, 92, 246, 0.05);
    }

    .skill-group-header {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        margin-bottom: 1.2rem;
    }

    .skill-group-title {
        font-weight: 700;
        color: #ffffff;
        font-size: 1.1rem;
    }

    /* Organização das tags dentro do card */
    .skill-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 0.6rem;
    }

    .skill-tag {
        padding: 0.4rem 0.8rem;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 500;
    }

    /* Cores das Tags */
    .tag-blue { background: rgba(59, 130, 246, 0.15); color: #60a5fa !important; border: 1px solid rgba(59, 130, 246, 0.2); }
    .tag-green { background: rgba(16, 185, 129, 0.15); color: #34d399 !important; border: 1px solid rgba(16, 185, 129, 0.2); }
    .tag-purple { background: rgba(139, 92, 246, 0.15); color: #a78bfa !important; border: 1px solid rgba(139, 92, 246, 0.2); }
    .tag-orange { background: rgba(245, 158, 11, 0.15); color: #fbbf24 !important; border: 1px solid rgba(245, 158, 11, 0.2); } 
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
    
    st.markdown("""
    <div style="text-align: left; width: 100%;">
        <h1 class="hero-name" style="margin-bottom: 0px !important; line-height: 0.8;">
            <span class="highlight">Diogo Bueno da Rosa</span>
        </h1>
        <div class="hero-subtitle" style="margin-top: 5px !important;">
            // Analista de Business Intelligence | Especialista em Dados
        </div>
        <div class="hero-subtitle" style="margin-top: 0px !important;">
            Estratégia · Performance · Governança
        </div>
    </div>
    <br>
    """, unsafe_allow_html=True)

    st.markdown("""
    Profissional com mais de **7 anos de experiência** em Planejamento e Business Intelligence em grandes empresas. 
    Especializado em transformar dados complexos em decisões estratégicas, atuando em todo o ciclo de BI: 
    desde a **modelagem** até a entrega de **dashboards, analises e relatórios para tomada de decisão**.
    """)

    # Definimos o HTML em uma variável limpa
    #html_content = f"""<div class="hero-cta">{link_curriculo}<a href="https://github.com/diogobueno-analytics" target="_blank" class="btn-primary"><svg width="16" height="16" viewBox="0 0 24 24" fill="white" style="margin-right:8px;"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>Projetos GitHub</a><a href="https://www.linkedin.com/in/diogobuenodarosa/" target="_blank" class="btn-primary"><svg width="16" height="16" viewBox="0 0 24 24" fill="white" style="margin-right:8px;"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>LinkedIn</a></div>""".replace('\n', '').strip()
    #st.markdown(html_content, unsafe_allow_html=True)

    html_final = f"""
    <div class="hero-cta" style="display: flex; gap: 10px; flex-wrap: wrap;">
        {link_curriculo}
        <a href="https://github.com/diogobueno-analytics" target="_blank" class="btn-primary" style="text-decoration: none;">
            Projetos GitHub
        </a>
        <a href="https://www.linkedin.com/in/diogobuenodarosa/" target="_blank" class="btn-primary" style="text-decoration: none;">
            LinkedIn
        </a>
    </div>
    """.replace('\n', '').strip()
    st.markdown(html_final, unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("O que eu entrego:")
    
    st.markdown("""
    * **🔍 Inteligência:** Análises que identificam oportunidades e previnem riscos para o negócio.
    * **📊 Visualização de Dados:** Dashboards End-to-End: modelagem, visualização e storytelling para suporte à diretoria.
    * **⚙️ Automação de análises:** Otimização de rotinas de dados e automação de relatórios para ganho de escala.
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ─── Skills ───
    st.subheader("Skills/Habilidades")

    st.markdown("""
    <div class="skills-grid">
    <div class="skill-group">
    <div class="skill-group-header">
    <span class="skill-group-icon">📊</span>
    <span class="skill-group-title">Business Intelligence</span>
    </div>
    <div class="skill-tags">
    <span class="skill-tag tag-blue">ETL</span>
    <span class="skill-tag tag-blue">Modelagem de Dados</span>
    <span class="skill-tag tag-blue">Storytelling</span>
    <span class="skill-tag tag-blue">Análise de Dados</span>
    <span class="skill-tag tag-blue">Dashboards</span>
    <span class="skill-tag tag-blue">KPIs</span>
    <span class="skill-tag tag-blue">Estatística Descritiva & +</span>
    <span class="skill-tag tag-blue">Planejamento Estratégico</span>
    </div>
    </div>
    <div class="skill-group">
    <div class="skill-group-header">
    <span class="skill-group-icon">🛠️</span>
    <span class="skill-group-title">Ferramentas</span>
    </div>
    <div class="skill-tags">
    <span class="skill-tag tag-purple">Power BI</span>
    <span class="skill-tag tag-purple">VS Code</span>                
    <span class="skill-tag tag-purple">Excel</span>
    <span class="skill-tag tag-purple">KNIME</span> 
    <span class="skill-tag tag-purple">PowerPoint</span>
    <span class="skill-tag tag-purple">Jira/Clickup/Trello</span>
    </div>              
    </div>
    <div class="skill-group">
    <div class="skill-group-header">
    <span class="skill-group-icon">💻</span>
    <span class="skill-group-title">Linguagens</span>
    </div>
    <div class="skill-tags">
    <span class="skill-tag tag-green">SQL</span>
    <span class="skill-tag tag-green">DAX</span>
    <span class="skill-tag tag-green">Python</span>
    </div>    
    </div>
    <div class="skill-group">
    <div class="skill-group-header">
    <span class="skill-group-icon">🌐</span>
    <span class="skill-group-title">Idiomas</span>
    </div>
    <div class="skill-tags">
    <span class="skill-tag tag-orange">Inglês</span>
    <span class="skill-tag tag-orange">Italiano</span>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

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

    st.markdown("""
    <style>
    /*Ajuste da barra superior "Deploy" 
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }                
                
    /* ── Contact ── */
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 0.85rem;
    }
    .contact-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(51, 65, 85, 1);
        border-radius: 15px;
        padding: 1.5rem 1.25rem;
        text-align: center;
        transition: all 0.25s;
        backdrop-filter: var(--blur);
    }
    .contact-card:hover {
        border-color: v#8B5CF6;
        background: rgba(139, 92, 246, 0.1);
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.3), 0 0 20px var(--accent-glow);
    }
    .contact-icon { font-size: 1.5rem; margin-bottom: 0.4rem; }
    .contact-label {
        font-family: var(--mono);
        font-size: 0.68rem;
        color: #FFFFFF;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
    }
    .contact-value {
        color: #FFFFFF;
        font-size: 0.875rem;
        font-weight: 500;
        margin-top: 0.2rem;
    }
    .contact-value a { color: #FFFFFF; text-decoration: none; }
    .contact-value a:hover { color: #8B5CF6; }
    </style>    
        """, unsafe_allow_html=True) 

    st.markdown("<br>", unsafe_allow_html=True)

    # Criando colunas para os botões de contato ficarem lado a lado
    #col_ln, col_gh = st.columns(2)

    st.markdown("""
    <div class="contact-grid">
    <div class="contact-card">
        <div class="contact-icon">📧</div>
        <div class="contact-label">Email</div>
        <div class="contact-value">
            <a href="mailto:adm.diogobueno@gmail.com">adm.diogobueno@gmail.com</a>
        </div>
    </div>
    <div class="contact-card">
        <div class="contact-icon">💼</div>
        <div class="contact-label">LinkedIn</div>
        <div class="contact-value">
            <a href="https://www.linkedin.com/in/diogobuenodarosa/" target="_blank">Diogo Bueno</a>
        </div>
    </div>
    <div class="contact-card">
        <div class="contact-icon">🐙</div>
        <div class="contact-label">GitHub</div>
        <div class="contact-value">
            <a href="https://github.com/diogobueno-analytics" target="_blank">diogobueno-analytics</a>
        </div>
    </div>
    <div class="contact-card">
        <div class="contact-icon">📍</div>
        <div class="contact-label">Localização</div>
        <div class="contact-value">Curitiba, Paraná</div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()

    # Rodapé simples
    st.markdown("""
    <div style="text-align: center; opacity: 0.6; font-size: 14px;">
        <p>Desenvolvido com Python e Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)