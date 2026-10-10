import streamlit as st
import google.generativeai as genai

st.title("🔍 旅路の荘ログイン不要のAI検索アプリ")

# APIキーの設定
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# エラーメッセージの指示通り、最新のモデル（gemini-3.8-flash）を指定します
model = genai.GenerativeModel('gemini-3.8-flash')

user_query = st.text_input("質問を入力してください：")

if st.button("検索"):
    if user_query:
        try:
            response = model.generate_content(user_query)
            st.write(response.text)
        except Exception as e:
            st.error(f"エラー詳細: {e}")
