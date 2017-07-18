import requests

def SearchByBaidu(keyword):
    try:
        kv = {'wd':keyword}
        r = requests.get("http://www.baidu.com/s",params = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

if __name__ == "__main__":
    print(SearchByBaidu("南京信息工程大学"))
