# Emotion Classifier 🎉

Um sistema de classificação de emoções que utiliza aprendizado de máquina para prever emoções a partir de textos. O projeto usa um modelo Naive Bayes para análise de sentimento e é implementado com Streamlit para a interface web.

## Índice 📚

1. [Introdução](#introdução)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Instalação](#instalação)
4. [Uso](#uso)
5. [Contribuição](#contribuição)
6. [Licença](#licença)

## Introdução 🎯

O Emotion Classifier é uma aplicação web desenvolvida para classificar emoções em textos. Ele utiliza um modelo treinado com Naive Bayes e um vectorizer de texto para prever emoções como "alegria" 😊 ou "medo" 😨. O projeto é implementado com Streamlit para uma interface amigável e interativa.

## Tecnologias Utilizadas 🛠️

- **Python**: Linguagem de programação 🐍
- **Streamlit**: Framework para criação de aplicações web 🖥️
- **Scikit-Learn**: Biblioteca para aprendizado de máquina 📚
- **Joblib**: Serialização de modelos 💾
- **CountVectorizer**: Técnica de pré-processamento de texto 📝
- **Lottie**: Animações para melhorar a experiência do usuário 🎨

## Instalação ⚙️

### Requisitos

Certifique-se de ter o Python 3.7 ou superior instalado em seu sistema. Você pode verificar a versão do Python com:

```bash
python --version
```

### Clone o Repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/thaleson/Emotion_Classifier.git
cd Emotion_Classifier
```

### Configuração do Ambiente

Crie um ambiente virtual e ative-o. Aqui está o procedimento para diferentes sistemas operacionais:

#### Windows 💻

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux 🌍

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Instale as Dependências

Instale as dependências do projeto com:

```bash
pip install -r requirements.txt
```

### Modelos e Vectorizer

Certifique-se de que os arquivos do modelo e do vectorizer estão no diretório correto:

- `models/naive_bayes_model.pkl` 📁
- `models/count_vectorizer.pkl` 📁

Caso esses arquivos não estejam disponíveis, você pode treinar o modelo e salvar os arquivos usando os scripts fornecidos na pasta `scripts`.

## Uso 🚀

Inicie a aplicação Streamlit com:

```bash
streamlit run app.py
```

### Navegação na Aplicação 🧭

- **Home**: Página inicial do sistema de previsão 🏠
- **Sobre**: Informações sobre o projeto e sua implementação ℹ️
- **Previsão**: Interface para inserir texto e obter a previsão de emoção 💬

## Contribuição 🤝

Contribuições são bem-vindas! Se você deseja contribuir com o projeto, por favor siga as etapas abaixo:

1. Faça um fork do repositório 🍴
2. Crie uma branch para sua feature (`git checkout -b minha-feature`) 🌿
3. Faça commit das suas alterações (`git commit -am 'Adiciona nova feature'`) 📝
4. Faça push para a branch (`git push origin minha-feature`) 🚀
5. Abra um Pull Request 🔄

## Licença 📜

Este projeto é licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

