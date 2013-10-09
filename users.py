from mod_python import util, Session
from engine import *
from dbase import *


def index(req,user=""):

	system = getSystem()
	
	if user!="":
		system.addUser(user)
		setSystem(system)

	users = system.getUsers()

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
          <h2><span>List of all users</span></h2><br>
	  <table border=1><tr><th>userName:</th></tr>""")

	for i in users:
		req.write("<tr><td>%s</td>" %(i))
	
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
            <li><a href="users.py">View users</a></li>
            <li><a href="adduser.py">Add user</a></li>
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
