import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
import html.parser


def execute_times(times, driver):
    for i in range(times):
        # 滑动到浏览器底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # 等待页面加载
        try:
            # 选中并点击页面底部的加载更多
            driver.find_element_by_css_selector('button.QuestionMainAction').click()
            time.sleep(1)  # 等待页面加载
        except:
            continue


def save_info(driver, name, url):
    txt_path = "D:\\workspace\\Python\\Zhihu_Girls\\" + name + "\\"
    pic_path = "D:\\workspace\\Python\\Zhihu_Girls\\" + name + "\\pic\\"
    if not os.path.exists(txt_path):
        os.mkdir(txt_path)
    else:
        print("the folder has existed!")
        return
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)
    driver.get(url)
    execute_times(10, driver)
    result_raw = driver.page_source
    result_soup = BeautifulSoup(result_raw, "html.parser")
    result_bf = result_soup.prettify()
    with open(txt_path+name+".txt", 'w', encoding="utf8") as savetxt:
        savetxt.write(result_bf)
    savetxt.close()
    print("save raw data successfully!")
    with open(txt_path+"noscript_meta.txt", 'w', encoding="utf8") as savenoscript:
        noscript_nodes = result_soup.find_all("noscript")
        noscript_inner_all = ""
        for noscript in noscript_nodes:
            noscript_inner = noscript.get_text()
            noscript_inner_all += noscript_inner + "\n"
        noscript_all = html.parser.unescape(noscript_inner_all)
        savenoscript.write(noscript_all)
    savenoscript.close()
    print("save noscript meta data successfully!")
    img_soup = BeautifulSoup(noscript_all, "html.parser")
    img_nodes = img_soup.find_all("img")
    with open(txt_path + "pic_url.txt", 'w', encoding="utf8") as savepic:
        cnt = 0
        for img in img_nodes:
            if img.get("src") is not None:
                img_url = img.get("src")
                line = str(cnt) + "\t" + img_url + "\n"
                savepic.write(line)
                urllib.request.urlretrieve(img_url, pic_path + str(cnt) + ".jpg")
                cnt += 1
    savepic.close()
    print("save url and pic successfully!")


def main():
    driver = webdriver.Chrome()
    mydict = dict(你的日常搭配是什么样子="https://www.zhihu.com/question/35931586",
                  女生腿好看胸平是一种什么体验="https://www.zhihu.com/question/61235373",
                  腿长是一种什么体验="https://www.zhihu.com/question/28481779",
                  拍照时怎样摆姿势好看="https://www.zhihu.com/question/19671417",
                  女性胸部过大会有哪些困扰与不便="https://www.zhihu.com/question/20196263",
                  短发女孩要怎么拍照才性感="https://www.zhihu.com/question/46458423",
                  身材好是一种怎样的体验="https://www.zhihu.com/question/26037846")
    for Name, url in mydict.items():
        try:
            save_info(driver, Name, url)
        except:
            print("error")
            continue


if __name__ == "__main__":
    main()
