import xlrd
from xlutils import copy
class operatingExcel():
    '''对表格操作'''
    def __init__(self):
        self.file_path = "G:/pycharm/PycharmProjects/pytest/case/case.xls"
        self.data = self.get_sheet()

    def get_sheet(self):
        '''打开表格，获取表1信息'''
        data = xlrd.open_workbook(self.file_path)
        table = data.sheet_by_index(0)
        return table

    def get_lins(self):
        '''获取总行数'''
        lins = self.data
        return lins.nrows

    def get_value(self,row,col):
        '''获取单元格内容'''
        return self.get_sheet().cell_value(row, col)

    def write_data(self,row,col,value):
        '''写入数据'''
        data = xlrd.open_workbook(self.file_path)
        copy_data = copy.copy(data)
        sheet_data = copy_data.get_sheet(0)
        sheet_data.write(row,col,value)
        copy_data.save(self.file_path)

    def get_row_valuses(self,row):
        '''根据行号，获取该行信息'''
        table = self.data
        row_data = table.row_values(row)
        return row_data

    def get_col_values(self,col_id=None):
        '''获取某列内容'''
        if col_id == None:
            col_data = self.data.col_values(0)
        else:
            col_data = self.data.col_values(col_id)
        return col_data

    def get_row_num(self,case_id):
        '''根据caseid找到对应的行号'''
        num = 0
        cols_data  = self.get_col_values()
        for col_data in cols_data:
            if case_id in col_data:
                return num
            num = num+1

    def get_row_data(self,case_id):
        '''根据caseid获取该行内容'''
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_valuses(row_num)
        return row_data
















