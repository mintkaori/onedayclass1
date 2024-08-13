import streamlit as st

# MBTI 성향에 대한 설명과 적합한 MBTI 유형을 반환하는 함수
def get_mbti_info(mbti_type):
    mbti_info = {
        'INTJ': ('논리적이며 계획적인 성향을 가진 INTJ는 문제 해결에 강하고 미래 지향적입니다. 목표를 세우고 이를 달성하기 위해 체계적으로 접근합니다.',
                 ['ENTP', 'INFP'], ['ESFJ', 'ISFP']),
        'ENTP': ('창의적이고 도전적인 성향을 가진 ENTP는 새로운 아이디어를 좋아하고 논쟁을 즐깁니다. 다양한 가능성을 탐색하고 혁신적인 해결책을 찾는 데 능숙합니다.',
                 ['INFJ', 'INTJ'], ['ISFJ', 'ESTJ']),
        'INFP': ('이상적이며 감성적인 성향을 가진 INFP는 자기 표현과 개인적 가치에 중점을 두며, 깊은 감정과 창의력을 가지고 있습니다.',
                 ['ENFJ', 'INFJ'], ['ESTJ', 'ENTJ']),
        'ENFJ': ('사교적이고 동정심이 많은 성향을 가진 ENFJ는 사람들과의 관계를 중시하며, 타인을 돕는 데 큰 만족을 느낍니다.',
                 ['INFP', 'ISFP'], ['ISTJ', 'INTP']),
        'ISTJ': ('책임감이 강하고 실용적인 성향을 가진 ISTJ는 세부사항에 주의를 기울이며 신뢰할 수 있는 계획적인 접근을 선호합니다.',
                 ['ESTJ', 'ISFJ'], ['ENFP', 'INFP']),
        'ESTJ': ('조직적이고 현실적인 성향을 가진 ESTJ는 구조와 규칙을 중요시하며, 실용적인 해결책을 선호합니다.',
                 ['ISTJ', 'ISFJ'], ['INFP', 'ENFP']),
        'ISFJ': ('세심하고 헌신적인 성향을 가진 ISFJ는 타인의 필요를 잘 이해하며, 안정적이고 지원적인 환경을 조성합니다.',
                 ['ESFJ', 'ISTJ'], ['ENTP', 'INTP']),
        'ESFJ': ('사교적이고 배려 깊은 성향을 가진 ESFJ는 타인과의 관계를 중요시하며, 도움을 주는 데 큰 만족을 느낍니다.',
                 ['ISFJ', 'ESTJ'], ['INTP', 'ENTP']),
        'INTP': ('논리적이고 분석적인 성향을 가진 INTP는 새로운 아이디어와 개념을 탐구하며 독립적인 작업을 선호합니다.',
                 ['ENTP', 'INFP'], ['ESFJ', 'ESTJ']),
        'ENFP': ('열정적이고 창의적인 성향을 가진 ENFP는 새로운 가능성을 탐구하며 자유롭고 개방적인 환경을 선호합니다.',
                 ['INFJ', 'INTJ'], ['ISTJ', 'ESTJ']),
        'INFJ': ('이상적이고 통찰력 있는 성향을 가진 INFJ는 깊은 이해와 감정을 기반으로 타인과의 관계를 중요시하며, 긍정적인 변화를 추구합니다.',
                 ['ENFJ', 'INFP'], ['ESTP', 'ISTP']),
        'ISTP': ('실용적이고 분석적인 성향을 가진 ISTP는 문제 해결에 있어 실용적 접근을 선호하며, 독립적이고 자유로운 작업을 즐깁니다.',
                 ['ESTP', 'ISFP'], ['ENFJ', 'ESFJ']),
        'ESTP': ('모험적이고 현실적인 성향을 가진 ESTP는 활동적이고 즉각적인 해결책을 선호하며, 새로운 경험을 즐깁니다.',
                 ['ISTP', 'ISFP'], ['INFJ', 'INFP']),
        'ISFP': ('감각적이고 내향적인 성향을 가진 ISFP는 감정적으로 풍부하며, 조용하고 평화로운 환경을 선호합니다.',
                 ['ESFP', 'INFP'], ['ESTJ', 'ENTJ']),
        'ESFP': ('사교적이고 실용적인 성향을 가진 ESFP는 현재 순간을 즐기며, 다른 사람들과 함께하는 활동을 좋아합니다.',
                 ['ISFP', 'ESTP'], ['INFJ', 'INTJ'])
    }
    
    description, compatible, incompatible = mbti_info.get(mbti_type, ('알 수 없는 MBTI 유형입니다.', [], []))
    return description, compatible, incompatible

# Streamlit 앱 설정
st.title('MBTI 성향 분석기')

# 사용자 입력 받기
name = st.text_input('이름을 입력해주세요 : ')
mbti_type = st.selectbox('당신의 MBTI 유형을 선택해주세요:', ['INTJ', 'ENTP', 'INFP', 'ENFJ', 'ISTJ', 'ESTJ', 'ISFJ', 'ESFJ', 'INTP', 'ENFP', 'INFJ', 'ISTP', 'ESTP', 'ISFP', 'ESFP'])

# 버튼 클릭 시 결과 표시
if st.button('성향 분석하기'):
    description, compatible, incompatible = get_mbti_info(mbti_type)
    
    # 결과를 예쁘게 표시
    st.markdown(f"## {name}님, 당신의 MBTI 성향은 **{mbti_type}**입니다.")
    st.markdown(f"### 성향 설명")
    st.write(description)
    
    st.markdown("### 잘 맞는 MBTI 유형")
    if compatible:
        st.markdown(f"- {', '.join(compatible)}")
    else:
        st.write("정보 없음")
    
    st.markdown("### 잘 맞지 않는 MBTI 유형")
    if incompatible:
        st.markdown(f"- {', '.join(incompatible)}")
    else:
        st.write("정보 없음")
