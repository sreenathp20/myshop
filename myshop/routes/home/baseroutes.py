from myshop import app, login_required
from flask import render_template, redirect, request, session, jsonify

import simplejson as json
from bson import json_util
from myshop.lib import config


@app.route("/<section>/")
#@login_required
def home_shop(section):
    print "section", section
    url = "http://localhost:1110"
    return render_template('pages/'+section+'/index.html', section=section, url=url)

@app.route("/<section>/<page>")
@login_required
def dashboard(section, page):
    return render_template('pages/'+section+'/'+page+'.html')

@app.route("/<section>/api/dashboard", methods=['GET', 'POST'])
@login_required
def api_dashboard(section):
    hcl = hire_routes.HireRoutes()
    result = hcl.Routes(request)
    return json.dumps(result)

@app.route("/<section>/api/statistics", methods=['GET', 'POST'])
@login_required
def api_statistics(section):
    hr = hire_routes.HireRoutes()
    result = hr.Routes(request, api='statistics')
    return json.dumps(result)

@app.route("/<section>/api/timeseries", methods=['GET', 'POST'])
@login_required
def api_timeseries(section):
    hr = hire_routes.HireRoutes()
    result = hr.Routes(request, api='timeseries')
    return json.dumps(result)

@app.route('/<section>/app.appcache')
def Appcache(section, action=None):
    return render_template('pages/'+section+'/app.appcache')

@app.route('/<section>/appcache.html')
def AppcacheHtml(section, action=None):
    return render_template('pages/'+section+'/appcache.html')


