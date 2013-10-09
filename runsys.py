from mod_python import util, Session
from engine import *
from dbase import *

def exe(req, **params):
    
    sess = Session.Session(req)
    if not sess.has_key("user"):
        util.redirect (req, "/pantoto-research/login.py")
    user = sess["user"]

    system = getSystem()
    pagelet=params["pagelet"]
    action=params["action"]
    for i in params:
        if i[0]=='1':
            fieldlabel=i[1:]
            value=params[i]
            system.setFieldByUser(user,pagelet,fieldlabel,value)
    

    system.executeAction(user,action)

    setSystem(system)
    util.redirect(req,"/pantoto-research/runsys.py?pagelet="+pagelet)



def loginverify(req, username):

    sess = Session.Session(req)
    sess["user"] = username
    sess.save()
    util.redirect(req,"/pantoto-research/runsys.py")

def logout(req):
    sess = Session.Session(req)
    del sess["user"]
    sess.save()
    util.redirect (req, "/pantoto-research/login.py")

def index(req, pagelet=""):

    sess = Session.Session(req)
    if not sess.has_key("user"):
        util.redirect (req, "/pantoto-research/login.py")
    user = sess["user"]
    system = getSystem()

    pagelets = system.getAllPagelets()
    wtop = ""
    for i in pagelets:
        wtop = wtop + '<li><a href="runsys.py?pagelet='+i+'">'+i+'</a></li>\n'
    
    if pagelet=="":
        pagelet=pagelets.keys()[0]
    pageletname = pagelet + " pagelet"
            

    req.content_type = "text/html"
    req.write( """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Pantoto-Research</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="style.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="js/jquery.js"></script>
<script type="text/javascript" src="js/cufon-yui.js"></script>
<script type="text/javascript" src="js/arial.js"></script>
<script type="text/javascript" src="js/cuf_run.js"></script>
<script type="text/javascript" src="js/radius.js"></script>
</head>
<body>
<div class="main">
  <div class="header">
    <div class="header_resize">
      <div class="menu_nav">
        <ul>%s
          <li class="last"><a href="#"><b>%s</b></a></li>
        </ul></div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="clr"></div>
  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
          <h2><span>%s</span></h2>
      <form action="runsys.py/exe"><input type="hidden" name="pagelet" value="%s" /><table> """ %(wtop, user,pageletname,pagelet))
#    req.write(str(system.getCurrentState().getState()))
    if pagelet != "":
        context = system.getUserContent(user,pagelet)
        for fieldlabel in context:
            req.write("""<tr><td><label for="field">""" )
            if context[fieldlabel]=='rw':
                req.write("<font color='green'>")
            elif context[fieldlabel]=='r-':
                req.write("<font color='red'>")
            else:
                req.write("<font color='blue'>")
            req.write("""%s :&nbsp;&nbsp;&nbsp;&nbsp;</font></label></td>""" %(fieldlabel))
            t=""
            if context[fieldlabel][0]=='r':
                t = system.getFieldByUser(user,pagelet,fieldlabel)
                if t==None:
                    t=""
            if context[fieldlabel][1]=='w':
                req.write("""<td><input id="1%s" name="1%s" value="%s" class="text" /></td></tr>\n""" %(fieldlabel,fieldlabel,t))
            else:
                req.write("""<td><label for="value">%s</label></td></tr>\n""" %(t))

        buttons = system.getExec(user)

        req.write("</table>")
        for button in buttons:
            req.write("""<br><input type="submit" name="action" value="%s" />\n""" %(button))

    req.write("""
      </form><br>
          <div class="clr"></div>
        </div>
      </div>
      <div class="clr"></div>
    </div>
  </div>
    <div class="footer">
      <p class="lr">&copy; Pantoto</a></p>
      <div class="clr"></div>
    </div>
  </div>
</div>
</body>
</html> """ )
