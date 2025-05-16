import requests
import json
import re, datetime

# 114年01月03日 12時22分00秒
def parse_line(line):
    try:
        date_match = re.match(r"^(\d{3})年(\d{2})月(\d{2})日 (\d{2})時(\d{2})分(\d{2})秒", line)
        if not date_match:
            raise ValueError("無法解析日期時間格式")

        year = int(date_match.group(1)) + 1911
        month = int(date_match.group(2))
        day = int(date_match.group(3))
        hour = int(date_match.group(4))
        minute = int(date_match.group(5))
        second = int(date_match.group(6))

        dt = datetime.datetime(year, month, day, hour, minute, second)
        pg_timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")

        return pg_timestamp

    except Exception as e:
        print(f"無法處理這行資料：{line}\n   錯誤原因：{e}")
        return None

url = "https://od.moi.gov.tw/api/v1/rest/datastore/A01010000C-001309-001"
response = requests.get(url)
data = response.json()
data = data["result"]["records"]

for item in data:
    print(f'{parse_line(item["ACCYMD"])} {item["PLACE"]} {item["CARTYPE"]}')