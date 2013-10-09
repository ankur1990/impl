from ZEO.ClientStorage import ClientStorage
from ZODB.DB import DB
import transaction
from engine import *


def getSystem():
	addr = 'localhost', 9001
	storage = ClientStorage(addr)
	db = DB(storage)
	connection = db.open()
	root = connection.root()
	if root.has_key("system"):
		return root["system"]
	else:
		return System()
	db.close()

def setSystem(system):
	addr = 'localhost', 9001
	storage = ClientStorage(addr)
	db = DB(storage)
	connection = db.open()
	root = connection.root()
	root["system"] = system
	transaction.commit()
	db.close()
