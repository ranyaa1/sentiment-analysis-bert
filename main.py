import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt

# Chargement du modèle BERT de sentiment (distilbert-base-uncased-finetuned-sst-2-english)
@st.cache_resource(show_spinner=False)
def load_model():
    return pipeline("sentiment-analysis")

classifier = load_model()

st.set_page_config(page_title="Analyse de Sentiment BERT", layout="centered")

st.title("📝 Analyse de Sentiment avec BERT")
st.markdown("""
Cette application permet d'analyser les sentiments des avis produits :
- Soit à partir d'un fichier CSV contenant une colonne `reviewText`
- Soit en saisissant un texte libre.
""")

mode = st.radio("Mode d'entrée :", ("Fichier CSV", "Texte libre"))

def analyze_text(text):
    if not text.strip():
        return None
    result = classifier(text)[0]
    label = result['label']
    score = result['score']
    return label, score

if mode == "Fichier CSV":
    uploaded_file = st.file_uploader("Choisissez un fichier CSV contenant une colonne `reviewText`", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if 'reviewText' not in df.columns:
            st.error("Le fichier CSV doit contenir une colonne nommée 'reviewText'.")
        else:
            st.success(f"Fichier chargé avec succès : {df.shape[0]} avis détectés.")
            
            with st.spinner("Analyse des sentiments en cours..."):
                results = df['reviewText'].apply(analyze_text)
                df['Sentiment'] = results.apply(lambda x: x[0] if x else None)
                df['Score'] = results.apply(lambda x: x[1] if x else None)

            st.dataframe(df[['reviewText', 'Sentiment', 'Score']].head(50))

            # Graphique des proportions de sentiments
            st.subheader("Répartition des sentiments")
            fig, ax = plt.subplots()
            sentiment_counts = df['Sentiment'].value_counts()
            sentiment_counts.plot(kind='bar', color=['green' if l=='POSITIVE' else 'red' for l in sentiment_counts.index], ax=ax)
            ax.set_ylabel("Nombre d'avis")
            ax.set_xlabel("Sentiment")
            ax.set_title("Distribution des sentiments")
            st.pyplot(fig)

elif mode == "Texte libre":
    user_text = st.text_area("Saisissez un avis à analyser", height=150)
    if st.button("Analyser"):
        if user_text.strip() == "":
            st.warning("Veuillez saisir un texte.")
        else:
            with st.spinner("Analyse en cours..."):
                label, score = analyze_text(user_text)
            st.markdown(f"**Sentiment :** {'😊 Positif' if label == 'POSITIVE' else '😞 Négatif'}")
            st.markdown(f"**Confiance :** {score:.2f}")
            st.write("---")
            st.markdown(f"> {user_text}")
