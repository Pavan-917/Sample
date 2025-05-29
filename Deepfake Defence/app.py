from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import os
import json
from werkzeug.utils import secure_filename
try:
    from image_blur import pixelate_face
except ImportError:
    def pixelate_face(input_path, output_path):
        print(f"Pixelating face from {input_path} to {output_path}")

# Set absolute paths for upload and blurred folders
UPLOAD_FOLDER = r'D:\Pavan Kumar\Sample\Deepfake Defence\Uploads'
BLURRED_FOLDER = r'D:\Pavan Kumar\Sample\Deepfake Defence\Blurred'
DB_FILE = r'D:\Pavan Kumar\Sample\Deepfake Defence\db.json'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['BLURRED_FOLDER'] = BLURRED_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BLURRED_FOLDER, exist_ok=True)

def load_db():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    images = load_db()
    return render_template('Site.html', images=images)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    caption = request.form.get('caption', '')
    if file:
        filename = secure_filename(file.filename)
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        blurred_filename = os.path.splitext(filename)[0] + '_blurred.jpg'
        blurred_path = os.path.join(app.config['BLURRED_FOLDER'], blurred_filename)
        file.save(original_path)
        pixelate_face(original_path, blurred_path)
        # Update database
        db = load_db()
        db.append({
            "original": filename,
            "blurred": blurred_filename,
            "caption": caption
        })
        save_db(db)
        return redirect(url_for('index'))
    return 'No file uploaded', 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/blurred/<filename>')
def blurred_file(filename):
    return send_from_directory(app.config['BLURRED_FOLDER'], filename)

@app.route('/api/images')
def api_images():
    return jsonify(load_db())

if __name__ == '__main__':
    app.run(debug=True)