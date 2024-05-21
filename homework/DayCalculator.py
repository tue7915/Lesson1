# 匯入 datetime 模組中的 datetime 類別，以便處理日期和時間
from datetime import datetime

# 提示使用者輸入第一個日期
date1_str = input("請輸入第一個日期 (YYYY-MM-DD): ")

# 提示使用者輸入第二個日期
date2_str = input("請輸入第二個日期 (YYYY-MM-DD): ")

# 設定日期解析的格式字串
date_format = "%Y-%m-%d"

# 將使用者輸入的日期字串轉換成日期物件
date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)

# 計算日期差距（天數）
delta = date2 - date1

# 使用格式字串顯示結果，其中delta.days是timedelta物件的屬性，代表兩日期之間的天數差距
print(f"{date1_str}與{date2_str}兩個日期之間的天數差距是 {delta.days + 1} 天。")
2