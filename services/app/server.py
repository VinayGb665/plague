from flask import Flask
from flask import request,redirect,render_template,session,jsonify,redirect
from verbatim_handler import handle_multiple
import os
import pandas as pd
from zipfile import  ZipFile
from services.db_con import login as check_login
from services.db_con import *
from html_comps import *
from time import sleep
app = Flask(__name__)
app.secret_key = 'any random string';
UPLOAD_FOLDER = './dataset'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def hello_world():
    if 'username' in session:
        return html_header+html_mid+render_template('up.html')+html_footer+script('submission_page')
    else:
        return redirect('/login')

@app.route('/postme', methods=['GET', 'POST'])
def upload_file():
    # if request.method == 'POST':
    #     print(request.form)
    #     print(request.files)
    
    if request.method == 'POST' and 'username' in session:
        if 'file-0' not in request.files:
            print('No file part')
            return redirect(request.url)
        else:    
            file = request.files['file-0']
            if file.filename == '':
                print('No selected file')
                return redirect(request.url)
            if file  and ('username' in session) and ('courseid' in request.form) and ('ass_name' in request.form):
                filename=file.filename
                user = session['username']
                courseid = request.form['courseid']
                ass_name = request.form['ass_name'] 
                file.save(app.config['UPLOAD_FOLDER']+'/'+filename)
                zip = ZipFile(app.config['UPLOAD_FOLDER']+'/'+filename)
                
                filename = os.path.join('', filename[:-4])
                # handled = handle_multiple([filename])
                
                # print(handled[0])
                if update_assignment(ass_name,filename,user,courseid):
                    for name in zip.namelist():   
                        zip.extract(name, app.config['UPLOAD_FOLDER']+'/')
                    return jsonify("True")
                else :
                    return jsonify("False")
                
                
            else:
                
                return jsonify("False")
    else:
        return jsonify("False")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return html_header+style('login')+html_mid+html_login+html_footer+script('admin_login')
    elif request.method == 'POST':
        res = check_login(request.form)
        if res[0] :
            session['isadmin'] = res[1]
            session['username'] = request.form['username']
            return jsonify(['True',session['username'],session['isadmin']])
        else:
            return jsonify(['False'],'',0)



@app.route('/admin',methods=['GET', 'POST'])
def admin_home():
    if 'isadmin' in session and session['isadmin']==1:
        return html_header+style('admin_page')+html_mid+html_admin_page+html_footer+script('admin_page')
    else :
        return redirect('/home')

@app.route('/home',methods=['GET'])
def home_p():
    if 'username' in session :
        return html_header+style('admin_page')+html_mid+html_home_page+html_footer+script('home_page')
    else:
        return redirect('/login')


@app.route('/listusers',methods=['GET', 'POST'])
def list_u():
    return jsonify(list_members())

@app.route('/delete_user',methods=['POST'])
def delete_u():
    print(request.form)
    if delete_member(request.form):
        return 'True'
    else:
        return 'False'


@app.route('/delete_course',methods=['POST'])
def delete_c():
    
    if 'username' in session:
        if delete_course(session['username'],request.form['course_id']):
            return 'True'
        else:
            return 'False'
    else:
        return 'False'


@app.route('/add_member',methods=['POST'])
def add_u():
    return add_member(request.form)
@app.route('/add_course',methods=['POST'])
def add_c():
    if 'username' in session:
        return add_course(session['username'],request.form['course_id'])
    else:
        return 'False'
@app.route('/mycourses/',methods=['GET'])
def me_course():
    if 'username' in session:
        return jsonify(list_courses(session['username']))
    else:
        return jsonify([])

@app.route('/mycourses/<courseid>',methods=['GET'])
def list_cour(courseid):
    if courseid:
        
        return html_header+style('admin_page')+html_mid+html_ass_page+html_footer+script('assignment_page')

@app.route('/listass/<courseid>',methods=['GET'])
def list_as(courseid):
    if 'username' in session:
        user=session['username']
        return jsonify(list_ass(user,courseid))
        
@app.route('/generate',methods=['POST'])
def generate_report():
    if 'username' in session:
        user = session['username']
        print('Illi',request.form)
        dir_name = get_file_name_for_ass(request.form['ass_name'],request.form['course'])
        return handle_multiple([dir_name])
@app.route('/signout',methods=['POST'])
def logout():
    session.pop('username',None)
    session.pop('isadmin',None)
    return "True"