import pickle
from engine import *


class tUnpickler(pickle.Unpickler):
	def find_class(self, module, name):
		return eval(name)

def tUnpicklerLoad(file):
		return tUnpickler(file).load()

def getSystem():
	try:
		file = open("/test/system.dat", "rb")
		system = tUnpicklerLoad(file)
		file.close()
	except:
		system = System()
	return system

def setSystem(system):
	file = open("/test/system.dat","wb")
	pickle.dump(system, file)
	file.close()	
