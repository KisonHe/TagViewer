
def extractTagFromString(string: str, ifIgnoreExclamationMark: bool) -> list:
    ret = []
    if isinstance(string, str):
        # 去掉空格
        string = string.replace(" ", "")
        ret = string.split("#")
        # 处理!开头的Tag
        for index in range(len(ret)):
            if (ret[index].startswith("!")):
                if (ifIgnoreExclamationMark):
                    # 忽略!，把整个string变成"",在下面删掉
                    ret[index] = ""
                else:
                    ret[index] = ret[index].replace("!", "")
        # 去掉 ''
        ret = list(filter(None, ret))
    else:
        return []
    return ret
