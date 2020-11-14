
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request
import tkinter as tk
from functools import partial
from selenium.webdriver.chrome.options import Options

def manga_downloader(win, e1, e2):
#first page
    url_in = e1.get()
    des_in = e2.get()
    win.destroy()
    url = url_in
    des = des_in.replace("\\", "/")
    des = des + "/"

    chrome_path ='/Users/tong2/Documents/workspace/web_scrape/chromedriver.exe'
   
    driver = webdriver.Chrome(chrome_path)
    driver.get(url)
    pic_box = driver.find_element(By.XPATH, "//*[@id=\"img\"]")
    pic_url = pic_box.get_attribute("src")
    urllib.request.urlretrieve(pic_url, des + '1.jpg')

    next_page_url = driver.find_element(By.XPATH, "//*[@id=\"next\"]").get_attribute("href")

    temp_url = ""
    pic_num = 2
    driver.close()
    while next_page_url != temp_url:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        
        
        driver_new = webdriver.Chrome(chrome_options=chrome_options, executable_path = chrome_path)
        driver_new.set_window_position(-10000,0)
        pic_num_str = str(pic_num)
        pic_name = pic_num_str + ".jpg"
        
        driver_new.get(next_page_url)

        pic_box_2 = driver_new.find_element(By.XPATH, "//*[@id=\"img\"]")
        pic_url_2 = pic_box_2.get_attribute("src")
        
        urllib.request.urlretrieve(pic_url_2, des + pic_name)
        
        temp_url = next_page_url
        next_page_url = next_page_url = driver_new.find_element(By.XPATH, "//*[@id=\"next\"]").get_attribute("href")

        pic_num = pic_num + 1
        driver_new.close()

    root = tk.Tk()
    root.geometry("200x200")
    root.title("下载完毕")
    label = tk.Label(root, text="漫画下载完毕！")
    label.pack()
    root.mainloop()


master = tk.Tk()
master.geometry("400x100")
master.title("E-hentai Manga Downloader Made by YT")
tk.Label(master, text="url of first page:").grid(row=0)
tk.Label(master, text="destination file: ").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row = 0, column = 1, padx = 75, ipady=1.5, columnspan = 2 )
e2.grid(row = 1, column = 1, padx = 75, ipady=1.5, columnspan = 2 )

button = tk.Button(master, text = "Download")
button.grid(row = 2)

s1 = e1.get()
s2 = e2.get()

button = tk.Button(master, text = "Download", command = partial(manga_downloader, master, e1, e2))
button.grid(row = 2)
print(s1)
print(s2)
master.mainloop()