# 📝 Analyse de Sentiment avec BERT
<img src="https://github.com/user-attachments/assets/9f334a21-a0a1-4d92-8422-6b82c37ddd76" width="500" alt="Image 1">

<img src="https://github.com/user-attachments/assets/f3b60245-c796-462b-9157-e9ae2427975f" width="500" alt="Image 2">

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
