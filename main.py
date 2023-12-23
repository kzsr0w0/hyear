# fastapi_app.py
import random
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import GPT2Tokenizer, GPT2LMHeadModel

app = FastAPI()

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

class GreetingRequest(BaseModel):
    name: str
    year: int

def generate_greeting(name, year):
    new_year_words = ["希望", "幸福", "繁栄", "健康", "成功", "平和", "愛", "喜び", "幸運", "夢"]
    random_word = random.choice(new_year_words)
    
    input_text = f"新年あけましておめでとうございます、{name}さん！{year}年の目標は"
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return f"{generated_text} そして、今年も{random_word}が訪れますように"

@app.post("/generate-greeting")
async def generate_greeting_endpoint(request: GreetingRequest):
    greeting = generate_greeting(request.name, request.year)
    return {"greeting": greeting}
