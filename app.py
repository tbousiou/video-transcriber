from flask import Flask, request, render_template, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
import os
from transcribe import generate_transcript

UPLOAD_FOLDER = './uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file_object = request.files['input_file']
        
        filename = secure_filename(file_object.filename)
        print("Filename", filename)
        
        # Save file to the uploads folder
        media_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file_object.save(media_file_path)
        
        
        #transcript = transcribe_file(os.path.join('/path/to/save/files', filename))
        transcript = 0
        txt_filename = generate_transcript(media_file_path)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], txt_filename))
        return redirect(url_for('download_file', name=txt_filename))
    return render_template('index.html')


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)