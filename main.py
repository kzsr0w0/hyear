# fastapi_app.py
import random
import string
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = FastAPI()

tokenizer = GPT2Tokenizer.from_pretrained('distilbert-base-uncased')
model = GPT2LMHeadModel.from_pretrained('distilbert-base-uncased')

class GreetingRequest(BaseModel):
    name: str
    year: int

def generate_greeting(name, year):
    new_year_words = ["希望", "幸福", "繁栄", "健康", "成功", "平和", "愛", "喜び", "幸運", "夢"]
    random_word = random.choice(new_year_words)
    
    # GPT-2モデルを使用してカスタマイズされたメッセージを生成
    input_text = f"新年あけましておめでとうございます、{name}さん！{year}年の目標は"
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    # ランダムな新年の言葉を追加して返す
    return f"{generated_text} そして、{random_word}が訪れますように。"    


@app.post("/generate-greeting")
async def generate_greeting_endpoint(request: GreetingRequest):
    greeting = generate_greeting(request.name, request.year)
    return {"greeting": greeting}