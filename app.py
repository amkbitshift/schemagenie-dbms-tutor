import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Configure the Streamlit page layout and theme
st.set_page_config(
    page_title="SchemaGenie - AI SQL Tutor",
    page_icon="🧙‍♂️",
    layout="centered"
)

# UI Headers
st.title("SchemaGenie 🧙‍♂️✨")
st.caption("AI SQL Companion & DBMS Architecture Tutor")

# Initialize the Groq client
try:
    client = Groq()
except Exception as e:
    st.error(f"Initialization Error: Ensure GROQ_API_KEY is set in your .env file. Details: {e}")
    st.stop()

# System Instructions
SYSTEM_PROMPT = """You are SchemaGenie, an expert Database Administrator, Senior SQL Engineer, and DBMS Professor. 
Your purpose is to assist users with writing optimized database queries, explaining core relational database concepts, and translating natural language into schema-valid SQL.

When responding to queries:
1. If the user asks for an SQL query, provide a clean, optimized SQL code block using uppercase keywords. Follow up with a breakdown of the relational algebra or logic.
2. If the user asks a theoretical DBMS question, provide highly structured explanations using bullet points, clear headings, and markdown tables.
3. If the user provides a prompt completely unrelated to databases, SQL, or computer science engineering, politely redirect them back to database topics.

Always format code snippets clearly inside markdown code blocks."""

# Initialize chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capture user input
if prompt := st.chat_input("Ask for an SQL query or explain DBMS concepts..."):
    
    # Display user prompt in the UI
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Add user prompt to session state history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate and display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Prepare the message payload with the system prompt and conversation history
        api_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        # Append history (Streamlit role maps perfectly to Groq API roles)
        for msg in st.session_state.messages:
            api_messages.append({"role": msg["role"], "content": msg["content"]})

        try:
            with st.spinner("Genie is analyzing the database request..."):
                chat_completion = client.chat.completions.create(
                    messages=api_messages,
                    model="llama-3.3-70b-versatile",
                    temperature=0.3,
                )
                
            response = chat_completion.choices[0].message.content
            message_placeholder.markdown(response)
            
            # Add assistant response to session state history
            st.session_state.messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            st.error(f"Groq Engine Error: {str(e)}")