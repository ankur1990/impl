from mod_python import util, Session

def index(req):
	
	util.redirect(req,"/pantoto-research/users.py")

