from selenium import webdriver
import time
import random,os
import tkinter as tk
from tkinter import messagebox, StringVar
from PIL import Image, ImageTk

class shotgroup:
    def __init__(self, web, acc, pwd, version):
        self.web = web
        self.acc = acc
        self.pwd = pwd
        self.url_list = []
        self.joke = []
        self.chrome_path = "./" + str(version)
        self.driver = None

    def login(self):
        self.driver.find_element_by_css_selector('input#username').send_keys(self.acc)
        self.driver.find_element_by_css_selector('input#password').send_keys(self.pwd)
        self.driver.find_element_by_css_selector('input.button2').click()

    def downloadWeb(self, n):
        page_list = []

        # 把要訪問的頁面紀錄起來
        for i in range(int(n)):
            page_list.append('https://www.shotgroup.net/home/viewforum.php?f=10&start=' + str(i * 20))

        for i in page_list:
            self.driver.get(i)  # 到該頁面
            url = self.driver.find_elements_by_css_selector('a.topictitle')  # 抓所有笑話的網址
            for j in url[2::2]:
                self.url_list.append(j.get_attribute('href'))  # 所有目標網址

        # 目標網址除存起來
        f = open('url.txt', 'w')
        for i in self.url_list:
            f.write(i + '\n')

    def downloadJoke(self):
        self.driver = webdriver.Chrome(self.chrome_path)
        self.driver.maximize_window()
        self.driver.get(
            'http://blog.xuite.net/brgj/hh/55259156-%E7%B6%93%E5%85%B8%E9%BB%83%E8%89%B2%E7%AC%91%E8%A9%B146%E5%80%8B+%28%E5%8D%83%E8%90%AC%E5%88%A5%E7%9C%8B%E6%9C%80%E5%BE%8C%E4%B8%80%E5%80%8B%29')
        jokes = self.driver.find_elements_by_css_selector('p')
        f = open('joke.txt', 'w')

        for i in jokes[9:-2]:
            if i.text != ' ':
                s = i.text
                f.write(s + '\n')

    def postJoke(self, n):
        f = open('joke.txt', 'r', encoding='utf8')
        stop = '2'
        ans = ''
        while True:
            s = f.readline()
            if s == '':
                self.joke.append(ans)
                break
            if stop in s:
                self.joke.append(ans)
                ans = s
                stop = str(int(stop) + 1)
            else:
                ans = ans + '\n' + s

        message = ['哈哈哈', '很好笑', '快來看看', '不能錯過', '推一個笑話', '進來看看吧', '一定要看的笑話拉～～～～']
        for i in range(int(n)):
            self.driver.get('https://www.shotgroup.net/home/posting.php?mode=post&f=10')
            article = random.randint(0, len(self.joke) - 1)
            self.driver.find_element_by_css_selector('input#subject').send_keys(message[article % 7])
            self.driver.find_element_by_css_selector('textarea#message').send_keys(self.joke[article])
            self.driver.find_element_by_css_selector('input.default-submit-action').click()
            time.sleep(15)

    def postComment(self):
        f = open('url.txt', 'r')
        while True:
            i = f.readline()
            if i == '':
                break
            else:
                self.url_list.append(i)

        message = ['哈哈哈', '很好笑喔', '謝謝版主', 'QQ', '推一個', '這不好笑阿', '這是網路找的吧']
        for i in self.url_list:
            self.driver.get(i)
            r = random.randint(0, len(message) - 1)
            s = message[r]
            self.driver.find_element_by_css_selector('textarea.inputbox').send_keys(s)
            self.driver.find_element_by_css_selector('input.button1').click()
            time.sleep(15)

    def start(self):
        self.driver = webdriver.Chrome(self.chrome_path)
        self.driver.maximize_window()
        self.driver.get('https://www.shotgroup.net/home/')

        #  # for id   . for class
        self.driver.find_element_by_css_selector('button.confirm').click()
        self.driver.find_element_by_css_selector('button.confirm').click()

        self.login()
        self.driver.find_elements_by_css_selector('a.grid_colour_overlay')[5].click()

    def action(self, c, n=None):

        if c == '1':
            self.start()
            self.postComment()
        if c == '2':
            self.start()
            self.postJoke(n)
        if c == '3':
            self.start()
            self.downloadWeb(n)
        if c == '4':
            self.downloadJoke()

    def cmd(self):
        print('*************************************************' + '\n')
        print('*         1.自動回覆留言                          *' + '\n')
        print('*         2.自動發文                              *' + '\n')
        print('*         3.重新下載目標網址                       *' + '\n')
        print('*         4.重新下載笑話（不要使用）                *' + '\n')
        print('**************************************************' + '\n')

        c = input('請輸入: ')
        if c == '1':
            self.start()
            self.postComment()
        if c == '2':
            n = input('要發幾篇？ ')
            self.start()
            self.postJoke(n)
        if c == '3':
            n = input('下載幾頁的資料？')
            self.start()
            self.downloadWeb(n)
        if c == '4':
            self.downloadJoke()

        self.driver.close()


