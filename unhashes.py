import hashlib
import os

# Folder where hashes are stored
HASHES_FOLDER = "HASHES"
HASH_FILE = os.path.join(HASHES_FOLDER, "hashed_output.fasta")

def hash_sha256(sequence):
    """Hashes the input sequence using SHA-256"""
    return hashlib.sha256(sequence.encode()).hexdigest()

def verify_hash_in_fasta(input_sequence, filename=HASH_FILE):
    """Verifies if the hashed input matches any stored hash in the FASTA file"""
    if not os.path.exists(filename):
        print("⚠️ FASTA file not found. Make sure the hash file exists in the HASHES folder.")
        return False

    input_hash = hash_sha256(input_sequence)  # Hash the input

    with open(filename, "r") as fasta_file:
        fasta_content = fasta_file.read().split("\n")  # Read all lines

        for i in range(len(fasta_content)):
            if fasta_content[i].startswith(">"):  # Ignore headers
                continue
            if input_hash == fasta_content[i].strip():  # Match found
                return True

    return False  # No match found

if __name__ == "__main__":
    sequence = input("Enter the sequence to check: ")  # Get user input
    if verify_hash_in_fasta(sequence):
        print("✅ Match found! The sequence was stored in the HASHES/hashed_output.fasta file.")
    else:
        print("❌ No match found! The sequence is not in the HASHES/hashed_output.fasta file.")
