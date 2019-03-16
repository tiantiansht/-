import json
from util.operating_excel import operatingExcel
from util.request_method import requestMethod
from  data.get_data import getData
from jsonpath_rw import jsonpath,parser
class dependentData():
    def __init__(self,case_id):
        self.case_id = case_id
        self.operating_excel = operatingExcel()
        self.requestMethod = requestMethod()
        self.getData = getData()

    def row_data(self):
        '''通过case_id去获取该case_id的整行数据'''
        rows_data = self.operating_excel.get_row_data(self.case_id)
        return rows_data

    def run_dependent_case(self):
        '''执行依赖case'''
        row_num = self.operating_excel.get_row_num(self.case_id)
        url = self.getData.get_url(row_num)
        request_type = self.getData.get_request_type(row_num)
        header = self.getData.get_header(row_num)
        body = self.getData.get_json_data(row_num)
        res = self.requestMethod.request_main(request_type,url,body,header)
        return json.loads(res)

    def get_data_for_key(self,row):
        '''根据依赖key获取执行case的响应数据'''
        depend_key = self.getData.get_data_depend(row)
        run_depend_data = self.run_dependent_case()
        json_data = parser(depend_key)
        madle = json_data.find(run_depend_data)
        return [math.value for math in madle][0]