import pymongo
import json
import os
import requests
from Classes.Tools import Tools

Decode = Tools.decode
Initer = Tools.initer


dirpath = os.getcwd()

with open(os.path.join(dirpath, "Database/DatabaseConfigs.json")) as f:
    configs = json.load(f)

get_database_url = json.loads(
    requests.get("{0}/Services/config/get/UserManagement".format(configs['MicroServiceManagementURl']),
                 verify=False).content)


if not get_database_url["State"]:
    exit(1)

get_database_url = json.loads(get_database_url["Description"])

url= ''
if get_database_url["Key"] == None:
    url = Decode(get_database_url["DatabaseString"])
else:
    Initer(get_database_url["Key"])
    url = Decode(get_database_url["DatabaseString"])




mongodb = pymongo.MongoClient(url)
database = mongodb[configs["DatabaseName"]]
UserDb = database[configs["UserCollection"]]
ServiceIno = database[configs["Service"]]
