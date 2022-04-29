import os
path = 'C:\\Users\\OS\\Desktop\\我的文件\\第七批NAC\\刘蓉3级\\刘蓉术前.20210508.104856'
# path为json文件存放的路径
json_file = os.listdir(path)
# 博主labelme所在的环境名就叫labelme，读者应修改成activate [自己labelme所在的环境名]
for file in json_file:
##    print(os.path.splitext(file))
    if os.path.splitext(file)[-1] == '.json':
        print(file)
        os.system("activate labelme && labelme_json_to_dataset.exe %s"%(os.path.join(path , file)))
