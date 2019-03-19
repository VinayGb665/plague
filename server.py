from flask import Flask
from flask import request,redirect,render_template
from verbatim_handler import handle_multiple
import os
import pandas as pd
from zipfile import  ZipFile
from html_comps import html_header,html_footer
app = Flask(__name__)

@app.route('/')
def hello_world():
    return html_header+render_template('up.html')+html_footer
#     return '''<form id = "uploadbanner"  enctype="multipart/form-data" method = "post" action = "/a">
#       <input id = "fileupload" name="file" type = "file" />
#       <input type = "submit" value = "submit" id = "submit" />
# </form>'''

@app.route('/postme', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #print(request.__dict__)
        
        # check if the post request has the file part
        #print(request.__dict__)
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file :
            
            
            #filename = secure_filename(file.filename)
            filename=file.filename
            #print(filename)
            #
            file.save(filename)
            zip = ZipFile(filename)
            zip.extractall('./tests')
            filename=os.path.join('./tests/', filename[:-4])
            #print("OOPOPO",filename)
            handled=handle_multiple([filename])
            df =pd.DataFrame(handled[0],index=handled[2],columns=handled[2])
            html = df.to_html()
            #print(html_footer)
            return html_header+html+html_footer
            
            
        else:
            return "AAAAAAAAA"
    