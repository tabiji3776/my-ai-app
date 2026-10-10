import streamlit as st
import google.generativeai as genai

st.title("🔍 ログイン不要のAI検索アプリ")

# 隠した鍵を安全に読み込む
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-pro')

user_query = st.text_input("質問を入力してください：")

if st.button("検索"):
    if user_query:
        response = model.generate_content(user_query)
        st.write(response.text)
