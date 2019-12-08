from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import os

# Estrutura básica do flask
app = Flask(__name__,template_folder='templates',static_folder='static')
UPLOAD_FOLDER = os.path.join(os.getcwd(),'upload')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    file = request.files['teste']
    savePath = os.path.join(UPLOAD_FOLDER,secure_filename(file.filename))
    file.save(savePath)
    return 'ok'

#-------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

