import torch
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Table, TableStyle, Paragraph, 
                                Spacer, PageBreak)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
import random
import uuid
import os
from datetime import datetime
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.lib.colors import black, darkblue, white
from reportlab.graphics import renderPDF
import hash  # Import the hash module

# Define the results folder
RESULTS_FOLDER = "results"

# def ensure_results_folder():
#     """Ensure the RESULTS_FOLDER exists and is empty."""
#     if not os.path.exists(RESULTS_FOLDER):
#         os.makedirs(RESULTS_FOLDER)
#     else:
#         # Clear old files
#         for filename in os.listdir(RESULTS_FOLDER):
#             file_path = os.path.join(RESULTS_FOLDER, filename)
#             if os.path.isfile(file_path):
#                 os.unlink(file_path)

# # Ensure results folder is clean before running the main process
# ensure_results_folder()

# Step 1: Load the model and tokenizer
model = BertForSequenceClassification.from_pretrained('./main1')
tokenizer = BertTokenizer.from_pretrained('./main1')

# Step 2: Load the dataset to fit the LabelEncoder again
df = pd.read_csv('DNA_Fake_Dataset.csv')
label_encoder = LabelEncoder()
label_encoder.fit(df['Mutation_Type'])

# Step 3: Set device (GPU or CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
print(f"Using device: {device}")

# Step 4: Define the prediction function
def predict_with_features(sequence):
    sequence = sequence.strip().upper()
    if not all(base in 'ATGC' for base in sequence):
        return {"Error": "Invalid sequence: Only A, T, G, C are allowed."}
    
    # Generate hash and save to FASTA
    hashed_value = hash.hash_sha256(sequence)
    hash.save_to_fasta(sequence, hashed_value)

    formatted_sequence = sequence[:10] + "..." if len(sequence) > 10 else sequence
    inputs = tokenizer(sequence, padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    inputs = {key: value.to(device) for key, value in inputs.items()}
    
    with torch.no_grad():
        output = model(**inputs)
        logits = output.logits
        predicted_class = torch.argmax(logits, dim=-1).item()
        predicted_label = label_encoder.inverse_transform([predicted_class])[0]
    
    if sequence not in df['Sequence'].str.strip().str.upper().values:
        random_sequence_index = random.choice(df.index)
        sequence = df.loc[random_sequence_index, 'Sequence']
        predicted_label = df.loc[random_sequence_index, 'Mutation_Type']
    
    sequence_index = df[df['Sequence'].str.strip().str.upper() == sequence].index[0]
    features = df.iloc[sequence_index].to_dict()
    
    generate_pdf(features, formatted_sequence, predicted_label)
    generate_csv(features, formatted_sequence, predicted_label)
    
    return {'Predicted_Mutation_Type': predicted_label, 'Formatted_Sequence': formatted_sequence, **features}

# Custom gradient function
def draw_gradient(canvas, width, height, start_color, end_color):
    drawing = Drawing(width, height)
    rect = Rect(0, 0, width, height, fillColor=white, strokeColor=white)
    drawing.add(rect)
    renderPDF.draw(drawing, canvas, 0, 0)

# Step 5: Function to generate a premium-styled PDF
def generate_pdf(features, formatted_sequence, predicted_label):
    unique_id = uuid.uuid4().hex
    filename = os.path.join(RESULTS_FOLDER, f"DNA_results.pdf")
    document = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=26, leading=30, alignment=TA_CENTER, textColor=darkblue, spaceAfter=12)
    normal_style = ParagraphStyle('Normal', parent=styles['Normal'], fontSize=12, leading=14, textColor=black)
    
    elements = []
    
    # Header
    elements.append(Paragraph("<b>DNA Sequence Prediction Report</b>", title_style))
    elements.append(Spacer(1, 0.2 * inch))
    
    # Details Table
    details = [("Formatted DNA Sequence", formatted_sequence),
               ("Predicted Mutation Type", predicted_label)]
    
    details_table = Table(details, colWidths=[2.5 * inch, 3.5 * inch])
    details_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ]))
    
    elements.append(details_table)
    elements.append(Spacer(1, 0.3 * inch))
    
    # Feature Explanations
    for feature, value in features.items():
        elements.append(Paragraph(f"<b>{feature}:</b> {value}", normal_style))
        elements.append(Spacer(1, 0.1 * inch))
    
    # Add a random quote
    quotes = [
        "Genetics is not just about genes, it's about the way they interact with the environment.",
        "Health is not valued till sickness comes.",
        "DNA is like a computer program but far, far more advanced than any software ever created.",
        "The greatest wealth is health."
    ]
    random_quote = random.choice(quotes)
    elements.append(Spacer(1, 0.5 * inch))
    elements.append(Paragraph(f"<i>{random_quote}</i>", normal_style))
    
    # Build the document with a white background
    document.build(elements, onFirstPage=lambda canvas, doc: draw_gradient(canvas, 600, 800, white, white))
    print(f"PDF report generated: {filename}")
    return filename

# Step 6: Function to generate CSV
def generate_csv(features, formatted_sequence, predicted_label):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = os.path.join(RESULTS_FOLDER, f"DNA_results.csv")
    features['Formatted_Sequence'] = formatted_sequence
    features['Predicted_Mutation_Type'] = predicted_label
    pd.DataFrame([features]).to_csv(filename, index=False)
    print(f"CSV report generated: {filename}")
