# streamlit_app.py
import streamlit as st
import requests
import random


st.title("新年のあいさつ生成器")

name = st.text_input("名前を入力してください")
year = st.number_input("年を入力してください", min_value=2020, max_value=2100, value=2023)

if st.button("あいさつを生成"):
    #response = requests.post("http://127.0.0.1:8000/generate-greeting", json={"name": name, "year": year})
    response = requests.post('https://hyear.onrender.com/generate-greeting', json={"name": name, "year": year})
    if response.status_code == 200:
        st.write(response.json()["greeting"])
    else:
        st.write("エラーが発生しました")