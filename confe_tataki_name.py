import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import string
import time
import codecs

# Chromeオプションの設定
chrome_options = Options()
#chrome_options.add_argument("--headless")  # ヘッドレスモード（ブラウザのGUIを表示しない）

# 名義情報
name = 'ハルカ カナタ'
tell = "09012345678"
address = 'test1234@icloud.com'

# チケット情報
# ここに選択したい公演が何公演目かを入力
stage_num = 1
# ここに選択したい演者の名前を入力
ticketName = '相川'
# ここに選択したいチケット枚数を入力
ticket_num =2


# URL
url = 'https://www.s2.e-get.jp/lrpnot/pt/&lg=-1&s=I6083J'

# 要素1
element1 = "#list_box > table.select_stage_table > tbody > tr:nth-child(2) > td.condition > p.reserve_btn_wrapper > a"
element2 = "conditon"
element3 = "#contents_wrapper > table:nth-child(8) > tbody > tr > td:nth-child(3) > a"

# 個々のURLにアクセスし、要素をチェックする関数
driver = webdriver.Chrome(options=chrome_options)
# 要素探索用
def element_exists(driver, selector):
    try:
        driver.find_element(By.CSS_SELECTOR, selector)
        return True
    except:
        return False

# リンクがあるまで探索
while True:
    print(f'アクセス: {url}')
    driver.get(url)
    if element_exists(driver, element1):
        print("Element found!")
        break
    else:
        print("Element not found, reloading...")

# 最初の画面クリック
element = driver.find_element(By.CSS_SELECTOR, element1)
element.click()
time.sleep(0.5)
# 席種選ぶ画面
element = driver.find_elements(By.CLASS_NAME, "conditon")
# 指定公演のリンクをクリック
# ※S席、A席もそれぞれ1と数える
# 例；1/1 S席(1公演目) 0
#　　 1/1 A席(1公演目) 1
# 2n-2でS席のみにしている。
# #1公演目(S席)の場合はn=1で0番目、3公演目(S席)の場合はn=3で上から4番目になる
element[2*stage_num-2].click()
time.sleep(0.5)

# 枚数選択画面(演者選ぶ画面)
#element = driver.find_elements(By.CLASS_NAME, "number")
elements = driver.find_elements(By.CLASS_NAME, "cp_sekisyu_name")
elements1 =EC.presence_of_all_elements_located((By.CLASS_NAME, "cp_sekisyu_name"))

# # 各要素をチェックし、文字列を含む要素を特定
target_index = -1
for index, element in enumerate(elements):
    if ticketName in element.text:
        target_index = index
        print(f"見つかり＼(^_^)／{target_index+1}番目!")
        break
    else :
        print("")
time.sleep(0.5)
# 指定のセレクトボックスを選ぶ
select_elements = driver.find_elements(By.CLASS_NAME, 'number')[target_index]
select = Select(select_elements)
# セレクトボックスの中で指定枚数の選択肢を選ぶ
select.select_by_value(str(ticket_num))
element = driver.find_element(By.CSS_SELECTOR, element3)
element.click()
time.sleep(0.5)
# 隣じゃないエラー
try:
    element = driver.find_elements(By.CLASS_NAME,"remodal-cancel")
    element[0].click()
except:
    print("")
# 次の画面へ遷移
tickets_elements = driver.find_elements(By.CLASS_NAME, "zaseki")
for index, tickets_element in enumerate(tickets_elements):
    # 取得座席表示
    print(tickets_element.text)
element = driver.find_element(By.CLASS_NAME, "definition")
element.click()
element = driver.find_element(By.ID, "pay3+3")
element.click()
element = driver.find_element(By.CLASS_NAME, "footer_next")
element.click()

# 名義入力
# 名前
element = driver.find_element(By.NAME, "namecana1").send_keys(name)
# 電話番号
driver.find_element(By.NAME, "phone").send_keys(tell)
# メールアドレス
driver.find_element(By.NAME, "mailpc").send_keys(address)
driver.find_element(By.NAME, "mailpc_cert").send_keys(address)
# 規約
driver.find_element(By.ID, "kiyaku_").click()
driver.find_element(By.CLASS_NAME, "footer_next").click()
time.sleep(0.5)
driver.find_element(By.CLASS_NAME, "footer_next").click()
time.sleep(0.5)
#最終決定
driver.find_element(By.CLASS_NAME, "remodal-confirm").click()
driver.quit()
