from mod_python import util, Session
from engine import *
from dbase import *

def init(req, **params):
	
	system = getSystem()

	initstate = {}

	for i in params:
		if i[0]=='1':
			initstate[i[1:]]=params[i]

	del system.view
	system.view = {}

	system.emptyFields()
	system.setInitialState(State(initstate))

	setSystem(system)
	util.redirect(req,"/pantoto-research/userpage.py")



def index(req,**params):
	
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
        </ul></div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="clr"></div>
  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
          <h1><span>Login Page</span></h1>
	  <div class="clr"></div>
	  <br>
	  <br>
	  <form id="form" name="form" method="post" action="runsys.py/loginverify">
	  	<span>
	  	<h3>User Name : <h3><input name="username" type="text"/>
	  	</span><br><br>
		<input type="submit" value = "Enter" /><br><br>  
	</form>
	  </table><br>
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
