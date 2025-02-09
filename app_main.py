from flask import Flask, render_template, request, send_file, redirect, url_for, flash, session
import os
from werkzeug.utils import secure_filename
from fpdf import FPDF  # For generating PDFs
import load  # Ensure your `load.py` is in the same directory as `app.py`
import hash  # Import the hash module

app = Flask(__name__)

# Configurations
app.secret_key = "your_secret_key"  # Replace with a secure key
RESULTS_FOLDER = "results"
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"fasta"}  # Allowed file extensions

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create necessary directories
os.makedirs(RESULTS_FOLDER, exist_ok=True)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sequence = None

    # Check for file upload
    if 'fasta_file' in request.files and request.files['fasta_file'].filename:
        file = request.files['fasta_file']
        
        if not allowed_file(file.filename):
            return {"success": False, "message": f"Invalid file type. Only {', '.join(ALLOWED_EXTENSIONS)} files are allowed."}

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract sequence from file
        with open(file_path, 'r') as f:
            sequence = ''.join(line.strip() for line in f if not line.startswith('>'))

    # Check for direct sequence input
    if not sequence and 'sequence_input' in request.form:
        sequence = request.form['sequence_input'].strip()

    if not sequence:
        return {"success": False, "message": "No valid input provided."}

    # Generate hash and save to FASTA
    hashed_value = hash.hash_sha256(sequence)
    hash.save_to_fasta(sequence, hashed_value)

    try:
        # Call the prediction function from `load.py`
        result = load.predict_with_features(sequence)

        if 'Error' in result:
            return {"success": False, "message": result['Error']}

        # Extract results
        prediction = result['Predicted_Mutation_Type']
        formatted_sequence = result['Formatted_Sequence']
        features = {k: v for k, v in result.items() if k not in ['Predicted_Mutation_Type', 'Formatted_Sequence']}

        # Store result in session for detailed analysis
        session['result'] = result

        # Generate PDF with results using the function from load.py
        pdf_file_path = os.path.join(RESULTS_FOLDER, "DNA_results.pdf")
        session['pdf_file_path'] = pdf_file_path

        return {"success": True, "pdf_file_path": pdf_file_path}

    except Exception as e:
        return {"success": False, "message": f"An error occurred: {str(e)}"}

@app.route('/detailed_analysis')
def detailed_analysis():
    result = session.get('result')
    if not result:
        flash("No result available for detailed analysis.", "error")
        return redirect(url_for('home'))
    return render_template('detailed_analysis.html', result=result)

@app.route('/download')
def download():
    pdf_path = session.get('pdf_file_path')
    if not pdf_path or not os.path.exists(pdf_path):
        flash("File not found for download.", "error")
        return redirect(url_for('home'))

    return send_file(pdf_path, as_attachment=True)

@app.route('/summary')
def summary():
    return render_template('summary.html')

if __name__ == '__main__':
    app.run(debug=True)
