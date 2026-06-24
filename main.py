import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from the .env file
load_dotenv()

# Initialize the FastAPI app
app = FastAPI(
    title="SchemaGenie API",
    description="Backend engine for the AI SQL Companion & DBMS Tutor"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the Groq client
try:
    client = Groq()
except Exception as e:
    print(f"Initialization Error: Ensure GROQ_API_KEY is set in your .env file. Details: {e}")

# Define data schemas
class GenerateRequest(BaseModel):
    prompt: str

class GenerateResponse(BaseModel):
    response: str

# Concrete system instructions to control model behavior and domain focus
SYSTEM_PROMPT = """You are SchemaGenie, an expert Database Administrator, Senior SQL Engineer, and DBMS Professor. 
Your purpose is to assist users with writing optimized database queries, explaining core relational database concepts, and translating natural language into schema-valid SQL.

When responding to queries:
1. If the user asks for an SQL query, provide a clean, optimized SQL code block using uppercase keywords (e.g., SELECT, JOIN, WHERE). Follow up with a breakdown of the relational algebra or logic behind the query, and include a brief note on performance optimization (like indexes).
2. If the user asks a theoretical DBMS question (e.g., Normalization, Transaction Management, Indexing structures), provide highly structured explanations using bullet points, clear headings, and markdown tables if applicable.
3. If the user provides a prompt completely unrelated to databases, SQL, or computer science engineering, politely redirect them back to database topics.

Always format code snippets clearly inside markdown code blocks (e.g., ```sql ... ```)."""

@app.post("/generate", response_model=GenerateResponse)
async def generate_sql_or_theory(req: GenerateRequest):
    if not req.prompt.strip():
        raise HTTPException(status_code=400, detail="The prompt workspace cannot be empty.")
    
    try:
        # Call the Groq SDK using the specified model and tailored system message
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": req.prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.3,  # Lower temperature for more precise, deterministic technical outputs
        )
        
        answer = chat_completion.choices[0].message.content
        return GenerateResponse(response=answer)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Groq Engine Error: {str(e)}")