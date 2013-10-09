from mod_python import util, Session
from engine import *
from dbase import *


def index(req, username, action):
	system = getSystem()
	users = system.getUsers()

	req.write("""
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
          <h2><span>Add a new Handler</span></h2><br>
          <br>
          <form action="transitions.py/addhandler" method="get">
          <ol>
          <li>
	  <input name="username" type="hidden" value="%s"/>
	  <input name="action" type="hidden" value="%s"/>
          <label for="for">User*</label>
          <select name="user">""" %(username,action))
	
	for i in users:
		req.write("""<option value="%s">%s</option>""" %(i,i))

	req.write("""</select>
          </li>
          <li>
          <label for="pagelet">Pagelet*</label>
          <input id="pagelet" name="pagelet" class="text" />
          </li>
          <li>
          <label for="field">Field*</label>
          <input id="field" name="field" class="text" />
          </li>
          <li>
          <label for="perm">Permissions*</label>
          <input id="perm" name="perm" class="text" />
          </li>
          <li>
          <input type="image" name="imageField" id="imageField" src="images/submit.gif" class="send" />
          <div class="clr"></div><br><br>
          </li>
          </ol>
          </form>

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
