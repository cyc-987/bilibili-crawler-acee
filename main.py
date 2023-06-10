cookie = "buvid3=7EFA37D0-F1FE-F4B2-67A7-4D5CC068ADB914443infoc; b_nut=1685935714; i-wanna-go-back=-1; _uuid=E89A53FC-24A5-27C6-78C1-C54B72B7210EB14503infoc; FEED_LIVE_VERSION=V8; buvid4=AAE58FD6-2446-1F09-6FDD-67B651BF5CD015811-023060511-9TO%2BhWhxQHNJ3e7kUXAEKSOuaP1Mma70%2FihuVRGs%2FX%2BtB6fXRkR%2B%2Fw%3D%3D; SESSDATA=c80ec98f%2C1701487755%2Ca841e%2A62; bili_jct=b715433af3ed96db45c1dff797a5153d; DedeUserID=442684513; DedeUserID__ckMd5=cee8be4fc3323d8e; CURRENT_FNVAL=4048; rpdid=0zbfAHJqia|bBS0o424|12R|3w1Q60UM; fingerprint=b32f37bd83655f0c199a35a8be87bd96; buvid_fp_plain=undefined; b_ut=5; header_theme_version=CLOSE; nostalgia_conf=-1; hit-new-style-dyn=1; hit-dyn-v2=1; LIVE_BUVID=AUTO6716861403882313; CURRENT_QUALITY=120; PVID=1; buvid_fp=733b5fc5c6eec385e826338a02b1a5e0; bp_video_offset_442684513=805386254393802900; innersign=0; b_lsid=A6934EFA_188A317535C; home_feed_column=4; browser_resolution=1121-916"
n = 5  # 最大的查询页码
judge = "点赞数"  # 筛选依据，请从下面的field字典里的键里选
threshold = 50000  # 被筛选字段的下限值

if __name__ == "__main__":
    import tools.request as request

    request.setKeyword("chatgpt")  # 设置关键词
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
        if data:
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