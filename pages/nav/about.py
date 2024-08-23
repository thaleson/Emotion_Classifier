import streamlit as st

def show():
    # Configurar o título da página
    st.title("Sobre o Projeto")

    # Descrição do Projeto
    st.subheader("Descrição do Projeto")
    st.markdown(
        """
        Este projeto é um classificador de emoções desenvolvido para identificar sentimentos em textos. Utilizamos técnicas de processamento de linguagem natural (NLP) e aprendizado de máquina para classificar frases em duas categorias principais: 'alegria' e 'medo'.

        O objetivo principal é fornecer uma ferramenta que possa analisar o sentimento expresso em textos e fornecer insights sobre a emoção predominante. Abaixo, detalhamos o processo de desenvolvimento do projeto, os modelos testados, e a conclusão final sobre a eficácia dos modelos.
        """
    )

    # Processo de Desenvolvimento
    st.subheader("Processo de Desenvolvimento")
    st.markdown(
        """
        O projeto seguiu as seguintes etapas:

        1. **Coleta e Pré-processamento de Dados**:
           - Utilizamos dois arquivos TXT, `base_treinamento.txt` e `base_teste.txt`, contendo frases e emoções associadas.
           - O pré-processamento incluiu a limpeza dos dados, remoção de stopwords e vetorização dos textos utilizando o `CountVectorizer`.

        2. **Treinamento e Avaliação dos Modelos**:
           - Testamos diferentes modelos de aprendizado de máquina para determinar o melhor desempenho na classificação das emoções:
             - **Naive Bayes**: Acurácia de 0.67
             - **Random Forest**: Acurácia de 0.60
             - **SVM (Support Vector Machine)**: Acurácia de 0.65

        3. **Escolha do Modelo Final**:
           - O modelo de **Naive Bayes** foi selecionado como o melhor modelo com base na acurácia mais alta (0.67) e no balanceamento entre precisão e recall.

        4. **Implementação e Deploy**:
           - A interface do usuário foi desenvolvida com Streamlit, incluindo páginas para navegação, informações sobre o projeto e uma ferramenta de previsão de emoções.
        """
    )

    # Códigos em Python
    st.subheader("Códigos em Python")
    st.markdown(
        """
        **Pré-processamento e Treinamento dos Modelos:**

        ```python
        import pandas as pd
        import numpy as np
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.naive_bayes import MultinomialNB
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.svm import SVC
        from sklearn.metrics import accuracy_score, classification_report

        # Função para carregar os dados e pré-processar
        def preprocessar_dados(df):
            vectorizer = CountVectorizer(stop_words='portuguese')
            X = vectorizer.fit_transform(df['texto'])
            le = LabelEncoder()
            y = le.fit_transform(df['emocao'])
            return X, y, vectorizer, le

        # Carregar dados
        base_treinamento = pd.read_csv('base_treinamento.txt', delimiter=',')
        base_teste = pd.read_csv('base_teste.txt', delimiter=',')

        X_treinamento, y_treinamento, vectorizer, le = preprocessar_dados(base_treinamento)
        X_teste, y_teste, _, _ = preprocessar_dados(base_teste)

        # Testar modelos
        models = {
            'Naive Bayes': MultinomialNB(),
            'Random Forest': RandomForestClassifier(),
            'SVM': SVC()
        }

        for name, model in models.items():
            model.fit(X_treinamento, y_treinamento)
            y_pred = model.predict(X_teste)
            accuracy = accuracy_score(y_teste, y_pred)
            print(f"Treinando o modelo: {name}")
            print(f"Acurácia do {name}: {accuracy:.2f}")
            print(classification_report(y_teste, y_pred, target_names=le.classes_))

        # Salvar o melhor modelo
        best_model = MultinomialNB()  # Exemplo, substitua pelo melhor modelo
        import joblib
        joblib.dump(best_model, 'melhor_modelo.pkl')
        ```
        """
    )
    # Conclusão
    st.subheader("Conclusão")
    st.markdown(
        """
        O projeto resultou em uma ferramenta funcional para classificar emoções em textos. O modelo de Naive Bayes apresentou a melhor acurácia entre os modelos testados e foi selecionado para uso final. 

        A utilização do modelo de Naive Bayes se mostrou eficiente devido à sua capacidade de lidar bem com a representação textual dos dados e à simplicidade do seu funcionamento. No entanto, é importante considerar que a acurácia pode variar com diferentes conjuntos de dados e é sempre recomendável realizar ajustes e validações adicionais para melhorar o desempenho do modelo.

        O sistema de previsão foi implementado utilizando Streamlit, proporcionando uma interface amigável para a interação com a ferramenta. Através das páginas do Streamlit, os usuários podem obter previsões sobre as emoções expressas em seus textos e obter insights valiosos para análises sentimentais.
        """
    )

if __name__ == "__main__":
    show()
