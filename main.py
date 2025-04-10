import streamlit as st
#from datetime import datetime #pip install streamlit-datetime-picker
#import pandas as pd #pip install pandas
from supabase import create_client, Client #pip install streamlit supabase

# Supabase 연결
url = st.secrets["supabase"]["url"]
key = st.secrets["supabase"]["service_key"]
supabase: Client = create_client(url, key)


st.subheader("🚌 동원훈련 수송버스 정보 검색", divider=True) 

# 사용자 입력
name = st.text_input("이름을 입력하세요").strip()
phone = st.text_input("전화번호 뒷번호 네자리를 입력하세요 ex)1234",  max_chars=4).strip()

# 검색 버튼
if st.button("버스번호 검색"):
    if not name or not phone:
        st.warning("이름과 전화번호를 모두 입력해주세요.")
    else:
        # Supabase에서 데이터 검색
        result = supabase.table("businfo").select("name, phone, busno").eq("name", name).eq("phone", phone).execute()
        data = result.data

        if data:
            #st.success("일치하는 정보를 찾았습니다:")
            for person in data:
                st.write(f"{person['name']}({person['phone']}) 님 께서는")
                #st.write(f"전화번호: {person['phone']}", max_chars=4)
                st.subheader(f"{person['busno']}번 버스에 탑승하세요. ")
        else:
            st.error("일치하는 정보를 찾을 수 없습니다.")







# # 세션 상태 초기화
# for key in ["answer1", "answer2", "answer3", "answer4", "answer5"]:
#     if key not in st.session_state:
#         st.session_state[key] = None

# # 1단계 질문
# st.subheader("1️⃣ 병역판정검사를 받으셨나요?")
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("예"):
#         st.session_state.answer1 = "예"
# with col2:
#     if st.button("아니오"):
#         st.session_state.answer1 = "아니오"

# # 2단계 질문
# if st.session_state.answer1:
#     if st.session_state.answer1 == "예":
#         st.success("검사를 받으셨군요. 검사결과참고치를 확인해보시면 정상/이상여부를 알 수 있습니다.  \n 바로가기")
#         st.subheader("2️⃣ 병역처분결과를 선택해주세요")
#         col1, col2, col3, col4, col5 = st.columns(5)
#         with col1:
#             if st.button("현역병입영대상", key="btn2_hy"):
#                 st.session_state.answer2 = "현역병입영대상"
#         with col2:
#             if st.button("사회복무요원", key="btn2_sh"):
#                 st.session_state.answer2 = "사회복무요원"
#         with col3:
#             if st.button("전시근로역", key="btn2_5"):
#                 st.session_state.answer2 = "전시근로역"
#         with col4:
#             if st.button("병역면제", key="btn2_6"):
#                 st.session_state.answer2 = "병역면제"
#         with col5:
#             if st.button("재신체검사대상", key="btn2_7"):
#                 st.session_state.answer2 = "재신체검사대상"
#     elif st.session_state.answer1 == "아니오":
#         st.warning("병역판정검사 절차 안내 바로가기")
#         st.subheader("2️⃣ 검사를 받으신 후에 궁금한 사항을 조회해보세요")
#         col1, col2, col3 = st.columns(3)
#         with col1:
#             if st.button("현역병", key="btn2_family"):
#                 st.session_state.answer2 = "현역병입영대상"
#         with col2:
#             if st.button("사회복무요원", key="btn2_friend"):
#                 st.session_state.answer2 = "사회복무요원"
#         with col3:
#             if st.button("아무것도", key="btn2_none"):
#                 st.session_state.answer5 = "잘모르겠다"

# # 3단계 질문
# if st.session_state.answer2 == "현역병입영대상":
#     st.success("현역병입영대상자로 판정받으셨군요.")
#     st.subheader("3️⃣ (고등학교)이상 재학중인 학생인가요?")
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("예", key="btn3_walk"):
#             st.session_state.answer3 = 1
#     with col2:
#         if st.button("아니오", key="btn3_music"):
#             st.session_state.answer3 = 0

# # 4단계 질문
# if st.session_state.answer3 == 1:
#     st.subheader("4️⃣ 빠르게 입영하고 싶으신가요?")
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("예", key="btn4_1"):
#             st.session_state.answer4 = "1네"
#     with col2:
#         if st.button("아니오", key="btn4_2"):
#             st.session_state.answer4 = "1아니"
# elif st.session_state.answer3 == 0:
#     st.subheader("4️⃣ 빠르게 입영하고 싶으신가요?")
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("예", key="btn4_3"):
#             st.session_state.answer4 = "2네"
#     with col2:
#         if st.button("아니오", key="btn4_4"):
#             st.session_state.answer4 = "2아니니"
#     #st.success("(재학생입영연기 이외의) 입영일자 연기 제도를 안내해드립니다.  \n 바로가기")


# # 5단계 질문
# if st.session_state.answer4 == "1네":
#     st.subheader("5️⃣ 입영방법을 선택해주세요")
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         if st.button("당해연도 본인선택", key="btn5_1"):
#             st.session_state.answer5 = "당해연도"
#     with col2:
#         if st.button("다음연도 본인선택", key="btn5_2"):
#             st.session_state.answer5 = "다음연도"
#     with col3:
#         if st.button("모집병 지원", key="btn5_3"):
#             st.session_state.answer5 = "모집병"
#     with col4:
#         if st.button("잘모르겠다", key="btn5_4"):
#             st.session_state.answer5 = "잘모르겠다"

# elif st.session_state.answer4 == "1아니":
#     st.success("고등학교 이상 재학중일때는 학제별 제한연령에 따라 입영이 직권으로 연기됩니다.  \n 예) 4년제 대학 제한연령 : 24세 / 2년제 대학 제한연령 : 22세")      
# elif st.session_state.answer4 == "2네":
#     st.success("고등학교 이상 재학중일때는 학제별 제한연령에 따라 입영이 직권으로 연기됩니다.  \n 예) 4년제 대학 제한연령 : 24세 / 2년제 대학 제한연령 : 22세")      
# elif st.session_state.answer4 == "2아니":
#     st.success("고등학교 이상 재학중일때는 학제별 제한연령에 따라 입영이 직권으로 연기됩니다.  \n 예) 4년제 대학 제한연령 : 24세 / 2년제 대학 제한연령 : 22세")      

# #최종 분기
# if st.session_state.answer5 == "당해연도":
#     st.success("당해연도 입영일자 본인선택 제도 안내  \n 바로가기")
# elif st.session_state.answer5 == "다음연도":
#     st.success("다음연도 입영일자 본인선택 제도 안내  \n 바로가기")
# elif st.session_state.answer5 == "모집병":
#     st.success("현역병모집지원 안내  \n 바로가기")
# elif st.session_state.answer5 == "잘모르겠다":
#     st.success("병역진로설계를 받아보세요.  \n 바로가기")



#     # st.markdown("---")
#     # st.subheader("💬 당신을 위한 오늘의 메시지:")
#     # st.success(st.session_state.answer4)
