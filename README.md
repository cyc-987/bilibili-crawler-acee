# bilibili-crawler-acee

## 依赖
1. Python 3  
2. requests 库  
   你可以`pip install requests`也可以在仓库根目录`pip -r install requirements.txt`  
## 用法
1. 打开B站获取cookie (可以不登录，所以你可以开隐私窗口打开一个B站网页)，填写到`main.py`里的`cookie`变量里  
2. 打开`main.py`，修改紧跟在`import`后面的几行，包括了关键词、最大页码等信息  
3. 应该就可以运行`main.py`了，输出在`output.csv`里，编码为utf-8 with BOM，正常来说中文的excel能正常显示中文(反正中文的Windows11里的中文Excel没问题)  


## FAQ
1. `data = resp.json().get("data").get("result")`这一行报错一般是因为Cookie过期了，或者这个Cookie抓太多了  
2. `for item in data:`这一行报错一般是因为页码超过了  