# 🏥 Aetna In-Network API

This project provides an API interface to **in-network negotiated rates and healthcare provider data** from Aetna's Machine Readable Files (MRFs). It allows developers and analysts to query normalized, structured data extracted from the official JSON datasets.

---

## 📚 About the Data

The data in `aetna.db` comes from Aetna's public transparency API, which contains:

- **In-network negotiated rates** between Aetna and healthcare providers
- **Billing codes** (CPT, DRG, etc.)
- **Negotiated prices** and billing modifiers
- **Provider reference information**
- **Provider groups and NPIs (National Provider Identifiers)**

This information is essential for **healthcare pricing transparency**, analytics, and regulatory compliance with the **Transparency in Coverage Final Rule**.

---

## 🔧 Tech Stack

- **Python 3.11+**
- **FastAPI** – modern, async-ready web framework
- **SQLAlchemy** – ORM for managing the database
- **SQLite** – local lightweight database (can be switched to PostgreSQL)
- **Uvicorn** – ASGI server for running FastAPI
- **tmux** – terminal multiplexer to keep the API running on server

---

## 🚀 How to Run Locally

git clone https://github.com/devid-saakyan/ActualSolutionsTestTask.git
cd ActualSolutionsTestTask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
download aetna.db here (https://drive.google.com/drive/folders/13QU3O6fg-Rm8Wa3MqMMG0z9z00MGbynv?usp=sharing) and change links, there is only 10% of all dataset
Also you can download fully database via that link
uvicorn main:app --reload

## 🚀 You can access the live Swagger UI at 👉 http://188.116.25.250:8005/docs#/
