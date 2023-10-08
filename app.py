from flask import Flask,jsonify
import pandas as pd
import openpyxl
import pdfplumber

app = Flask(__name__)


@app.route('/v1/process')
def process():
    print('we are in process!')
    data = {'message':'processed'}
    return jsonify(data) , 200



def import_bill_database_from_excel(filepath):
    '''gets an excel file name and imports data from it'''
    df = pd.read_excel('filepath',0)

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






def make_numbers_list():
    pass


if __name__ == '__main__':
    app.run('0.0.0.0','5000',debug=True)
