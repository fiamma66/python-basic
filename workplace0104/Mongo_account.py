from pymongo import MongoClient

class MongoBase:
    def __init__(self,collection):
        self.collection=collection
        self.OpenDB()
    def OpenDB(self):
        user='root'
        passwd='root'
        # on local host
        host='192.168.114.130'
        port='27017'
        auth_db='admin'
        uri = "mongodb://"+user+":"+passwd+"@"+host+":"+port+"/"+auth_db+"?authMechanism=SCRAM-SHA-1"
        self.con = MongoClient(uri, connect=False)
        self.db=self.con['wangdong']
        self.collection=self.db[self.collection]
    def closeDB(self):
        self.con.close()