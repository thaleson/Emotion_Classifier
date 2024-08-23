import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(
    page_title="Classificador de Emoções",
    page_icon="😊",  # Você pode substituir o ícone conforme sua preferência
    layout="wide"
)

# Aplicar estilos personalizados
st.markdown(
    f"""
    <style>
    {open("static/style.css").read()}
    </style>
    """,
    unsafe_allow_html=True
)

# Navegação entre páginas
with st.sidebar:
    selected = option_menu(
        "Navegação",
        ["Home", "Sobre", "Previsão"],
        icons=["house", "info-circle", "cloud"],
        menu_icon="cast",
        default_index=0,
    )

    st.markdown("""
        <p style="text-align: center;">Meus Contatos</p>
        """, unsafe_allow_html=True)

    # Badges
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between;">
            <div>
                <a href="https://github.com/thaleson" target="_blank">
                    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="https://www.linkedin.com/in/thaleson-silva-9298a0296/" target="_blank">
                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" width="100" />
                </a>
            </div>
            <div>
                <a href="mailto:thaleson177@gmail.com" target="_blank">
                    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" width="80" />
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Exibir o conteúdo das páginas
if selected == "Home":
    from pages.nav import home
    home.show()
elif selected == "Sobre":
    from pages.nav import about
    about.show()
elif selected == "Previsão":
    from pages.nav import predict
    predict.show()
