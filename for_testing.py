import os
import requests
import fitz

print(fitz.__file__)
#from tqdm.auto import tqdm
#Note: tqdm is used to obtain a progress bar from any loop you run with it

# Get PDF path 
# Change this variable to your pdf path______________________________
pdf_path = r"G:\My Drive\feines 2025\MS Imaging paper\to submit.pdf"
#____________________________________________________________________

# Check that the path exists
if os.path.exists(pdf_path):
    print(f"PDF file '{pdf_path}' exists.")
else:
    print(f"PDF file '{pdf_path}' does not exist")

# Open the PDF file
document = fitz.open(pdf_path)