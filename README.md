# 📝 Analyse de Sentiment avec BERT

Cette application utilise un modèle **BERT pré-entraîné** (DistilBERT) pour détecter automatiquement le **sentiment positif ou négatif** dans des avis textuels. Elle est développée avec **Streamlit** pour une interface simple et interactive.

---

## 🚀 Fonctionnalités

- Analyse de sentiment en **temps réel** via un **modèle BERT** (`distilbert-base-uncased-finetuned-sst-2-english`)
- Deux modes d'entrée :
  - 📂 **Fichier CSV** contenant une colonne `reviewText`
  - ✍️ **Texte libre** saisi manuellement
- 📊 Affichage graphique de la distribution des sentiments
- Affichage du **score de confiance** de la prédiction

---

## 🧠 Modèle utilisé

- **Nom :** `distilbert-base-uncased-finetuned-sst-2-english`
- **Source :** [HuggingFace Transformers](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)
- **Type :** Sentiment Analysis (fine-tuned BERT)

---

## ⚙️ Installation

1. **Cloner le dépôt :**

```bash
git clone https://github.com/votre-utilisateur/bert-sentiment-analyzer.git
cd bert-sentiment-analyzer
