import streamlit as st
from datetime import datetime #pip install streamlit-datetime-picker
import pandas as pd #pip install pandas
from supabase import create_client, Client #pip install streamlit supabase

# Supabase 연결
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)

# UI 예시
st.title("버스번호 조회")
name = st.text_input("이름")
phone = st.text_input("전화번호 뒷자리 (4자리)", max_chars=4)


if st.button("조회하기"):
    st.write(name, phone) 
    if not name or not phone:
        st.error("이름과 전화번호 뒷자리를 모두 입력해주세요.")
    else:
        res = supabase.table("businfo").select("busno, irno").eq("name", name).eq("phone", phone).execute()
        #st.write(res) #결과찍어보기
        busno = res.data[0]['busno']
        irno = res.data[0]['irno']
        if res.data:
            st.success(f"당신의 버스번호는: {busno} {irno}")
        else:
            st.warning("일치하는 정보가 없습니다.")

