import datetime
today = datetime.datetime.now().date()
today_human_readable = today.strftime("%d %b, %Y")
current_year = datetime.datetime.now().date().year
xmas = datetime.date(current_year,12,25)
days_before_x = xmas - today
print(f"""
Today is: {today_human_readable}
Days before X-mas: {days_before_x.days}
""")
