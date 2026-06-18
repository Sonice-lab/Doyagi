def check_eligibility():
    # 매출액 기준 요건 제외 사항
    # 1. 업력 1년 미만의 기업
    # 2. 부가가치세 과세표준증명 및 부가가치세 면세사업자 수입금액증명의 자료발급이 불가한 ’면세_법인사업자‘ 혹은 ’고유번호증을 소지한 비영리단체‘는 매출액 심사없이 사업참여 가능함
    print("=== 매출액 기준 적격 심사 프로그램 ===")
    print("(※ 어느 단계에서든 'q'를 입력하면 프로그램이 종료됩니다.)\n")
    
    while True:
        try:
            print("-" * 40)
            
            # 1. 고용보험 피보험자수 입력
            user_input1 = input("1. 고용보험 피보험자수를 입력하세요 (명): ")
            if user_input1.lower() == 'q':
                break
            insured_employees = int(user_input1)
            
            # 2. 기업의 상반기 매출액 입력
            user_input2 = input("2. 기업의 상반기 매출액을 입력하세요 (원): ")
            if user_input2.lower() == 'q':
                break
            first_half_sales = int(user_input2)
            
            # 3. 기업의 하반기 매출액 입력
            user_input3 = input("3. 기업의 하반기 매출액을 입력하세요 (원): ")
            if user_input3.lower() == 'q':
                break
            second_half_sales = int(user_input3)
            
            # 연 매출액 산정 (상반기 + 하반기)
            total_annual_sales = first_half_sales + second_half_sales
            
            # 기준 매출액 산정 (피보험자수 x 1,900만원)
            required_sales = insured_employees * 19000000
            
            print("\n--- 심사 결과 ---")
            print(f"산정된 연 매출액: {total_annual_sales:,}원")
            print(f"기준 매출액: {required_sales:,}원")
            
            # 적격 여부 판단
            if total_annual_sales >= required_sales:
                print("\n적격입니다. 다음 심사 절차를 진행해주세요.\n")
            else:
                print("\n부적격입니다.(사유: 연매출액 미달)\n")
                
        except ValueError:
            print("\n[오류] 숫자 또는 프로그램 종료를 위한 'q'만 입력해주세요.\n")
            
    print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다.")

# 프로그램 실행
if __name__ == "__main__":
    check_eligibility()