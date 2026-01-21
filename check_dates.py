import datetime

# 验证文档中的日期
dates_to_check = [
    '2026-02-15',
    '2026-02-16',
    '2026-02-17',
    '2026-02-18',
    '2026-02-19',
    '2026-02-20'
]

weekday_map = ['日', '一', '二', '三', '四', '五', '六']

print("2026年日期验证结果：")
print("=" * 50)

for date_str in dates_to_check:
    dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    weekday_idx = dt.weekday()  # 0是周一，6是周日
    # 转换为中国习惯的星期表示（0是周日，6是周六）
    china_weekday_idx = (weekday_idx + 1) % 7
    china_weekday = weekday_map[china_weekday_idx]
    print(f"{date_str} 是 星期{china_weekday}")

print("=" * 50)
