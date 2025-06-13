import streamlit as st
import hashlib
import random

st.set_page_config(page_title="이름 성향 분석기 🔮", page_icon="🎨")
st.title("🔮 이름 성향 분석기")
st.markdown("당신의 이름에서 느껴지는 **직업, 색상, 분위기**를 AI 없이 재미로 분석해드려요! 😄")

# 후보 리스트
jobs = [
    "패션 디자이너", "백엔드 개발자", "시인", "요리사", "음악가", 
    "마케팅 전략가", "게임 기획자", "사진작가", "UX 디자이너", "심리상담사"
]

colors = [
    ("하늘색", "#87CEEB"), ("레몬 옐로우", "#FFF44F"), ("연보라", "#D8BFD8"),
    ("모스 그린", "#8A9A5B"), ("산호색", "#FF7F50"), ("민트", "#98FF98"),
    ("네이비 블루", "#000080"), ("살구색", "#FFDAB9"), ("복숭아색", "#FFD1DC"),
    ("블러디 레드", "#B22222")
]

vibes = [
    "차분하고 지적인 느낌이에요.",
    "에너지가 넘치고 긍정적인 분위기에요!",
    "감성적이고 예술적인 느낌이 강해요.",
    "친절하고 따뜻한 인상을 줘요.",
    "신비롭고 깊은 분위기가 느껴져요.",
    "유쾌하고 매력적인 사람이에요.",
    "섬세하고 배려심 많은 느낌이에요.",
    "강단 있고 리더십 있는 분위기에요.",
    "순수하고 따뜻한 감성이 있어요.",
    "개성 넘치고 창의적인 느낌이에요!"
]

# 이름 해시로 숫자 생성
def name_to_seed(name):
    name_bytes = name.encode("utf-8")
    return int(hashlib.sha256(name_bytes).hexdigest(), 16)

# 입력
name = st.text_input("📝 이름을 입력하세요:")

if name:
    seed = name_to_seed(name)
    random.seed(seed)  # 이름 기반 고정된 결과

    job = random.choice(jobs)
    color_name, hex_code = random.choice(colors)
    vibe = random.choice(vibes)

    st.markdown("🧠 **분석 결과**")
    st.markdown(f"- 직업: **{job}**")
    st.markdown(f"- 색상: **{color_name}** (`{hex_code}`)")
    st.markdown(f"- 분위기: *{vibe}*")

    st.markdown("🎨 어울리는 색상 미리보기:")
    st.color_picker("이 색이에요!", hex_code, label_visibility="collapsed")

    st.markdown("---")
    st.markdown("🔁 이름을 바꿔가며 테스트해보세요!")
