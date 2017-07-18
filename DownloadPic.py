import requests
import os

def DownloadPic(url,root):
    try:
        path = root+"web_designer.jpg"
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path,'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")

if __name__ == "__main__":
    url = "https://pic1.zhimg.com/v2-4dd17d02424897a9b73c426b10fe14d8_r.jpg"
    root = "D://workspace//Python//reptile//pic//"
    DownloadPic(url,root)
