# 🛍️ LLM-Ops E-Commerce Product Recommender

## 🚀 Overview
The **LLM-Ops E-Commerce Product Recommender** is an AI-powered application that analyzes customer reviews from a CSV file and suggests the best products using **Groq LLMs** via **LangChain**.
It combines **LLM reasoning**, **data processing**, and **MLOps observability** for end-to-end intelligent product insights.


---

## 🧠 Features
- 🧾 **Automated Review Extraction:** Upload a CSV file containing product reviews.
- 💬 **Groq-Powered LLM Inference:** Uses **LangChain + Groq** to summarize, score, and interpret sentiment.
- 🔍 **Smart Recommendations:** Suggests top products based on review quality, sentiment, and frequency.
- ⚙️ **MLOps Integration:** Exposes metrics with **Prometheus** for observability and system performance.
- 🌐 **Flask Backend:** Lightweight API for serving model responses and managing LLM requests.



## ⚙️ Tech Stack
`LangChain` · `Groq` · `HuggingFace` · `Flask` · `Pandas` · `pypdf` · `Prometheus` · `Python-dotenv` · `Docker` · `Datasets`





## 🧩 Architecture
```
User → Flask API → LangChain Pipeline → Groq LLM → Recommendation Output
                              ↓
                       Prometheus Metrics
```

**Flow Explanation:**
1. A CSV file containing product reviews.
2. The system preprocesses the reviews using `pandas`.
3. Reviews are passed into **LangChain with Groq** for text summarization & ranking.
4. Results are served via a Flask endpoint or displayed in a web UI.
5. Metrics are tracked by **Prometheus** for operational monitoring.



