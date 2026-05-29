import streamlit as st

# 웹 앱의 제목 설정
st.title("🔢 구구단 2단 ~ 9단")
st.write("파이썬 반복문 코드를 그대로 웹 화면으로 옮겼습니다.")
st.write("---")

# 보내주신 구구단 반복문 구조 그대로 활용
for i in range(2, 10):
    # 각 단의 시작을 알리는 소제목 (굵은 글씨)
    st.markdown(f"### 📢 {i}단")

    for j in range(1, 10):
        # print 대신 st.write를 사용해 웹 화면에 출력
        # 연산자 기호를 곱하기(×)로 바꾸고 결과는 ** 기호로 굵게 강조했습니다.
        st.write(f"{i}  ×  {j}  =  **{i*j}**")

    # 단이 끝날 때마다 깔끔하게 가로 구분선 넣기
    st.divider()
