from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import g4f

app = FastAPI(title="DevAI API", version="1.0.0")

# Code
# ------------------------
# Models
# ------------------------

class PromptInput(BaseModel):
    prompt: str


class CodeInput(BaseModel):
    code: str


# ------------------------
# Provider + Model fallback list
# ------------------------

PROVIDERS = [
    (g4f.Provider.Gemini, "gemini-2.5-flash-lite"),
    (g4f.Provider.PollinationsAI, "openai-fast"),
    (g4f.Provider.DeepInfra, "MiniMax/MiniMax-M2.5"),
    (g4f.Provider.Perplexity, "turbo"),
    (g4f.Provider.Groq, "Openai/gpt-oss-20b")
]


# ------------------------
# GPT Function
# ------------------------

async def ask_gpt(prompt: str):

    last_error = None

    for provider, model in PROVIDERS:
        try:

            response = await g4f.ChatCompletion.create_async(
                model=model,
                provider=provider,
                messages=[{"role": "user", "content": prompt}],
            )

            if response:
                print(f"SUCCESS using {provider} with {model}")
                return response

        except Exception as e:
            print(f"FAILED {provider} ({model}) -> {e}")
            last_error = e

    raise HTTPException(status_code=500, detail=f"All providers failed: {last_error}")


# ------------------------
# Routes
# ------------------------

@app.get("/")
def home():
    return {"message": "DevAI API running with multi-provider fallback 🚀"}


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
