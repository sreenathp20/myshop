from myshop import app, login_user, login_required, logout_user, login_manager, current_user
from flask import render_template, redirect, request, session, jsonify
import simplejson as json, sys
from myshop.lib.user.user import User
from myshop.lib.user.manageuser import ManageUser
from bson import json_util

@app.route("/login")
#@load_config
def login():
    #print "test", app.test
    return render_template('pages/login.html')

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    print "unauthorized", current_user.get_id()
    #return redirect("/login")
    return redirect("/home")

@app.route("/")
@login_required
def home():
    section = app.current_user.main_access
    print "current_user.main_access", app.current_user.main_access
    #return render_template('pages/'+section+'/layout_blank_page.html', section=section)
    return redirect('/'+section+''+'/')
    #return "under development"

@app.route("/loginuser", methods=["POST"])
def loginuser():
    data = json.loads(request.data)
    if "username" in data and "password" in data:
        params = {}
        params["username"] = data['username']
        params["password"] = data['password']
        u = User(params["username"], params["password"])
        if u.is_authenticated():
            res = {"success": True}
            login_user(u)
            mu = ManageUser()
            print "request.remote_addr", request.remote_addr
            mu.SendNotification(request.remote_addr)
            return json.dumps(res)
        else:
            res = {"success": False}
            return json.dumps(res)
    else:
        res = {"success": False}
        return json.dumps(res)

@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect("/login")

@login_manager.user_loader
def load_user(userid):
    #print "userid", userid
    try:
        mu = ManageUser()
        cred = mu.GetCredential(str(userid))
        #print "cred", cred
        u = User(cred["_id"], cred["password"])
        u.role = cred["role"]
        u.access = cred["access"]
        u.main_access = cred["main_access"]
    except:
        print "load_user error:", sys.exc_info()[0]
        u = "error check in log"
    return u



