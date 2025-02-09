import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
import torch
import random
import os

# Load the dataset
df = pd.read_csv('e:/Hackathon/HackTU/Model/synthetic_dna_chemical_risks.csv')

# Load the model and tokenizer
model = BertForSequenceClassification.from_pretrained('e:/Hackathon/HackTU/Final/pookie')
tokenizer = BertTokenizer.from_pretrained('e:/Hackathon/HackTU/Final/pookie')

# Function to predict the risk level
def predict_risk_level(dna_sequence):
    inputs = tokenizer(dna_sequence, return_tensors="pt", padding='max_length', truncation=True)
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1)
    return ['Low', 'Moderate', 'High'][predictions.item()]

# Function to read sequence from a FASTA file
def read_fasta(file_path):
    with open(file_path, 'r') as f:
        return ''.join(line.strip() for line in f if not line.startswith('>'))

# Ask for user input
input_type = input("Enter '1' to input a DNA sequence or '2' to upload a FASTA file: ").strip()

if input_type == '1':
    dna_sequence = input("Enter the DNA sequence (ATGC format): ").strip()
elif input_type == '2':
    file_path = input("Enter the path to the FASTA file: ").strip()
    if os.path.exists(file_path):
        dna_sequence = read_fasta(file_path)
    else:
        print("File not found.")
        exit()
else:
    print("Invalid input.")
    exit()

# Predict the risk level
predicted_risk_level = predict_risk_level(dna_sequence)

# Select a random row from the dataset
random_row = df.sample(n=1).iloc[0]

# Print the details
print(f"DNA Sequence: {dna_sequence}")
print(f"Chemicals to Avoid: {random_row['Chemicals_to_Avoid']}")
print(f"Found in Products: {random_row['Found_in_Products']}")
print(f"Health Impact: {random_row['Health_Impact']}")
print(f"Predicted Risk Level: {predicted_risk_level}")
