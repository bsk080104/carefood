import streamlit as st

st.markdown("""
    <style>
    h1 { font-size: 34px !important; font-weight: bold; color: #1B5E20; }
    .sub-title { font-size: 24px !important; color: #555555; margin-bottom: 20px; }
    .q-font { font-size: 24px !important; font-weight: bold; margin-top: 25px; color: #222222; }
    .result-title { font-size: 28px !important; color: #0D47A1; font-weight: bold; }
    .food-box { background-color: #F1F8E9; padding: 25px; border-radius: 12px; border-left: 6px solid #4CAF50; }
    
    .stCheckbox label p, .stRadio label p {
        font-size: 22px !important;
        font-weight: 500 !important;
        line-height: 1.5 !important;
    }
    
    div.stButton > button p {
        font-size: 26px !important;
        font-weight: bold !important;
    }
    div.stButton > button {
        padding: 15px 30px !important;
        width: 100% !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("어르신 맞춤형 영양식품 추천")
st.markdown('<p class="sub-title">나이, 만성질환, 저작능력을 조합하여 어르신께 최적의 음식을 제안합니다!</p>', unsafe_allow_html=True)
st.write("---")

st.markdown('<p class="q-font">1. 귀하의 연령대는 어떻게 되십니까?</p>', unsafe_allow_html=True)
age = st.radio("연령 선택", ["60대", "70대", "80대 이상"], index=0)

st.markdown('<p class="q-font">2. 현재 관리 중이거나 신경 쓰이시는 질환이 있으신가요? (복수 선택 가능)</p>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    bp = st.checkbox("고혈압")
    sugar_dis = st.checkbox("당뇨")
with col2:
    lipids = st.checkbox("고지혈증/이상지질혈증")
    joints = st.checkbox("관절염/골다공증")
no_disease = st.checkbox("없음")

st.markdown('<p class="q-font">3. 평소 음식을 드실 때 씹거나 삼키는 데 어려움이 있으신가요?</p>', unsafe_allow_html=True)
chew = st.radio("식감 선호도 선택", [
    "딱딱한 과일이나 고기도 잘 씹을 수 있음",
    "부드러운 고기나 나물류 선호",
    "부드러운 죽이나 마시는 음료 선호"
], index=0)

st.write("")
st.write("---")

if st.button("맞춤 식품 추천 결과 보기"):
    st.markdown('<p class="result-title">분석 결과</p>', unsafe_allow_html=True)

    protein_spek = ""
    if "60대" in age:
        protein_spek = "한 끼 단백질 15g"
    elif "70대" in age:
        protein_spek = "한 끼 단백질 20g 및 소화효소 첨가"
    else:
        protein_spek = "한 끼 단백질 25g 이상 필수"

    selected_diseases = []
    nutrients_needed = []

    if no_disease or not (bp or sugar_dis or lipids or joints):
        selected_diseases.append("일반 건강군")
        nutrients_needed.append("기력 회복 및 노화 방지를 위한 5대 영양소 균형 지키기")
    else:
        if bp:
            selected_diseases.append("고혈압")
            nutrients_needed.append("나트륨 1회 400mg 이하 섭취 권장")
        if sugar_dis:
            selected_diseases.append("당뇨")
            nutrients_needed.append("정제당 피하고 대체당 섭취 권장")
        if lipids:
            selected_diseases.append("고지혈증/이상지질혈증")
            nutrients_needed.append("포화지방 피하고 오메가-3 불포화지방산 섭취 권장")
        if joints:
            selected_diseases.append("관절염/골다공증")
            nutrients_needed.append("칼슘 및 비타민D 섭취 권장")

    disease_count = len(selected_diseases) if "일반 건강군" not in selected_diseases else 0

    if "딱딱한 과일이나 고기도 잘 씹을 수 있음" in chew:
        texture_grade = "일반 식품 섭취 가능"
        if disease_count >= 2:
            food_recommend = "현미 잡곡밥과 두부, 버섯 반찬"
        elif bp:
            food_recommend = "다시마로 육수를 낸 소고기 무국"
        elif sugar_dis:
            food_recommend = "현미 잡곡밥과 돼지고기 수육"
        elif lipids:
            food_recommend = "고등어 시래기 조림"
        elif joints:
            food_recommend = "멸치로 육수를 낸 뼈없는 감자탕"
        else:
            food_recommend = "버섯 불고기 볶음밥"

    elif "부드러운 고기나 나물류 선호" in chew:
        texture_grade = "연화식 위주 식단 필요"
        if disease_count >= 2:
            food_recommend = "기름기를 뺀 닭안심 찜"
        elif bp:
            food_recommend = "들깨 소스를 얹은 삼치구이"
        elif sugar_dis:
            food_recommend = "으깬 단호박을 얹은 닭가슴살 샐러드"
        elif lipids:
            food_recommend = "토마토 소스를 얹은 삼치 찜"
        elif joints:
            food_recommend = "으깬 브로콜리에 치즈를 얹은 감자조림"
        else:
            food_recommend = "부드러운 계란을 넣은 찜"

    else:
        texture_grade = "액체류 식단 필요"
        if disease_count >= 2:
            food_recommend = "소금을 빼고 들깨가루를 넣은 단호박 죽"
        elif bp:
            food_recommend = "소금을 넣지 않은 표고버섯 야채죽"
        elif sugar_dis:
            food_recommend = "통귀리를 넣은 소고기 죽"
        elif lipids:
            food_recommend = "들깨와 대두 가루를 넣은 버섯죽"
        elif joints:
            food_recommend = "검은콩 and 흑임자를 갈아넣은 죽"
        else:
            food_recommend = "소고기를 갈아넣은 전복죽"

    st.markdown(f"""
    <div class="food-box">
        <p style="font-size: 20px;"><b>분석 대상 특징:</b> {age} / {', '.join(selected_diseases)} 관리군</p>
        <p style="font-size: 20px;"><b>[나이 반영] 단백질 :</b> <span style="color:#2E7D32; font-weight:bold;">{protein_spek}</span></p>
        <p style="font-size: 20px;"><b>[질환 반영] 영양 지침:</b> {', '.join(nutrients_needed)}</p>
        <p style="font-size: 20px;"><b>[식감 반영] 물성 단계:</b> <span style="color:#E65100; font-weight:bold;">{texture_grade}</span></p>
        <hr style="border: 0.5px solid #81C784;">
        <p style="font-size: 25px; color: #1565C0;"><b>최종 추천 식품: [{food_recommend}]</b></p>
    </div>
    """, unsafe_allow_html=True)
