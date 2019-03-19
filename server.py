from flask import Flask
from flask import request,redirect,render_template
from levboi import handle_multiple
import os
from zipfile import  ZipFile
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('up.html')
#     return '''<form id = "uploadbanner"  enctype="multipart/form-data" method = "post" action = "/a">
#       <input id = "fileupload" name="file" type = "file" />
#       <input type = "submit" value = "submit" id = "submit" />
# </form>'''

@app.route('/postme', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.__dict__)
        
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
            print("Aaaaaaaaaaaaaaaaa")
            #filename = secure_filename(file.filename)
            filename=file.filename
            print(filename)
            #
            file.save(filename)
            zip = ZipFile(filename)
            zip.extractall('./tests')
            filename=os.path.join('./tests/', filename[:-4])
            print("OOPOPO",filename)
            return render_template("base.html",data=handle_multiple([filename]))
            
        else:
            return "AAAAAAAAA"
    