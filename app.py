Python
import streamlit as st
import google.generativeai as genai

st.title("🔍 旅路の荘ログイン不要のAI検索アプリ")

# APIキーの設定
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# 利用可能なモデルを自動的に探す
valid_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]

if valid_models:
    # 見つかった最初のモデル名（models/以降）を自動設定
    target_model = valid_models[0].replace("models/", "")
    model = genai.GenerativeModel(target_model)
    
    user_query = st.text_input("質問を入力してください：")
    
    if st.button("検索"):
        if user_query:
            try:
                response = model.generate_content(user_query)
                st.write(response.text)
            except Exception as e:
                st.error(f"エラー詳細: {e}")
else:
    st.error("利用可能なAIモデルが見つかりません。")
