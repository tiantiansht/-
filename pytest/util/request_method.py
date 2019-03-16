import requests
import json
class requestMethod():
    def get_request(self,url,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,headers=header,verify=False)
        else:
            res = requests.get(url=url,verify=False)
        return res.json()

    def post_request(self,url,body,header=None,cookie=None):
        if header != None:
            res = requests.post(url=url,headers=header,data=body,cookies=cookie,verify=False)
        else:
            res = requests.post(url=url,data=body,cookies=cookie,verify=False)
        return res.json()

    def request_main(self,method,url,body=None,header=None,cookie=None):
        if method == "post":
            res = self.post_request(url,body,header,cookie)
        else:
            res = self.get_request(url,header)
        #return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        return res
