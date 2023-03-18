import tools.request as request


request.setKeyword("hahahi")  # 设置关键词
n = 5  # 最大的查询页码
judge = "点赞数"  # 筛选依据，请从下面的field字典里的键里选
threshold = 500000  # 被筛选字段的下限值


# 字段字典，格式为 名称:api返回值对应的键
field = {
    "标题": "title",
    "描述": "description",
    "评论数": "review",
    "播放数": "play",
    "收藏数": "favorites",
    "点赞数": "like",
    "链接": "arcurl"
}

# 第一行写入字段
outp = open("output.csv", "w", encoding="utf-8-sig")
for i in field:
    outp.write("\"{}\"".format(str(i))+",")
outp.write("\n")


for i in range(1, n+1):
    data = request.getData(i)
    result = {}
    # 便利每页个条目
    for item in data:
        # 获取每一个字段的值
        for j in field:
            result[j] = str(item.get(field[j])).replace("\r", "").replace("\n", "\\n")
        # 若符合条件则写入
        if int(result[judge]) > threshold:
            for j in result.values():
                outp.write("\"{}\"".format(j)+",")
            outp.write("\n")
outp.close()