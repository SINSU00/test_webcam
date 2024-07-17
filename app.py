import streamlit as st
import cv2

st.title("Webcam Test")

# 웹캠 인덱스 설정 (기본값: 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("웹캠에 접근할 수 없습니다. 웹캠이 올바르게 연결되어 있는지 확인하세요.")
else:
    st.write("웹캠이 정상적으로 연결되었습니다.")
    # 웹캠에서 프레임을 읽어오기
    ret, frame = cap.read()
    if ret:
        # OpenCV 이미지를 Streamlit에서 표시할 수 있는 형식으로 변환
        st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

cap.release()
