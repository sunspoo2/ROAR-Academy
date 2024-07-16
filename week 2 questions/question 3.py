import PyPDF2 
import re
import os

# Define the base directory where your file is located
base_dir = '/Users/aanhn/Documents/GitHub/ROAR-Academy/samples'

# Define the file name
file_name = 'Sense-and-Sensibility-by-Jane-Austen.pdf'

# Combine the base directory and file name to get the full path
file_path = os.path.join(base_dir, file_name)
file_handle = open(file_path, 'rb')
pdfReader = PyPDF2.PdfReader(file_handle) 
page_number = len(pdfReader.pages)   # this tells you total pages 

full_text = ""
for page_num in range(page_number):
    page_object = pdfReader.pages[page_num] 
    page_text = page_object.extract_text()   # this is the str type of full page
    full_text += page_text + "\n"

file_handle.close()#close the file

def clean_text(text):
    text = re.sub(r'\d+', "", text) #remove all numbers
    text = re.sub(r'[^\w\s]', "", text)#remove all punctuation
    text = text.lower()#make everything lowercase
    return text

cleaned_text = clean_text(full_text)#clean the extracted text
words = cleaned_text.split()#split the words


frequency_table = {}#make the dictionary for word frequencies

for word in words:
    if word in frequency_table:
        frequency_table[word] +=1#Count the frequency of each word
    else:
        frequency_table[word] = 1

for word, frequency in frequency_table.items():
    print (f'{word}:{frequency}')