class Gui():
    def __init__(self):
        chose = ['自動回覆留言', '自動發文', '重新下載目標網址', '重新下載笑話（不要使用）']
        self.win = tk.Tk()
        self.win.title('社團讚讚')
        self.lableAcc = tk.Label(self.win, text='帳號')
        self.textAcc = tk.Entry(self.win, text='ww')
        self.lablePwd = tk.Label(self.win, text='密碼')
        self.textPwd = tk.Entry(self.win, show='*')
        self.ButtonW = tk.Button(self.win, text='Window', command=lambda: self.click('windows.exe'))
        self.ButtonL = tk.Button(self.win, text='Linux', command=lambda: self.click('linux'))
        self.ButtonM = tk.Button(self.win, text='Mac', command=lambda: self.click('mac'))
        self.v1 = StringVar(value='選擇功能')
        self.select = tk.OptionMenu(self.win, self.v1, command=self.Select, *chose )
        self.textSelect = tk.Entry(self.win)
        self.labelSelect = tk.Label(self.win, text='要發幾篇?')
        render = ImageTk.PhotoImage(Image.open(resource_path('./img/'+str(random.randint(0,4))+'.jpg')))
        self.photo = tk.Label(self.win, image=render)
        self.photo.image = render
        self.photo.grid(row=0, column=3,rowspan=5)
        self.lableAcc.grid(row=0, column=0)
        self.textAcc.grid(row=0, column=1)
        self.lablePwd.grid(row=1, column=0)
        self.textPwd.grid(row=1, column=1)
        self.ButtonL.grid(row=4, column=0)
        self.ButtonM.grid(row=4, column=1)
        self.ButtonW.grid(row=4, column=2)
        self.select.grid(row=2, column=0,columnspan='2')
        self.user = None
    def Select(self, select):
        if select == '自動發文':
            self.textSelect.grid_remove()
            self.labelSelect.grid_remove()
            self.labelSelect = tk.Label(self.win, text='要發幾篇?')
            self.textSelect = tk.Entry(self.win)
            self.labelSelect.grid(row=3, column=0)
            self.textSelect.grid(row=3, column=1)
        elif select == '自動回覆留言' or select == '重新下載笑話（不要使用）':
            self.textSelect.grid_remove()
            self.labelSelect.grid_remove()
        else:
            self.textSelect.grid_remove()
            self.labelSelect.grid_remove()
            self.labelSelect = tk.Label(self.win, text='下載幾頁的資料？')
            self.textSelect = tk.Entry(self.win)
            self.labelSelect.grid(row=3, column=0)
            self.textSelect.grid(row=3, column=1)

    def click(self, os):
        try:
            if self.textAcc.get() == '':
                messagebox.showinfo('帳密不得為空', '請輸入帳號')
            elif self.textPwd.get() == '':
                messagebox.showinfo('帳密不得為空', '請輸0入密碼')
            elif self.v1.get() == '選擇功能':
                messagebox.showinfo('你智障?', '請選擇功能')
            else:
                self.user = shotgroup('https://www.shotgroup.net/home/', self.textAcc.get(), self.textPwd.get(), os)
                if self.v1.get() == '自動回覆留言':
                    self.user.action('1')
                elif self.v1.get() == '自動發文':
                    self.user.action('2', int(self.textSelect.get()))
                elif self.v1.get() == '重新下載目標網址':
                    self.user.action('3', int(self.textSelect.get()))
                elif self.v1.get() == '重新下載笑話（不要使用）':
                    self.user.action('4')

        except ValueError:
            messagebox.showinfo('ValueError', '請輸入"數字"')

    def start(self):
        self.win.mainloop()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def runGui():
    gui = Gui()
    gui.start()


if __name__ == "__main__":
    runGui()
    '''
    random.seed( )
    print( '請輸入你的作業系統：' + '\n' + '（1）Linux' + '\n' + '（2）Windows' + '\n' + '（3）Mac' )
    v = input( '請輸入: ')
    version = ''
    if v == '1':
        version = 'linux'
    elif v == '2':
        version = 'windows.exe'
    else:
        version = 'mac'

    web = 'https://www.shotgroup.net/home/'
    acc = input('請輸入帳號: ')
    pwd = input('請輸入密碼: ')
    user = shotgroup(web, acc, pwd, version )
    user.cmd()
    '''
