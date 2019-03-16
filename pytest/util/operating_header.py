from util.operating_json_file import operatingJson
class operatingHeader():
    def __init__(self):
        self.operating_json = operatingJson()

    def get_cookie(self,data):
        cookie = data.cookies.get_dict()
        return cookie

    def read_cookie(self):
        file = "G:/pycharm/PycharmProjects/pytest/dataconfig/cookie.json"
        cookie = self.operating_json.read_json(file)
        return cookie

    def write_cookie(self,data):
        cookie = self.get_cookie(data)
        self.operating_json.write_json(cookie)
