import requests


# headers，包括了UA和Cookie
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41",
    "Cookie": "buvid3=456845EF-E2DC-E75A-35C3-FE69F0BE7BFC10922infoc; b_nut=1672140010; _uuid=B159A93D-B667-67C1-49C7-99659134B72C12043infoc; buvid4=B2A40E96-162B-2CEB-42BA-01AB6ABADCB012661-022122719-mQ3ahp215nlp41kZvUuzCA%3D%3D; buvid_fp_plain=undefined; SESSDATA=0e123f1b%2C1687692218%2Cafc50%2Ac2; bili_jct=ca97d687f4bc7f72e89f8bc2152a1689; DedeUserID=442684513; DedeUserID__ckMd5=cee8be4fc3323d8e; sid=5auof2ki; CURRENT_FNVAL=4048; rpdid=|(J|)|lYukJR0J'uY~kuR|Jkl; i-wanna-go-back=-1; b_ut=5; nostalgia_conf=-1; fingerprint=803313416b7f5e22db4ee7eb805b00e6; buvid_fp=4f72c9d867a9103dae4f20f0188bf1d2; CURRENT_QUALITY=116; LIVE_BUVID=AUTO6416749602193257; hit-new-style-dyn=0; hit-dyn-v2=1; header_theme_version=CLOSE; home_feed_column=5; innersign=1; bp_video_offset_442684513=774413110852190300; b_lsid=681078F7B_186F54A994F; PVID=4"
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