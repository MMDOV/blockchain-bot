from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchWindowException
import time
import ttkbootstrap as ttk

USERNAME = r'retard.bigdaddy@gmail.com'
PASSWORD = r'Mitsubishizxcvbnm216712'
webdriver_path = r"chromedriver.exe"
extension_path = r"VeePN.crx"
ser = service.Service(executable_path=webdriver_path)
option = Options()
option.add_extension(extension_path)
driver = webdriver.Chrome(service=ser, options=option)
x_path = r'//*[@id="page"]/div/div[1]/div/div/div/div/'


# Main Function
def lets_go():
    try:
        global driver
        driver.get(r"https://blockchaincuties.com/en/dungeon-worlds")
    except NoSuchWindowException:
        driver = webdriver.Chrome(service=ser, options=option)
        driver.get(r"https://blockchaincuties.com/en/dungeon-worlds")
    lvl = number_of_dungeon.get()
    dungeon = var.get()
    window.destroy()
    time.sleep(7)
    cookie = driver.find_element(By.XPATH, r'//*[@id="app"]/div[1]/div/div/div[3]')
    cookie.click()
    login = driver.find_element(By.XPATH, r'//*[@id="app"]/div[5]/div[2]/div[2]/div[1]/div/nav/div[2]/a[1]')
    login.click()
    user_box = driver.find_element(By.XPATH, r'//*[@id="app"]/div[5]/div[4]/div/div[2]/div/div/div[2]/div/div/div['
                                             r'1]/form/div[1]/div/input')
    user_box.send_keys(USERNAME)
    pass_box = driver.find_element(By.XPATH, r'//*[@id="app"]/div[5]/div[4]/div/div[2]/div/div/div[2]/div/div/div['
                                             r'1]/form/div[2]/div[1]/div/input')
    pass_box.send_keys(PASSWORD)
    login_btn = driver.find_element(By.CLASS_NAME, r'wallet-login-btn')
    login_btn.click()
    time.sleep(5)
    dungeon_1 = driver.find_element(By.XPATH, r'//*[@id="page"]/div/div/div/div/div[1]/div/div[2]/a/button')
    dungeon_2 = driver.find_element(By.XPATH, r'//*[@id="page"]/div/div/div/div/div[2]/div/div[2]/a/button')
    try:
        dungeon_1.click()
    except ElementClickInterceptedException:
        driver.find_element(By.CSS_SELECTOR, r'#app > div.news-wrapper > div > div > div.el-dialog__body > div > '
                                             r'div.patchnotes-section > div.news-buttons > button:nth-child('
                                             r'1)').click()
    if int(dungeon) == 1:
        dungeon_1.click()
        time.sleep(5)
        if int(lvl) == 1:
            dungeon_j_1()
        elif int(lvl) == 3:
            dungeon_j_3()
    else:
        dungeon_2.click()


# Dungeons

def dungeon_j_1():
    dungeon_1 = driver.find_element(By.CSS_SELECTOR, r'#world-svg > g:nth-child(4)')
    dungeon_1.click()
    enter_btn = driver.find_element(By.XPATH, r'//*[@id="page"]/div/div/div[3]/div/div[2]/div/div[6]/button')
    enter_btn.click()
    time.sleep(30)
    cat1 = driver.find_element(By.CLASS_NAME, r"dungeon-cutie-wrapper")
    cat1.click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[25]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[35]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[45]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[55]').click()
    time.sleep(15)
    driver.find_element(By.XPATH, f'{x_path}div[55]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[65]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[75]').click()
    time.sleep(15)
    driver.find_element(By.XPATH, f'{x_path}div[75]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[76]').click()
    time.sleep(10)
    driver.find_element(By.XPATH, f'{x_path}div[76]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[77]').click()
    time.sleep(20)
    driver.find_element(By.XPATH, f'{x_path}div[77]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[78]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[79]').click()
    time.sleep(20)
    driver.find_element(By.XPATH, f'{x_path}div[79]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[89]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[99]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[98]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[97]').click()
    time.sleep(20)
    driver.find_element(By.XPATH, f'{x_path}div[97]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[107]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[117]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[127]').click()
    time.sleep(15)
    driver.find_element(By.XPATH, f'{x_path}div[127]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[137]').click()
    time.sleep(15)
    driver.find_element(By.XPATH, f'{x_path}div[137]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[147]').click()
    time.sleep(420)


def dungeon_j_3():
    dungeon_3 = driver.find_element(By.CSS_SELECTOR, r'#world-svg > g:nth-child(6)')
    dungeon_3.click()
    enter_btn = driver.find_element(By.XPATH, r'//*[@id="page"]/div/div/div[3]/div/div[2]/div/div[8]/button')
    enter_btn.click()
    time.sleep(30)
    cat1 = driver.find_element(By.CLASS_NAME, r"dungeon-cutie-wrapper")
    cat1.click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[25]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[24]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[23]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[33]').click()
    time.sleep(15)
    driver.find_element(By.XPATH, f'{x_path}div[33]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[43]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[42]').click()
    time.sleep(40)
    driver.find_element(By.XPATH, f'{x_path}div[42]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[41]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[51]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[61]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[62]').click()
    time.sleep(10)
    driver.find_element(By.XPATH, f'{x_path}div[62]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[72]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[82]').click()
    time.sleep(40)
    driver.find_element(By.XPATH, f'{x_path}div[82]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[92]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[93]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[94]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[95]').click()
    time.sleep(40)
    driver.find_element(By.XPATH, f'{x_path}div[95]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[96]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[97]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[98]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[108]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[109]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[119]').click()
    time.sleep(40)
    driver.find_element(By.XPATH, f'{x_path}div[119]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[129]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[139]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[149]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[159]').click()
    time.sleep(40)
    driver.find_element(By.XPATH, f'{x_path}div[159]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[169]').click()
    time.sleep(10)
    driver.find_element(By.XPATH, f'{x_path}div[169]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[179]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[189]').click()
    time.sleep(40)
    driver.find_element(By.XPATH, f'{x_path}div[189]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[199]').click()
    time.sleep(60)
    driver.find_element(By.XPATH, f'{x_path}div[199]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[198]').click()
    time.sleep(40)
    driver.find_element(By.XPATH, f'{x_path}div[198]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[208]').click()
    time.sleep(10)
    driver.find_element(By.XPATH, f'{x_path}div[208]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[218]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[217]').click()
    time.sleep(60)
    driver.find_element(By.XPATH, f'{x_path}div[217]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, f'{x_path}div[227]').click()
    time.sleep(420)


# ----------------------------------------------UI------------------------------------------------ #
window = ttk.Window()
window.title("Bot Vahid")
window.config(pady=20, padx=20)
var = ttk.IntVar()
radio1 = ttk.Radiobutton(window, text="Dungeons of Jotunheim", variable=var, value=1)
radio2 = ttk.Radiobutton(window, text="Infernum World", variable=var, value=2)
radio1.grid(row=0, column=0)
radio2.grid(row=0, column=1)
num_dun = ttk.Label(text="Dungeon Number : ", padding=10)
num_dun.grid(row=1, column=0)
number_of_dungeon = ttk.Entry(width=20)
number_of_dungeon.insert(0, '3')
number_of_dungeon.grid(row=1, column=1)
button = ttk.Button(text="Lets Go!", width=20, bootstyle='dark', command=lets_go)
button.config(padding=10)
button.grid(row=2, column=0, columnspan=2)
window.mainloop()
