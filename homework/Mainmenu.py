from datetime import datetime

def check_date():
    # 獲取今天的日期
    today = datetime.today().date()
    
    # 提示使用者輸入日期
    input_date_str = input("請輸入日期（格式：YYYY-MM-DD）：")
    
    try:
        # 將輸入的日期轉換為datetime對象
        input_date = datetime.strptime(input_date_str, "%Y-%m-%d").date()
        
        # 判斷是否為今天
        if input_date == today:
            print("今日")
        else:
            print("非今日")
    except ValueError:
        print("輸入的日期格式不正確，請使用YYYY-MM-DD格式。")

# 執行日期判斷函數
check_date()