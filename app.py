from flask import Flask, request, jsonify, render_template
import yt_dlp
import os
from werkzeug.utils import secure_filename
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

app = Flask(__name__)

DOWNLOAD_FOLDER = 'downloads'
UPLOAD_FOLDER = 'uploads'
CONVERT_FOLDER = 'converted'

os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form.get('url')
    format = request.form.get('format')
    resolution = request.form.get('resolution')

    if not video_url:
        return jsonify({"error": "URL video tidak ditemukan"}), 400

    if format == 'mp4':
        if resolution == 'auto':
            fmt = 'bestvideo+bestaudio/best'
        else:
            fmt = f'bestvideo[ext=mp4][height<={resolution}]+bestaudio[ext=m4a]/mp4'

        ydl_opts = {
            'format': fmt,
            'merge_output_format': 'mp4',
            'ffmpeg_location': r'C:\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }

    elif format == 'mp3':
        ydl_opts = {
            'format': 'bestaudio',
            'ffmpeg_location': r'C:\ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        return jsonify({"error": "Format tidak didukung"}), 400

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        return jsonify({"message": "Download berhasil!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/docx-to-pdf', methods=['POST'])
def docx_to_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'File tidak ditemukan'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'Nama file kosong'}), 400

    if not file.filename.endswith('.docx'):
        return jsonify({'error': 'File harus .docx'}), 400

    filename = secure_filename(file.filename)
    docx_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(docx_path)

    pdf_name = filename.replace('.docx', '.pdf')
    pdf_path = os.path.join(CONVERT_FOLDER, pdf_name)

    doc = Document(docx_path)
    c = canvas.Canvas(pdf_path, pagesize=A4)

    width, height = A4
    y = height - 40

    for para in doc.paragraphs:
        c.drawString(40, y, para.text)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()

    return jsonify({
        'message': 'Convert berhasil',
        'pdf': pdf_name
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
