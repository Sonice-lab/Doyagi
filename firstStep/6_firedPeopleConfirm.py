from datetime import datetime
import calendar # 추가: 달의 마지막 날짜 계산을 위해 필요
try:
    from dateutil.relativedelta import relativedelta
except ImportError:
    print("오류: 필요한 라이브러리(python-dateutil)가 설치되어 있지 않습니다.")
    print("터미널에 'pip install python-dateutil'을 입력하여 설치해주세요.")
    exit()

def format_date_str(date_str):
    dt = datetime.strptime(date_str, "%Y%m%d")
    return dt.strftime("%Y년 %m월 %d일")

def run_program():
    print("=== 청년일자리도약장려금 사업 안내 프로그램 ===")
    print("종료하려면 'q'를 입력하세요.")

    while True:
        app_date_input = input("\n1. 사업참여신청일을 입력하세요 (YYYYMMDD): ")
        if app_date_input.lower() == 'q': break
        
        layoff_date_input = input("2. 고용조정이직발생 이력을 입력하세요 (없으면 N, 날짜는 YYYYMMDD): ")
        if layoff_date_input.lower() == 'q': break

        try:
            app_date = datetime.strptime(app_date_input, "%Y%m%d")
            app_date_formatted = format_date_str(app_date_input)
            
            start_q1 = datetime(2026, 1, 1)
            end_q1 = datetime(2026, 3, 31)

            # 1. 고용조정이직 이력이 없을 경우
            if layoff_date_input.upper() == 'N':
                limit_date = app_date - relativedelta(months=3)
                
                # [보완] 신청일이 해당 월의 말일인 경우(28일 이상), 3개월 전 날짜도 그 달의 말일로 보정
                if app_date.day >= 28:
                    last_day_of_month = calendar.monthrange(limit_date.year, limit_date.month)[1]
                    limit_date = limit_date.replace(day=last_day_of_month)
                
                if start_q1 <= app_date <= end_q1:
                    print(f"\n[안내] 사업참여신청일이 {app_date_formatted}로 확인됩니다.")
                    print("청년을 먼저 채용했을 경우 사업참여 신청일 기준으로 3개월 이내(2026년 01월 01일)에 채용한 청년부터 명단 등록이 가능합니다.")
                    print("※ 2025년도 채용자일 경우 고용24 사이트에서 2026년도 사업이 아닌 2025년도 사업으로 신청해주셔야하며,")
                    print("25년도 사업 또한 청년을 먼저 채용한 경우 채용일로부터 3개월이내 사업 참여신청한 경우에만 지원 가능합니다.")
                else:
                    print(f"\n[안내] 사업참여신청일이 {app_date_formatted}로 확인됩니다.")
                    print(f"청년을 먼저 채용했을 경우 사업참여 신청일 기준으로 3개월 이내({limit_date.strftime('%Y년 %m월 %d일')} 이후) 채용한 청년부터 명단 등록이 가능합니다.")

            # 2. 고용조정이직 이력이 있는 경우
            else:
                layoff_date = datetime.strptime(layoff_date_input, "%Y%m%d")
                layoff_date_formatted = format_date_str(layoff_date_input)
                
                # [핵심 보완] 발생일에서 하루를 먼저 뺀 후 3개월을 더하여 월말 계산 오류 원천 차단
                end_limit_date = (layoff_date - relativedelta(days=1)) + relativedelta(months=3)
                
                # 채용 가능 시점은 제한기간 종료일의 다음 날
                eligible_date = end_limit_date + relativedelta(days=1)
                
                print(f"\n[안내] 사업참여신청일이 {app_date_formatted}로 확인됩니다.")
                print(f"사업참여는 적격이시나, 귀사에서 고용조정이직이 {layoff_date_formatted}에 발생했기 때문에 이에 따라 사업참여제한기간이 발생합니다.")
                print(f"▶ 사업참여 제한기간: {layoff_date_formatted} ~ {end_limit_date.strftime('%Y년 %m월 %d일')}")
                print(f"▶ 채용 가능 시점: {eligible_date.strftime('%Y년 %m월 %d일')} 채용자부터 채용자 명단 등록이 가능합니다.")

        except ValueError:
            print("오류: 날짜 형식이 올바르지 않습니다. YYYYMMDD 형식으로 입력해주세요.")

if __name__ == "__main__":
    run_program()