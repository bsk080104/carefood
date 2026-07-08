%%writefile app.py
import streamlit as st
st.markdown("""
    <style>
    h1 { font-size: 34px !important; font-weight: bold; color: #1B5E20; }
    .q-font { font-size: 24px !important; font-weight: bold; margin-top: 25px; color: #222222; }
    .result-title { font-size: 28px !important; color: #0D47A1; font-weight: bold; }
    .food-box { background-color: #F1F8E9; padding: 25px; border-radius: 12px; border-left: 6px solid #4CAF50; }
    </style>
""", unsafe_allow_html=True)

st.title("어르신 맞춤형 영양식품 추천")
st.write("나이, 만성질환, 저작능력을 조합하여 어르신께 최적의 음식을 제안합니다!")
st.write("---")

# 1. 연령대 입력
st.markdown('<p class="q-font">1. 귀하의 연령대는 어떻게 되십니까?</p>', unsafe_allow_html=True)
age = st.radio("연령 선택", ["60대", "70대", "80대 이상"], index=0)

# 2. 만성 질환 입력 (★해당 없음 선택지 추가)
st.markdown('<p class="q-font">2. 현재 관리 중이거나 신경 쓰이시는 질환이 있으신가요? (복수 선택 가능)</p>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    bp = st.checkbox("고혈압")
    sugar_dis = st.checkbox("당뇨")
with col2:
    lipids = st.checkbox("고지혈증/이상지질혈증")
    joints = st.checkbox("관절염/골다공증")
no_disease = st.checkbox("없음")

# 3. 저작 능력 입력
st.markdown('<p class="q-font">3. 평소 음식을 드실 때 씹거나 삼키는 데 어려움이 있으신가요?</p>', unsafe_allow_html=True)
chew = st.radio("식감 선호도 선택", [
    "딱딱한 과일이나 고기도 잘 씹을 수 있음",
    "부드러운 고기나 나물류 선호",
    "부드러운 죽이나 마시는 음료 선호"
], index=0)

st.write("")
st.write("---")

# 🚀 [조립식 알고리즘 가동]
if st.button("맞춤 식품 추천 결과 보기"):
    st.markdown('<p class="result-title">분석 결과</p>', unsafe_allow_html=True)

    # 연령별 단백질 스펙 계산
    protein_spek = ""
    if "60대" in age:
        protein_spek = "한 끼 단백질 15g"
    elif "70대" in age:
        protein_spek = "한 끼 단백질 20g 및 소화효소 첨가"
    else:
        protein_spek = "한 끼 단백질 25g 이상 필수"

    # 질환 조합별 영양 제한 수치 계산
    selected_diseases = []
    nutrients_needed = []

    # '질환 없음'을 체크했거나, 아무것도 체크하지 않은 경우 처리
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

    # 저작 능력에 따른 최종 제형 및 메뉴 조립
    disease_count = len(selected_diseases) if "일반 건강군" not in selected_diseases else 0

    if "딱딱한 과일이나 고기도 잘 씹을 수 있음" in chew:
        texture_grade = "독립 섭취군 [1단계 일반 제형]"
        if disease_count >= 2:
            food_recommend = "영양 밸런스 균형식 '고단백 저염 두부면 샐러드 믹스'"
        elif sugar_dis:
            food_recommend = "대체당을 활용한 '당조절 오곡 통곡물 쌈밥'"
        elif "일반 건강군" in selected_diseases:
            food_recommend = "면역력 증진을 위한 '고단백 버섯 불고기 영양 쌈밥 한상'"
        else:
            food_recommend = "기력 회복을 위한 '고단백 현미 한정식 차림'"

    elif "부드러운 고기나 나물류 선호" in chew:
        texture_grade = "잇몸 섭취군 [2단계 연화식(Soft Food)]"
        if disease_count >= 2:
            food_recommend = "저염·저당 기술을 적용한 '효소 처리 부드러운 생선 조림'"
        elif bp:
            food_recommend = "천연 육수로 맛을 낸 '저염 부드러운 소갈비찜'"
        elif "일반 건강군" in selected_diseases:
            food_recommend = "성장·회복을 돕는 '효소 연화 특제 한우 아롱사태 찜'"
        else:
            food_recommend = "부드럽게 찐 '칼슘 강화 고단백 두부 스테이크'"

    else:
        texture_grade = "혀/설로 섭취군 [3단계 고밀도 유동식]"
        if disease_count >= 2:
            food_recommend = "복합 만성질환자용 프리미엄 메디푸드 '정밀 영양 녹두죽'"
        elif sugar_dis:
            food_recommend = "혈당 정체용 천연 대체당 '스테비아 검은콩 영양죽'"
        elif "일반 건강군" in selected_diseases:
            food_recommend = "소화 흡수가 빠른 '고단백 전복 타우린 영양 미음'"
        else:
            food_recommend = "소화가 잘되는 '고칼슘 뉴트리션 단호박 미음'"

    # 결과 출력
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
