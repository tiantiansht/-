import json
class operatingJson():
    def read_json(self,file):
        '''读取json文件'''
        with open(file,"r+") as f:
            data = json.load(f)
            return data

    def get_data(self,id):
        '''根据关键字获取body数据'''
        file = "G:/pycharm/PycharmProjects/pytest/dataconfig/body.json"
        return self.read_json(file)[id]

    def get_header(self,id):
        '''根据关键字获取header数据'''
        file = "G:/pycharm/PycharmProjects/pytest/dataconfig/header.json"
        return self.read_json(file)[id]

    def write_json(self,data):
        '''写入json文件'''
        file = "G:/pycharm/PycharmProjects/pytest/dataconfig/cookie.json"
        with open(file,"w") as f:
            f.write(json.dumps(data))






