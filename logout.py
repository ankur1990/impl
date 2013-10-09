from mod_python import util,Session

def index(req):
	
	sess = Session.Session(req)
	del sess["regno"]
	sess.save()
	util.redirect (req, "login.html")
