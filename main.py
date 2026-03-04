from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
import g4f

app = FastAPI(title="DevAI API", version="1.0.0")


# ------------------------
# Models
# ------------------------

class PromptInput(BaseModel):
    prompt: str


class CodeInput(BaseModel):
    code: str


# ------------------------
# GPT Function
# ------------------------

async def ask_gpt(prompt: str):
    try:
        response = await g4f.ChatCompletion.create_async(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ------------------------
# Routes
# ------------------------

@app.get("/")
def home():
    return {"message": "DevAI API running with GPT4Free 🚀"}


@app.post("/ask")
async def ask(payload: PromptInput):
    answer = await ask_gpt(payload.prompt)
    return {"response": answer}


@app.post("/explain-error")
async def explain_error(payload: PromptInput):
    prompt = f"""
    Explain this programming error clearly and give fix suggestions:

    {payload.prompt}
    """
    answer = await ask_gpt(prompt)
    return {"explanation": answer}


@app.post("/explain-code")
async def explain_code(payload: CodeInput):
    prompt = f"""
    Explain what this code does in simple terms and mention complexity:

    {payload.code}
    """
    answer = await ask_gpt(prompt)
    return {"explanation": answer}


@app.post("/generate-tests")
async def generate_tests(payload: CodeInput):
    prompt = f"""
    Generate unit tests for this code:

    {payload.code}
    """
    answer = await ask_gpt(prompt)
    return {"tests": answer}
