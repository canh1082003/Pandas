import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from type import BASE_URL 

options = Options()
driver = webdriver.Chrome(options=options)

all_data = {}
page_num = 1
MAX_PAGES = 4
while page_num <= MAX_PAGES:
    url = f"{BASE_URL}?page={page_num}&pageSize=50"
    print(f"Đang thu thập trang {page_num}: {url}")
    driver.get(url)
    time.sleep(10)

    rows = driver.find_elements(By.CSS_SELECTOR, "#dvResultSearch > table > tbody > tr")
    if not rows:
        print("Không còn dữ liệu. Dừng lại.")
        break

    data = []
    for row in rows:
        try:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) >= 4:
                ma_so_thue = cells[1].find_element(By.TAG_NAME, "strong").text.strip()
                ten_doanh_nghiep = cells[2].find_element(By.TAG_NAME, "a").text.strip()
                ngay_cap = cells[3].text.strip()
                data.append({
                    "Tên doanh nghiệp": ten_doanh_nghiep,
                    "Mã số thuế": ma_so_thue,
                    "Ngày cấp": ngay_cap
                })
        except Exception as e:
            print("Lỗi khi xử lý dòng:", e)

    all_data[f"Trang_{page_num}"] = pd.DataFrame(data)
    page_num += 1



if not all_data:
    print("Không có dữ liệu nào được thu thập.")
    exit()


downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "doanh_nghiep_mst.xlsx")
with pd.ExcelWriter(downloads_path, engine='openpyxl') as writer:
    for sheet_name, df in all_data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Đã lưu kết quả vào: {downloads_path}")
