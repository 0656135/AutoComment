from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class shotgroup:
    def __init__(self, web, acc, pwd  ):
        self.web = web
        self.acc = acc
        self.pwd = pwd
        self.url_list = []
        chrome_path = "./chromedriver"

        self.driver = webdriver.Chrome(chrome_path )
        self.driver.maximize_window()

    def login(self):
        self.driver.find_element_by_css_selector( 'input#username' ).send_keys( self.acc )
        self.driver.find_element_by_css_selector( 'input#password').send_keys( self.pwd )
        self.driver.find_element_by_css_selector('input.button2').click()

    def destinationWeb(self):
        page_list = []
        page_number = input( '請輸入要讀取的頁數: ')

        # 把要訪問的頁面紀錄起來
        for i in range( int( page_number) ):
            page_list.append('https://www.shotgroup.net/home/viewforum.php?f=10&start=' + str(i * 20))

        for i in page_list:
            self.driver.get(i)  # 到該頁面
            url = self.driver.find_elements_by_css_selector('a.topictitle')  # 抓所有笑話的網址
            for j in url[2::2]:
                self.url_list.append(j.get_attribute('href'))  # 所有目標網址

        #目標網址除存起來
        f = open( 'url.txt', 'w' )
        for i in self.url_list:
            f.write(  i + '\n' )


    def readurl(self):
        f = open( 'url.txt', 'r' )
        while True:
            i = f.readline( )
            if i == '' : break
            else : self.url_list.append( i )


    def comment(self):
        message = [ '哈哈哈', '很好笑喔', '謝謝版主']
        for i in self.url_list:
            self.driver.get( i )
            r = random.randint(0,2)
            s =  message[r]
            self.driver.find_element_by_css_selector( 'textarea.inputbox').send_keys( s )
            self.driver.find_element_by_css_selector('input.button1').click()
            time.sleep(15)


    def cmd(self):
        print( '*************************************************' + '\n' )
        print( '*         1.讀取目標網址並開始自動留言               *'  + '\n')
        print( '*         2.重新讀取目標網址並開始自動留言            *' + '\n')
        print( '**************************************************' + '\n' )
        c = input( '請輸入: ')

        self.driver.get( 'https://www.shotgroup.net/home/' )

        #  # for id   . for class
        self.driver.find_element_by_css_selector( 'button.confirm').click()
        self.driver.find_element_by_css_selector('button.confirm').click()

        self.login()
        self.driver.find_elements_by_css_selector( 'a.grid_colour_overlay')[5].click()
        #self.driver.find_element_by_css_selector('button.confirm').click()
        #self.driver.find_element_by_css_selector('button.confirm').click()

        if c == '1':
            self.readurl()
            self.comment()
        if c == '2':
            self.destinationWeb()


def main():
    web = 'https://www.shotgroup.net/home/'
    acc = 'Dickson769'
    pwd = 'shotgroup'
    user = shotgroup( web, acc, pwd )
    user.cmd()


if __name__ == "__main__":
    main()