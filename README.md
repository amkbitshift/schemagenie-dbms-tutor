# SchemaGenie 🧙‍♂️✨

> **AI SQL Companion & DBMS Architecture Tutor**
> 
> 🔴 **Live Application:** [Try SchemaGenie Here](https://schemagenie-dbms-tutor-wqsup8fgzfgtetzfyyn89b.streamlit.app)

SchemaGenie is an intelligent database assistant engineered to help developers write optimized queries, translate natural language into schema-valid SQL, and master core Database Management System (DBMS) architecture concepts. Powered by the **Groq SDK** and **Streamlit**, it leverages the **Llama 3.3 70B** model to deliver lightning-fast, highly precise, deterministic database engineering support.

---

## 🚀 Features

* **Natural Language to SQL:** Seamlessly converts plain-English database requests into highly optimized SQL queries using standardized uppercase syntax.
* **Query Analysis:** Breaks down generated SQL queries into relational algebra logic and explains performance mechanics.
* **DBMS Academic Tutor:** Provides structured deep-dives into complex relational database topics like Normalization (1NF to BCNF), Transaction Management (ACID), Indexing structures (B+ Trees), and Concurrency Control.
* **Chat History Memory:** Maintains session state context so you can ask follow-up questions about previous queries.
* **Clean UI:** A minimalist, markdown-supported chat interface built entirely in Python.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend & Backend** | Streamlit | Pure Python framework handling both the UI and server logic. |
| **LLM Orchestration**| Groq SDK | High-speed API interface to execute Llama-3.3-70b-versatile. |
| **Environment** | python-dotenv | Secure local environment variable management. |

---

## 📦 Project Architecture & Directory Layout

```text
schemagenie-dbms-tutor/
├── .env                  # API Authentication Credentials (Ignored by Git)
├── .gitignore            # Version control safety filters
├── app.py                # Main Streamlit Application Engine
├── requirements.txt      # Python dependencies for cloud deployment
└── README.md             # Project Documentation
