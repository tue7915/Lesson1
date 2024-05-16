# 匯入 datetime 模組中的 datetime 類別，以便處理日期和時間
from datetime import datetime

# 提示使用者輸入目標日期
target_date_str = input("請輸入目標日期 (YYYY-MM-DD): ")

# 定義日期格式字串，以便稍後將輸入的日期轉換成日期物件
date_format = "%Y-%m-%d"

# 使用 datetime.strptime 函數將使用者輸入的日期字符串轉換為日期物件
target_date = datetime.strptime(target_date_str, date_format)

# 取得當前日期和時間
current_date = datetime.now()

# 計算距離目標日期還有多少天，即時間差
delta = target_date - current_date

# 顯示結果，包括目標日期和距離天數
print(f"距離目標日期 {target_date_str} 還有 {delta.days} 天。")
