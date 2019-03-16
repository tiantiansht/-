import json
import operator
class result_test():
    def rlt_test(self,expext,result):
        flag = None
        if expext in result:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self,dict_one,dict_two):
        '''判断两个字典是否相等'''
        if isinstance(dict_one,str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two,str):
            dict_two = json.loads(dict_two)
        return operator.eq(dict_one,dict_two)


