import streamlit as st
import requests

st.title("Ollama Simple UI Chat")

user_input = st.text_input("پیام خود را بنویسید:")

if st.button("ارسال"):
    if user_input.strip() == "":
        st.warning("لطفا یک پیام وارد کنید!")
    else:
        # فرض کنیم سرویس ollama روی localhost و پورت 12345 فعال است
        url = "http://localhost:12345/api/generate"  # این آدرس را با توجه به api backend خودت تنظیم کن
        payload = {'message': user_input}
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                data = response.json()
                answer = data.get("response", "پاسخی دریافت نشد!")
                st.success(f"پاسخ: {answer}")
            else:
                st.error(f"خطا در سرویس: {response.status_code}")
        except Exception as e:
            st.error(f"ارتباط با سرور برقرار نشد: {e}")
