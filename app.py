import pandas as pd
import openpyxl
import pdfplumber

def pdf_to_dictionary(filepath,number_usage):
    
    '''convert pdf to txt'''
    txt = ''
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            txt += page.extract_text()
    
    '''delete useless data'''
    file_lines = txt.split('\n')
    sep = '\n'.join(file_lines[1:12])
    data = txt.split(sep)
    txt = ''.join(data)
    
    '''convert txt to dictionary'''
    file_lines = txt.split('\n')
    ending_point = 'ﻞﮐ ﻊﻤﺟ'
    for line in file_lines:
        if ending_point in line:
            break
        else:
            sections = line.split(' ')
            if len(sections) > 12:
                usage = int(''.join(sections[0].split(',')))
                number_usage[sections[12][2:]] = usage

