from mod_python import util, Session
from engine import *
from dbase import *

def addfield(req,pagelet,field):
	
	system = getSystem()
	
	system.addField(pagelet,Field(field))
	setSystem(system)
	util.redirect(req,"/pantoto-research/pagelets.py")

def index(req,pagelet=""):

	system = getSystem()
	
	if pagelet!="":
		system.addPagelet(pagelet)
		setSystem(system)
	
	pagelets = system.getAllPagelets()

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
          <h2><span>List of all pagelets</span></h2><br>
	  <table border=1><tr><th>Pagelet</th><th>Fields</th><th>Add Field</th></tr>""")

	for i in pagelets:
		req.write("<tr><td>%s</td><td>" %(i))
		for j in pagelets[i].getFields():
			req.write(j+", ")
		req.write("""</td><td><form action="pagelets.py/addfield" method="post"><input name="pagelet" type="hidden" value="%s"/><input id="field" name="field" class="text"/><input type="image" name="imageField" id="imageField" src="images/go.gif" class="send" /></form>""" %(i))
	
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
            <li><a href="pagelets.py">View Pagelets</a></li>
            <li><a href="addpagelet.py">Add Pagelet</a></li>
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
