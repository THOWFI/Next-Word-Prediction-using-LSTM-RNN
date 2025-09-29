# 📝 Next Word Prediction — LSTM & GRU

A compact, practical repo demonstrating **next-word prediction** using two RNN variants:

- **`appLSTM.py`** — Next-word inference using a pretrained **LSTM** model  
- **`appGRU.py`** — Next-word inference using a pretrained **GRU** model

This README is based on the repository contents you provided and is a short, professional guide to understand and run the project.

---

## ✅ Highlights
- Two lightweight Streamlit apps for interactive next-word prediction.  
- Pretrained models included (`.h5`) plus tokenizer (`token.pickle`).  
- Simple pipeline: tokenization → windowing/padding → model inference.  
- Notebooks included for experiment & retraining.

---

## 📦 Project Tree (core)
```

Next-Word-Prediction-using-GRU-LSTM/
├── appLSTM.py               # Streamlit app: LSTM inference (main)
├── appGRU.py                # Streamlit app: GRU inference (main)
├── next_word_LSTM.h5        # Pretrained LSTM model
├── next_word_GRU.h5         # Pretrained GRU model
├── token.pickle             # Tokenizer (vocab → index) required at inference
├── hamlet.txt               # Sample corpus used for experiments/training
├── experiements.ipynb       # LSTM training / experiments notebook
├── experiements GRU.ipynb   # GRU training / experiments notebook
└── requirements.txt         # Python dependencies

````

---

## 🔎 What’s inside (brief)
- **Models:** `next_word_LSTM.h5`, `next_word_GRU.h5` — Keras models saved after training.  
- **Tokenizer:** `token.pickle` — must match the model used.  
- **Corpus / Notebooks:** training & experimentation are documented in the included notebooks.  
- **Apps:** Streamlit-based UI for quick manual testing and demos.

---

## ⚙️ Requirements & environment
Install dependencies from the repo:

```bash
python -m venv .venv
# Activate:
# Windows: .venv\Scripts\activate
# macOS / Linux: source .venv/bin/activate

pip install -r requirements.txt
# If resource constrained: consider `pip install tensorflow-cpu`
````

---

## ▶️ Quick start — run locally

Run the **LSTM** app:

```bash
streamlit run appLSTM.py
```

Run the **GRU** app:

```bash
streamlit run appGRU.py
```

Open the provided Streamlit URL, type a short phrase, click **Predict Next Word** — the app returns the most probable next word.

---

## ⚡ How the apps work (one-liner)

Load `token.pickle` → convert input phrase to token indices → pad/trim to model input length → `model.predict()` → map predicted token index back to word.

---

## 🔑 Practical notes

* **Tokenizer & model must match**: always use the `token.pickle` that was used to train the respective model.
* Give **context (a few words)** for better next-word predictions.
* To **retrain or improve** results, open the notebooks, adjust corpus/parameters, and re-save `token.pickle` + model `.h5`.

---

## ⚙️ Retraining (brief)

Use the provided notebooks (`experiements.ipynb`, `experiements GRU.ipynb`) — they show preprocessing, model creation, training and saving of `token.pickle` and `.h5` model files.

---

## 📜 License

For **educational and research** purposes. Validate and test thoroughly before using in production.

---
