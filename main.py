from flask import Flask,render_template,redirect,flash
from flask import request
import json
with open("config.json",'r') as c:
    condition=json.load(c)["condition"]
app = Flask(__name__) # defining app
@app.route('/login',methods=['GET','POST']) #creating endpoint having request methods
def dashboard_login(): # functioon of endpoint
    if request.method=='POST': # checking if method is post or not
        username=request.form.get('uname') # taking username
        password=request.form.get('pswd') # taking password
        if not username.isalpha():
            print(condition["status4"])
            return('{  "status":'+str(condition["status4"])+","+"<br>"+"&nbsp;&nbsp;&nbsp;"+'"msg": "'+(condition["msg4"]+'"'+"<br>"+"}"))
            #return(str(condition["msg4"]))
        elif len(password)<6:
            return('{  "status":'+str(condition["status2"])+","+"<br>"+"&nbsp;&nbsp;&nbsp;"+'"msg": "'+(condition["msg2"]+'"'+"<br>"+"}"))
            #return(str(condition["msg2"]))
        elif password.isalpha():
            print(condition["status2"])
            return('{  "status":'+str(condition["status3"])+","+"<br>"+"&nbsp;&nbsp;&nbsp;"+'"msg": "'+(condition["msg3"]+'"'+"<br>"+"}"))
            #return(str(condition["msg3"]))
        
        else:
            return('{  "status":'+str(condition["status1"])+","+"<br>"+"&nbsp;&nbsp;&nbsp;"+'"msg": "'+(condition["msg1"]+'"'+"<br>"+"}"))
            #return(str(condition["msg1"]))

    else:
        return render_template("login.html") # to display login page
app.run() # running app









#if not password.isalpha(): # passowrd checking

            # a='''"status": 202,<br>"msg":"Failure: only numbers allowed in username"'''
 #           print(password)
  #          print(condition["status1"])
   #         return(str(condition["status1"]))# to redirect to any page use "return render_template("pagename.html")"
    #    else:
     #       print(password)
      #      print(condition["status2"])
            # b='''"status": 203,<br>"msg":"Failure: only numbers allowed in username"'''
       #     return(str(condition["status2"]))# to redirect to any page use "return render_template("pagename.html")"
#if not password.isalpha(): # passowrd checking
    #print(password)
    #return("Failed password should be alpha-numeric")# to redirect to any page use "return render_template("pagename.html")"
#else:
    #return("Successful") # to redirec
