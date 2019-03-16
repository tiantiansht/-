import logging
class Logging():
    def test_logging(self,caseID,data):
        logger = logging.getLogger('test_log')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("G:/pycharm/PycharmProjects/pytest/dataconfig/test.log","a",encoding="utf-8")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.error("用例:%s,错误信息:%s"%(caseID,data))
        logger.removeHandler(fh)




