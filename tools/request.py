import requests
from main import cookie


# headers，包括了UA和Cookie
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41",
    "Cookie": cookie
}
# 抓包得到的api
api = "https://api.bilibili.com/x/web-interface/wbi/search/type"


# 抓包得到要发送的参数
params = {
    "__refresh__": "true",
    "_extra": "",
    "context": "",
    "page": "1",  # 页码
    "page_size": "42",  # 每页显示的条数
    "order": "click",  # 排序方式，这里是按点击数排序
    "from_source": "",
    "from_spmid": "333.337",
    "platform": "pc",
    "highlight": "1",
    "single_column": "0",
    "keyword": "ikun", # 关键词
    "qv_id": "l27zxYC5vnANLUnB4FzeQb7oRIKvgQI6",
    "ad_resource": "5654",
    "source_tag": "3",
    "gaia_vtoken": "",
    "category_id": "",
    "search_type": "video",
    "dynamic_offset": "30",
    "w_rid": "6f076052a7958e88f41ff28927276123",
    "wts": "1679142625",
}


# 设置关键词
def setKeyword(keyword):
    params["keyword"] = keyword


# 获取指定页码的所有条目
def getData(page):
    params["page"] = page  # 修改params里的页码
    resp = requests.get(api, params=params, headers=headers)
    data = resp.json().get("data").get("result")
    return data