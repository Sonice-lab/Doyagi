from datetime import datetime

def check_youth_startup_eligibility(birth_date_str, start_date_str, app_date_str):
    try:
        # 1. 입력받은 문자열(YYYYMMDD)을 datetime 객체로 변환
        birth_date = datetime.strptime(birth_date_str, "%Y%m%d").date()
        start_date = datetime.strptime(start_date_str, "%Y%m%d").date()
        app_date = datetime.strptime(app_date_str, "%Y%m%d").date()
    except ValueError:
        return "⚠️ 오류: 날짜 형식이 올바르지 않습니다. YYYYMMDD 형식(예: 19870101)으로 정확히 입력해주세요."

    # 2. 창업일 기준 대표자의 만 나이 계산
    age_at_start = start_date.year - birth_date.year - ((start_date.month, start_date.day) < (birth_date.month, birth_date.day))

    # 3. 사업개시년수 계산 (참여신청일 기준)
    biz_years = app_date.year - start_date.year - ((app_date.month, app_date.day) < (start_date.month, start_date.day))

    # 4. 기준일 설정 ('86.1.1 이후 출생자 여부 판단용)
    limit_birth_date = datetime(1986, 1, 1).date()

    # ---------------------------------------------------------
    # 적격 여부 심사 로직
    # ---------------------------------------------------------
    
    # [나] 요건: 창업일 기준 대표 나이가 만 15세 ~ 39세가 아닌 경우
    if not (15 <= age_at_start <= 39):
        return "청년창업기업 유형으로 사업을 참여할 수 없습니다.(사유: 사업창업일 기준 대표나이가 청년이 아님)"

    # [다] 요건: 참여신청일 현재 사업주가 청년('86.1.1. 이후 출생자)이 아닌 경우
    if birth_date < limit_birth_date:
        return "청년창업기업 유형으로 사업을 참여할 수 없습니다.(사유:청년일자리도약장려금사업 참여신청일 현재 사업주가 청년(‘86.1.1. 이후 출생자)이 아님)"

    # [라] 요건: 참여신청일 현재 사업개시일로부터 7년이 초과한 경우
    if biz_years >= 7:
        return "청년창업기업 유형으로 사업을 참여할 수 없습니다.(사유:청년일자리도약장려금사업 참여신청일 현재 사업을 개시한 날부터 7년이 초과한 기업임)"

    # [가] 요건: 모든 조건 충족 (적격)
    return f"적격입니다(나이 적격, 사업개시년수(적격, ({biz_years}년)). 5인 미만이어도 다른 요건이 충족된다면, 사업에 참여하실 수 있습니다. 연매출액 심사 절차를 진행해주세요."

def main():
    print("=" * 50)
    print("       🏢 청년창업기업 적격 여부 자가진단 시스템")
    print("=" * 50)
    print("※ 날짜는 모두 8자리 숫자(YYYYMMDD) 형태로 기입해주세요.")
    print("※ 프로그램을 종료하시려면 언제든지 'q' 또는 'Q'를 입력하세요.\n")
    
    while True:
        # 1. 생년월일 입력
        birth_date_str = input("1. 청년 대표자의 생년월일을 입력하세요(예시:19870101): ").strip()
        if birth_date_str.lower() == 'q':
            print("\n시스템을 종료합니다. 이용해 주셔서 감사합니다.")
            break
            
        # 2. 사업개시일 입력
        start_date_str = input("2. 사업개시일을 입력하세요(예시:20260413): ").strip()
        if start_date_str.lower() == 'q':
            print("\n시스템을 종료합니다. 이용해 주셔서 감사합니다.")
            break
            
        # 3. 사업참여일 입력
        app_date_str = input("3. 사업참여일(도약장려금 신청일)을 입력하세요(예시:20260618): ").strip()
        if app_date_str.lower() == 'q':
            print("\n시스템을 종료합니다. 이용해 주셔서 감사합니다.")
            break
        
        # 결과 출력
        print("\n" + "-" * 50)
        print("📊 [심사 결과]")
        result = check_youth_startup_eligibility(birth_date_str, start_date_str, app_date_str)
        print(result)
        print("-" * 50 + "\n")

# 프로그램 실행
if __name__ == "__main__":
    main()