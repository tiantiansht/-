import os
import sys
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_path)
from data import excel_column_data
from util.operating_excel import operatingExcel
from util.operating_json_file import operatingJson
from util.connect_db import connectDb
class getData():
    def __init__(self):
        self.operating = operatingExcel()
        self.operating_json = operatingJson()
        self.connect_db = connectDb()

    def get_case_lines(self):
        return self.operating.get_lins()

    def get_case_ID(self,row):
        '''获取用例ID'''
        col = int(excel_column_data.get_id())
        caseID = self.operating.get_value(row,col)
        return caseID

    def get_case_is_run(self,row):
        '''获取是否运行'''
        col = int(excel_column_data.get_is_run())
        Flag = None
        run_value = self.operating.get_value(row,col)
        if run_value == "yes":
            Flag = True
        else:
            Flag = False
        return Flag

    def get_url(self,row):
        '''获取url'''
        col = int(excel_column_data.get_url())
        request_url = self.operating.get_value(row,col)
        return request_url

    def get_request_type(self,row):
        '''获取请求方式'''
        col = int(excel_column_data.get_request_type())
        request_type = self.operating.get_value(row,col)
        return request_type

    def get_is_cookie(self,row):
        '''获取是否需要cookie'''
        col = int(excel_column_data.get_request_data_type())
        request_cookie = self.operating.get_value(row,col)
        return request_cookie

    def get_header(self,row):
        '''获取header信息'''
        col = int(excel_column_data.get_header())
        request_header = self.operating.get_value(row,col)
        if request_header == "":
            return None
        else:
            request_json_header = self.operating_json.get_header(request_header)
            return request_json_header


    def get_case_depend(self,row):
        '''获取case是否存在依赖'''
        col = int(excel_column_data.get_case_depend())
        request_case_depend = self.operating.get_value(row,col)
        if request_case_depend == "":
            return None
        else:
            return request_case_depend

    def get_data_depend(self,row):
        '''获取依赖的返回数据'''
        col = int(excel_column_data.get_data_depend())
        request_data_depend = self.operating.get_value(row,col)
        if request_data_depend == "":
            return None
        else:
            return request_data_depend

    def get_field_depend(self,row):
        '''获取数据依赖字段'''
        col = int(excel_column_data.get_field_depend())
        request_field_depend = self.operating.get_value(row,col)
        if request_field_depend == "":
            return None
        else:
            return request_field_depend

    def get_data(self,row):
        '''获取body信息'''
        col = int(excel_column_data.get_data())
        request_data = self.operating.get_value(row,col)
        if request_data != "":
            return request_data
        else:
            return None

    def get_json_data(self,row):
        '''根据关键字获取json文件中body相关信息'''
        data = self.get_data(row)
        if data != None:
            request_json_header = self.operating_json.get_data(data)
        else:
            request_json_header = None
        return request_json_header

    def get_expect(self,row):
        '''获取预期结果'''
        col = int(excel_column_data.get_expect())
        request_expect = self.operating.get_value(row,col)
        return request_expect

    def write_result(self,row,value):
        '''写入实际结果'''
        col = int(excel_column_data.get_result())
        self.operating.write_data(row,col,value)

    def get_sql(self,row):
        '''通过sql获取预期结果'''
        col = int(excel_column_data.get_expect())
        sql = self.operating.get_value(row, col)
        result = self.connect_db.search_one(sql)
        return result






