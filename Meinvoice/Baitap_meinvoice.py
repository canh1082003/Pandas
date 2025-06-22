import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from type import MEINVOICE_URL, Ma_Hoa_Don
import time
from read import get_invoice_data
from logger_config import setup_logger
from chrome_config import create_chrome_driver

logger = setup_logger()
driver = create_chrome_driver()
wait = WebDriverWait(driver, 20)

invoices = get_invoice_data("meinvoice.xlsx")

for row in invoices:
    ma_hoa_don = row.get("Mã Tra Cứu")
    url = row.get("Url")

    logger.info(f"Truy cập: {url}")
    driver.get(url)

    logger.info(f"Nhập mã hóa đơn: {ma_hoa_don}")
    try:
        input_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Nhập mã tra cứu hóa đơn']")))
        input_box.clear()
        input_box.send_keys(ma_hoa_don)

        search_button = wait.until(EC.element_to_be_clickable((By.ID, "btnSearchInvoice")))
        search_button.click()
        time.sleep(3)

        invoice_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.download-invoice")))
        invoice_button.click()

        download_pdf_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.dm-item.pdf.txt-download-pdf")))
        download_pdf_button.click()

        logger.info(f"Mã hóa đơn {ma_hoa_don} hợp lệ. Đã tải PDF.")
    except Exception as e:
        logger.warning(f"Mã hóa đơn {ma_hoa_don} không hợp lệ hoặc lỗi: {e}")
        continue