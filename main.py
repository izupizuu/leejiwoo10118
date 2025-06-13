import streamlit as st
import openai

st.set_page_config(page_title="이름 성향 분석기 🔮", page_icon="🎨")
st.title("🔮 이름 성향 분석기")
st.markdown("당신의 이름에서 느껴지는 **직업, 색상, 분위기**를 AI가 예측해드려요!")

openai.api_key = st.secrets["OPENAI_API_KEY"]  # 또는 환경변수 사용

name = st.text_input("📝 이름을 입력해주세요:")

if name and st.button("✨ 분석 시작하기"):
    with st.spinner("AI가 분석 중입니다... 🎨"):
        prompt = f"""
        너는 사람 이름을 듣고, 그 이름에서 느껴지는 이미지나 분위기를 분석하는 전문가야.

        이름: {name}

        아래 형식에 따라 대답해줘:
        1. 어울리는 직업 (하나)
        2. 어울리는 색상 (색 이름과 HEX 코드)
        3. 이름에서 느껴지는 분위기 (한 문장)

        예시 형식:
        - 직업: 디자이너
        - 색상: 연보라 (#D8BFD8)
        - 분위기: 부드럽고 감성적인 느낌이에요.
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,
        )

        result = response.choices[0].message.content.strip()

        st.markdown("🧠 **분석 결과**")
        st.markdown(result)

        import re
        hex_match = re.search(r"#([A-Fa-f0-9]{6})", result)
        if hex_match:
            hex_code = "#" + hex_match.group(1)
            st.markdown(f"🎨 어울리는 색상 미리보기:")
            st.color_picker("이 색이에요!", hex_code, label_visibility="collapsed")
