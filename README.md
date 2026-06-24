# SchemaGenie 🧙‍♂️✨

> **AI SQL Companion & DBMS Architecture Tutor**

SchemaGenie is an intelligent database assistant engineered to help developers write optimized queries, translate natural language into schema-valid SQL, and master core Database Management System (DBMS) architecture concepts. Powered by the **Groq SDK** and **FastAPI**, it leverages the **Llama 3.3 70B** model to deliver lightning-fast, highly precise, deterministic database engineering support.

---

## 🚀 Features

* **Natural Language to SQL:** Seamlessly converts plain-English database requests into highly optimized SQL queries using standardized uppercase syntax.
* **Query Analysis:** Breaks down generated SQL queries into relational algebra logic and explains performance mechanics.
* **DBMS Academic Tutor:** Provides structured deep-dives into complex relational database topics like Normalization (1NF to BCNF), Transaction Management (ACID), Indexing structures (B+ Trees), and Concurrency Control.
* **Guardrails:** Focuses strictly on computer science, SQL, and database concepts, filtering out non-technical workspace distractions.
* **Sleek Terminal UI:** A dark-themed, terminal-inspired responsive web interface with built-in Markdown parsing to render tables, queries, and architectural lists beautifully.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend Framework** | FastAPI (Standard) | High-performance Python web framework for APIs. |
| **LLM Orchestration**| Groq SDK | High-speed interface to execute Llama-3.3-70b-versatile. |
| **Frontend UI** | HTML5, CSS3, JavaScript | Lightweight, zero-dependency, responsive interface. |
| **Markdown Engine** | Marked.js | Client-side parser to render SQL blocks and schemas dynamically. |

---

## 📦 Project Architecture & Directory Layout

```text
schemagenie-dbms-tutor/
├── .env                  # API Authentication Credentials (Ignored by Git)
├── .gitignore            # Version control safety filters
├── index.html            # Terminal Interface UX Engine
├── main.py               # FastAPI Core Router & Groq Client Setup
└── README.md             # Project Documentation
