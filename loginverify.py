from mod_python import util,Session

def index(req, username, password):

        if not (username=="admin" and password==""):
                util.redirect (req, "index.html")

        sess = Session.Session(req)
        sess["login"] = 1
        sess.save()
        util.redirect (req, "home.py")

