from mod_python import util, Session
from engine import *
from dbase import *

def addhandler(req,username,action,user,pagelet,field,perm):
    
    system = getSystem()
    
    system.addHookToAction(username, action,{user:{pagelet:{field:perm}}})

    setSystem(system)
    util.redirect(req,"/pantoto-research/transitions.py")



def addtransition(req, name, user, initstate, finalstate, channel, send ):
    
    system = getSystem()

    if send == "Send":
        send = True
    else:
        send = False

    trans = Transition(user, channel, send, initstate, finalstate, name)
    system.addTransition(trans)

    setSystem(system)
    util.redirect(req,"/pantoto-research/transitions.py")

def index(req):

    system = getSystem()
    
    transitions = system.getTransitions()

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
      <div class="logo"> <img src="images/logo.png" alt="" height="100" />
      </div>
      <div class="clr"></div>
      <div class="menu_nav">
        <ul>
          <li><a href="users.py">Users</a></li>
          <li><a href="pagelets.py">Pagelets</a></li>
          <li><a href="transitions.py">Transitions</a></li>
          <li class="last"><a href="run.py">Run system</a></li>
        </ul></div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="clr"></div>
  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
          <h2><span>Transitions and associated handlers</span></h2><br>
      <table border=1><tr><th>User</th><th>Event</th><th>Event State</th><th>Next State</th><th>Channel</th><th>Send</th><th>Handler</th><th>Add Handler</th></tr>""")

    for i in transitions:
        for j in transitions[i]:
            req.write("<tr><td>%s</td>" %(i))
            req.write("<td>%s</td><td>" %(j))
            req.write(str(transitions[i][j][0])+"</td><td>"+str(transitions[i][j][1])+"</td><td>"+str(transitions[i][j][3])+"</td><td>"+str(transitions[i][j][4])+"</td><td>"+str(transitions[i][j][2])+"</td>")
            req.write("""<td><center><form action="addhandler.py" method="post"><input name="username" type="hidden" value="%s"/><input name="action" type="hidden" value="%s"/><input type="image" name="imageField" id="imageField" src="images/go.gif" class="send" /></form></center></td>""" %(i,j))
            req.write("</tr>")
    
    req.write("""
      </table><br>
          <div class="clr"></div>
        </div>
      </div>
      <div class="sidebar">
        <div class="gadget">
          <h2 class="star">Menu</h2>
          <div class="clr"></div>
          <ul class="sb_menu">
            <li><a href="transitions.py">View Transitions</a></li>
            <li><a href="addtransition.py">Add Transitions</a></li>
          </ul>
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
