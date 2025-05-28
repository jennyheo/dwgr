import streamlit as st
from datetime import datetime #pip install streamlit-datetime-picker
import pandas as pd #pip install pandas
from supabase import create_client, Client #pip install streamlit supabase

# Supabase 연결
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)

# UI 예시
st.title("🚌 동원훈련 버스정보 조회")
name = st.text_input("이름")
phone = st.text_input("전화번호 뒷자리 (숫자 4자리)", max_chars=4)


if st.button("조회하기"):
    if not name or not phone:
        st.warning("이름과 전화번호를 모두 입력해주세요.")
    else:
        res = supabase.table("businfo").select("busno").eq("name", name).eq("phone", phone).execute()
        if res.data:
            st.success(f"{name}님께서 탑승하실 버스는 **{res.data[0]['busno']} 번** 버스 입니다.")
        else:
            st.warning("일치하는 정보가 없습니다.")


