import requests
import os

def DownloadPic(url,root):
    try:
        path = root+url.split('/')[-1]
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
    url = "https://pic1.zhimg.com/web_designer.jpg"
    root = "D://workspace//Python//reptile//pic//"
    DownloadPic(url,root)
