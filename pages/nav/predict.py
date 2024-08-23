import streamlit as st
import joblib
from sklearn.feature_extraction.text import CountVectorizer
import time
import re  # Importado para validação de texto

# Carregar o modelo e o vectorizer
modelo = joblib.load('models/naive_bayes_model.pkl')
vectorizer = joblib.load('models/count_vectorizer.pkl')

def preprocessar_dados_novos(textos, vectorizer):
    """
    Preprocessa os textos usando o vectorizer.

    Parameters:
    textos (list): Lista de textos para preprocessar.
    vectorizer (CountVectorizer): O vectorizer para transformar os textos.

    Returns:
    scipy.sparse.csr.csr_matrix: Dados preprocessados prontos para o modelo.
    """
    return vectorizer.transform(textos)

def verificar_texto(texto):
    """
    Verifica se o texto contém apenas letras e espaços.

    Parameters:
    texto (str): O texto a ser verificado.

    Returns:
    bool: True se o texto for válido, False caso contrário.
    """
    return bool(re.match("^[A-Za-z\s]+$", texto))

def show():
    """
    Exibe a interface de previsão de emoções no Streamlit.
    """
    st.title("Previsão de Emoções")

    # Input de texto pelo usuário
    texto = st.text_area("Digite o texto para previsão:")

    if st.button("Prever"):
        if texto:
            # Verificar se o texto é válido
            if verificar_texto(texto):
                # Exibir mensagem de análise
                with st.spinner("Analisando texto..."):
                    # Simular algum tempo de processamento
                    time.sleep(1)  # Remove isso quando o tempo de processamento for real

                    # Preprocessar e prever
                    X_novos = preprocessar_dados_novos([texto], vectorizer)
                    previsao = modelo.predict(X_novos)[0]

                    # Mapeamento das emoções com emoticons
                    emocao_dict = {
                        0: ('alegria', '😊', 'success', 'green'),
                        1: ('medo', '😨', 'error', 'red')
                    }

                    emocao, emoticon, estilo, cor = emocao_dict[previsao]

                    # Exibir resultado com formatação
                    st.markdown(
                        f"""
                        <p style="color: {cor}; font-size: 20px;">
                            Emoção do seu texto prevista é: <strong>{emocao}</strong> {emoticon}
                        </p>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.error("Por favor, insira apenas texto (letras e espaços). Números e caracteres especiais não são permitidos.")
        else:
            st.warning("Por favor, insira um texto para previsão.")

if __name__ == "__main__":
    show()
