import os
import sys
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(file_path)
from util.log import Logging
from data.get_data import getData
from util.request_method import requestMethod
from util.result_verification import result_test
from util.send_email import sendMeail
from data.dependent_data import dependentData
from util.operating_header import operatingHeader
class running_case():
    def __init__(self):
        self.Logging = Logging()
        self.get_data = getData()
        self.operating_header = operatingHeader()
        self.requestMethod = requestMethod()
        self.resultTest = result_test()
        self.senMeail = sendMeail()

    def run(self):
        pass_count = []
        fail_count = []
        count = self.get_data.get_case_lines()
        for i in range(1,count):
            case_is_run = self.get_data.get_case_is_run(i)
            if case_is_run:
                caseID = self.get_data.get_case_ID(i)
                case_request_type = self.get_data.get_request_type(i)
                url = self.get_data.get_url(i)
                is_cookie = self.get_data.get_is_cookie(i)
                header = self.get_data.get_header(i)
                body = self.get_data.get_json_data(i)
                expect = self.get_data.get_expect(i)
                is_depend = self.get_data.get_case_depend(i)
                if is_depend != None:
                    self.depend = dependentData(is_depend)
                    run_key = self.depend.get_data_for_key(i)
                    field_depend = self.get_data.get_field_depend(i)
                    body[field_depend] = run_key
                    request = self.requestMethod.request_main(case_request_type,url,body,header)
                else:
                    if is_cookie == "write":
                        request = self.requestMethod.request_main(case_request_type, url, body, header)
                        self.operating_header.write_cookie(request)
                    elif is_cookie == "yes":
                        cookie = self.operating_header.read_cookie()
                        request = self.requestMethod.request_main(case_request_type, url, body, header,cookie)
                    else:
                        request = self.requestMethod.request_main(case_request_type, url, body, header)
                result = self.resultTest.rlt_test(expect, request)
                if result:
                    result_value = "pass"
                    pass_count.append(i)
                else:
                    result_value = "fail"
                    fail_count.append(i)
                    self.Logging.test_logging(caseID,request)
                self.get_data.write_result(i,result_value)
        self.senMeail.send_main(pass_count,fail_count)


run = running_case()
run.run()


