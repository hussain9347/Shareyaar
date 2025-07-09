import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash
from werkzeug.utils import secure_filename

# --- App Initialization ---
# This setup correctly tells Flask where to find the HTML files.
# Since app.py is in 'Backend/', '../' points to the parent 'Share-yaar/' folder.
app = Flask(
    __name__,
    template_folder='../' 
)

# --- Configuration ---
# This ensures the 'uploads' folder is created in the main 'Share-yaar' directory.
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'uploads'))
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'rar', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'enc'} # Added .enc for encrypted files

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'a-very-secret-key-change-it' # It's important to change this!
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size

# --- Helper Function ---
def allowed_file(filename):
    """Checks if the file's extension is in the ALLOWED_EXTENSIONS set."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- Route for the main page (upload and file list) ---
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    """
    Handles file uploads and displays the list of uploaded files.
    """
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part in the request.', 'error')
            return redirect(request.url)
        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected. Please choose a file to upload.', 'info')
            return redirect(request.url)
            
        # The filename is now handled client-side, so we just save it.
        # The client-side JS will add a .enc extension.
        filename = secure_filename(file.filename)
        
        # Ensure the upload folder exists before saving
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])
            
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash(f'Encrypted file "{filename}" uploaded successfully!', 'success')
        return redirect(url_for('upload_file'))

    # For a GET request, list the files in the upload folder
    uploaded_files = []
    if os.path.exists(app.config['UPLOAD_FOLDER']):
        try:
            file_list = os.listdir(app.config['UPLOAD_FOLDER'])
            uploaded_files = [f for f in file_list if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f))]
        except OSError as e:
            flash(f"Error reading the uploads directory: {e}", "error")

    return render_template('index.html', files=uploaded_files)

# --- NEW ROUTE for the download page ---
@app.route('/share/<filename>')
def share_file(filename):
    """
    Renders the download page for the recipient.
    """
    # Just pass the filename to the template. The template's JS will handle the rest.
    return render_template('download.html', filename=filename)

# --- Route for serving the raw file data for download ---
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    Provides the raw (encrypted) file data for download.
    """
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        flash("Sorry, that file could not be found.", "error")
        # A proper error page would be better in a real app
        return "File not found.", 404

# --- Route for deleting files ---
@app.route('/delete/<filename>')
def delete_file(filename):
    """
    Deletes a specific file from the 'uploads' directory.
    """
    try:
        safe_filename = secure_filename(filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], safe_filename)
        
        if os.path.exists(file_path):
            os.remove(file_path)
            flash(f'File "{safe_filename}" has been deleted.', 'success')
        else:
            flash('File not found or invalid filename.', 'error')
    except Exception as e:
        flash(f'Error deleting file: {e}', 'error')
    
    return redirect(url_for('upload_file'))


# --- Running the App ---
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=5000, debug=True)
