import streamlit as st
#from datetime import datetime #pip install streamlit-datetime-picker
#import pandas as pd #pip install pandas
#from supabase import create_client, Client #pip install streamlit supabase


# Streamlit 세션 상태에서 현재 페이지를 추적하기 위한 초기 설정
if 'page' not in st.session_state:
    st.session_state['page'] = 'main'

# 다른 페이지로 이동하는 함수
def navigate_to(page):
    st.session_state['page'] = page
    st.rerun()

col1, col2, col3 = st.columns(3)
with col1 :
    if st.button('메인', key="1-1"):
        navigate_to('main')
with col2:
    if st.button('서브1', key="1-2"):
        navigate_to('sub1')
with col3:
    if st.button('서브2', key="1-3"):
        navigate_to('sub2')

# 메인 페이지 내용 정의
def main_page():
    st.title('메인 페이지')
    st.write('여기는 메인 페이지입니다.')
    if st.button('서브1 페이지로 이동', key="2-2"):
        navigate_to('sub1')
    if st.button('서브2 페이지로 이동', key="2-3"):
        navigate_to('sub2')


# 서브1 페이지 내용 정의
def sub_page1():
    st.title('서브1 페이지')
    st.write('여기는 서브1 페이지입니다.')
    if st.button('메인 페이지로 돌아가기'):
        navigate_to('main')

# 서브2 페이지 내용 정의
def sub_page2():
    st.title('서브2 페이지')
    st.write('여기는 서브2 페이지입니다.')
    if st.button('메인 페이지로 돌아가기'):
        navigate_to('main')


# 페이지 네비게이션 로직
if st.session_state['page'] == 'main':
    main_page()
elif st.session_state['page'] == 'sub1':        
    sub_page1()
elif st.session_state['page'] == 'sub2':
    sub_page2()

