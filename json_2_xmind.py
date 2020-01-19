import xmind
import json
import sys
import os

def dfs(topic_data, topic):
    if isinstance(topic_data,dict):
        for i in topic_data.keys():
            sub_topic = topic.addSubTopic()
            sub_topic.setTitle(i)
            dfs(topic_data[i], sub_topic)
    else:
        if isinstance(topic_data,list):
            data=''
            index = 0
            for i in topic_data:
                if isinstance(i,dict):
                    sub_topic = topic.addSubTopic()
                    sub_topic.setTitle(index)
                    index += 1
                    dfs(i, sub_topic)
                    continue
                data += i
                data += ','
            if(len(data) != 0):
                sub_topic = topic.addSubTopic()
                sub_topic.setTitle(data)
        else:
            sub_topic = topic.addSubTopic()
            sub_topic.setTitle(topic_data)
            return sub_topic


def json_2_xmind(json_file_path, xmind_name):
    workbook = xmind.load(xmind_name)
    sheet1 = workbook.getPrimarySheet()
    sheet1.setTitle(xmind_name)  # 设置画布名称
    root_topic1 = sheet1.getRootTopic()
    root_topic1.setTitle(xmind_name)
    with open(json_file_path) as f:
        dict_data = json.load(f)
        dfs(dict_data, root_topic1)
    xmind.save(workbook, path=xmind_name)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('''
        usage :
            python3 json_2_xmind.py exp.json name.xmind
        ''')
        exit()
    if not os.path.exists(sys.argv[1]):
        print("file", sys.argv[1], "not exist")
        exit()
    json_2_xmind(sys.argv[1], sys.argv[2])
