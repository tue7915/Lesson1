from datetime import datetime

def months_until_today(input_date_str):
    # 解析輸入的日期字串
    input_date = datetime.strptime(input_date_str, "%Y-%m-%d")
    
    # 獲取今天的日期
    today = datetime.today()
    
    # 計算年和月的差異
    years_diff = today.year - input_date.year
    months_diff = today.month - input_date.month
    
    # 總的月份差異
    total_months_diff = years_diff * 12 + months_diff
    
    return total_months_diff

# 提示使用者輸入日期
input_date_str = input("請輸入日期（格式：YYYY-MM-DD）：")
months_left = months_until_today(input_date_str)
print(f"從輸入日期到今天有 {months_left} 個月。")