# fastapi_app.py
import random
import string
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class GreetingRequest(BaseModel):
    name: str
    year: int

def generate_greeting(name, year):
    new_year_words = ["希望", "幸福", "繁栄", "健康", "成功", "平和", "愛", "喜び", "幸運", "夢"]
    random_word = random.choice(new_year_words)
    return f"新年あけましておめでとうございます、{name}さん！{year}年もよろしくお願いします。{random_word}が訪れますように"

@app.post("/generate-greeting")
async def generate_greeting_endpoint(request: GreetingRequest):
    greeting = generate_greeting(request.name, request.year)
    return {"greeting": greeting}
