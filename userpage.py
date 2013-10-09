from mod_python import util, Session
from engine import *
from dbase import *

def index(req,user=""):

    sess = Session.Session(req)
    if sess.has_key("user") and user == "":
        user = sess["user"]
    system = getSystem()
    users = system.getUsers()
    wtop = ""
    for i in users:
            wtop = wtop + '<li><a href="runsys.py/loginverify?username='+i+'" target="iframe">'+i+'</a></li>\n'
    

    req.content_type = "text/html"
    req.write( """
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
  <div class="header">
    <div class="header_resize">
      <div class="menu_nav">
        <ul>""" + wtop + """
          <li class="last"><a href="users.py">Close</a></li>
        </ul></div>
      <div class="clr"></div>
    </div>
  </div>
<iframe frameborder=0 scrolling=no height="100%%" width="100%%" src="about:blank" name="iframe"></iframe>
</body>
</html>

      """)
