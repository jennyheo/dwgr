import streamlit as st
from datetime import datetime #pip install streamlit-datetime-picker
import pandas as pd #pip install pandas
from supabase import create_client, Client #pip install streamlit supabase

# Supabase 연결
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)

st.subheader("🚍 동원훈련 탑승정보 조회")
st.divider()
name = st.text_input("이름")
phone = st.text_input("전화번호 뒷자리 (4자리)", max_chars=4)
if st.button("버스정보 조회하기"):
    if not name or not phone:
        st.error("이름과 전화번호 뒷자리를 모두 입력해주세요.")
    elif not phone.isdigit():
        st.error("전화번호 뒷자리는 숫자만 입력 가능합니다.")
    elif len(phone) != 4:
        st.error("전화번호 뒷자리는 4자리로 입력해주세요.")
    else:
        first_char = name[0]
        third_char = name[2]
        phone2=phone[-3:]
        #res = supabase.table("businfo").select("busno, irno").eq("name", name).eq("phone", phone).execute()
        
        res = (supabase.table("businfo")
           .select("*")
           .like("name", f"{first_char}_{third_char}%")
           .eq("phone", phone3)
           .execute())
        
        if res.data:
            busno = res.data[0]['busno']
            irno = res.data[0]['irno']
            st.success(f"{name}님께서 승차하실 버스번호는 {busno} 입니다.")
        else:
            st.warning("일치하는 정보가 없습니다.")


    
