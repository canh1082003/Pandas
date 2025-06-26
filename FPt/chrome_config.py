from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_chrome_driver(download_dir: str = r"D:\DATA\Truong\Bt_Python\Baitap2_Pandas\FPt"):
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': download_dir,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })
    driver = webdriver.Chrome(options=chrome_options)
    return driver
