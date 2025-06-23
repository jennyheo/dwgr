import streamlit as st
from datetime import datetime #pip install streamlit-datetime-picker
import pandas as pd #pip install pandas
from supabase import create_client, Client #pip install streamlit supabase

# Supabase 연결
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["key"]
supabase: Client = create_client(url, key)

# UI 예시

#리런한 이후에는 여기를 보여주기
if 'kkk1' in st.session_state and st.session_state['kkk1'] is not None:
    #st.write("kkk1 is not None!")
    #조회가 성공적일때만 비상연락처를 입력한다.
    st.title("🚨 비상연락처 입력하기")
    st.divider()
    #st.write(st.session_state['kkk1'])
    #st.write(st.session_state['kkk2'])
    st.write(f"{st.session_state['kkk2']}님의 비상연락처를 입력합니다")
    #if st.button("비상연락처 입력하기"):
    inwith = st.text_input("관계")
    inphone2 = st.text_input("전화번호", max_chars=13)
    if st.button("저장하기"):
        if not inwith or not inphone2:
            st.error("본인과의 관계 및 전화번호를 모두 입력해주세요.")

else:
    st.title("🚍 동원훈련 버스정보 조회")
    st.divider()
    name = st.text_input("이름")
    phone = st.text_input("전화번호 뒷자리 (4자리)", max_chars=4)
    if st.button("버스정보 조회하기"):
        st.session_state['kkk1'] = ''
        st.session_state['kkk2'] = ''
        #st.write(name, phone) 
        if not name or not phone:
            st.error("이름과 전화번호 뒷자리를 모두 입력해주세요.")
        else:
            res = supabase.table("businfo").select("busno, irno").eq("name", name).eq("phone", phone).execute()
            #st.write(res) #결과찍어보기
            busno = res.data[0]['busno']
            irno = res.data[0]['irno']
            if res.data:
                st.success(f"{name}님께서 승차하실 버스번호는 {busno} 입니다.")
                #st.write(st.session_state['kkk1'])
                #st.write(st.session_state['kkk2'])
                if st.button("비상연락처 입력하기"):
                    st.session_state['kkk1'] = irno
                    st.session_state['kkk2'] = name
                    #st.rerun() #리런한다
            else:
                st.warning("일치하는 정보가 없습니다.")

if 'kkk1' in st.session_state :
    st.write(st.session_state['kkk1'])



    
