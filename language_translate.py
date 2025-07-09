import tensorflow as tf
import os
import io
import unicodedata
import re

custom_cache_dir = "C:\\Users\\chhet\\OneDrive\\Desktop\\Gen AI\\_data"

#importing data
text_file_path = tf.keras.utils.get_file(
    fname="fra-eng.zip",
    origin='http://storage.googleapis.com/download.tensorflow.org/data/fra-eng.zip',
    extract=True,
    cache_dir=custom_cache_dir 
)

dataset_dir = text_file_path
path_to_data_file = os.path.join(dataset_dir, "fra.txt") 


# Check if the file exists
try:
    with io.open(path_to_data_file, mode="r", encoding="utf-8") as f:
        lines = f.read().split("\n")
        lines = [line.strip() for line in lines if line.strip()]

    print(f"Successfully read {len(lines)} lines from: {path_to_data_file}")
    
    #printing few lines
    
    for i in range(50000,50005):
        print(f"{i+1}: {lines[i]}")
except:
    print(f"Error: The file was not found at {path_to_data_file}")
   
   
# Preprocessing the text
def normalize_text(line):
    line = unicodedata.normalize("NFKC", line.strip().lower())
    line = re.sub(r"([^ \w])(?!\s)", r"/1", line)
    line = re.sub(r"\s+", " ", line).strip()
    return line.lower()