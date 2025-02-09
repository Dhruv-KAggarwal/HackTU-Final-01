import torch
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import random
import uuid
import os
from datetime import datetime

# Step 1: Load the model and tokenizer
model = BertForSequenceClassification.from_pretrained('./main1')
tokenizer = BertTokenizer.from_pretrained('./main1')

# Assuming predict_with_features is defined somewhere in your code
def predict_with_features(sequence):
    # Tokenize the input sequence
    inputs = tokenizer(sequence, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim=1).item()
    return predicted_class_id

def generate_csv_report(features, filename):
    # Convert the features dictionary to a pandas DataFrame
    features_df = pd.DataFrame([features])  # Create a DataFrame from the dictionary

    # Export the DataFrame to a CSV file
    features_df.to_csv(filename, index=False)
    print(f"CSV report generated: {filename}")

def test_prediction(sequence):
    output = predict_with_features(sequence)
    return output

# Example usage:
if __name__ == "__main__":
    # Example features and filename
    features = {"feature1": 1, "feature2": 2}  # Replace with actual features
    filename = "output.csv"
    
    generate_csv_report(features, filename)
    
    # Example sequence
    new_sequence = "AGCTGATCG"  # Replace with actual sequence
    result = test_prediction(new_sequence)
    print(result)