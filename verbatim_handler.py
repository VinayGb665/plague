import sys
import pandas as pd
import os
import subprocess
from subprocess import check_output
import pprint
import numpy as np
from comment_handler import remove_comments_and_docstrings
from src import type_zero
from src import type_one
from src import type_two
from src import type_three
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY   
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

w_lev0 = 0.295
w_lev1 = 0.265
w_lev2 = 0.245
w_lev3 = 0.205

def fun(details,data): 
    doc = SimpleDocTemplate("Report.pdf", pagesize=letter)
    
    h3 = PS(name = 'Heading1',
     fontSize = 24,
     leading = 230,
     leftIndent = 150,
     textColor = "white",
     fontName="Helvetica-BoldOblique")


    h1 = PS(name = 'Heading1',
     fontSize = 36,
     leading = 290,
     leftIndent = 100,
     textColor = "red",
     )


    h2 = PS(name = 'Heading2',
     fontSize = 12,
     leading = 24,
     leftIndent = 10)

    h4 = PS(name = 'Heading2',
     fontSize = 12,
     leading = 14,
     leftIndent = 10,
     fontName="Helvetica-BoldOblique")



    elements = []
    elements.append(Paragraph('', h1))
    elements.append(Paragraph('x', h3))
    elements.append(Paragraph('Plagiarism Report', h1))
    elements.append(Paragraph('__________________________________________________________________',h2))
    elements.append(Paragraph('SUBMISSION BY: ' +details['sub_by'], h4))
    elements.append(Paragraph('SUBMISSION DATE: '+str(details['sub_date']), h4))
    elements.append(Paragraph('SUBMISSION ID: '+details['sub_id'], h4))
    elements.append(Paragraph('ASSIGNMENT NAME: '+details['sub_name'], h4))
    elements.append(Paragraph('COURSE NAME: '+details['sub_course'], h4))
    elements.append(Paragraph('TOTAL FILES: '+str(details['sub_files']), h4))

    elements.append(PageBreak())
    sList = [('BOX', (0,0), (-1,-1), 0.25, colors.black),('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), ('TEXTCOLOR', (0,0), (-1,0), colors.blue)]
    
    for i in range(1, len(data)):
        if data[i][-1] >= 60:
            sList.append(('BACKGROUND', (0,i), (-1,i), colors.red))
            sList.append(('TEXTCOLOR', (0,i), (-1,i), colors.white))
    
    t=Table(data)
    t.setStyle(TableStyle(sList))
    elements.append(t)  
    doc.build(elements)
    os.system('xdg-open /home/dexter/Desktop/Projects/plague/Report.pdf')



def handle_multiple(argument_array,sub,file=True):
    '''
        Input - array of files to be compared   
            runs plag check on each of the file and builds the table array
        Ouput 
    '''
    details = sub
    print(argument_array)
    temp=argument_array
    size=len(argument_array)
    if(size <= 1):
        argument_array=[]
        for root, dirs, files in os.walk("./dataset/"+temp[0]):  
            for filename in files:
                argument_array.append(temp[0]+'/'+filename)
        size=len(argument_array)
    print("Later:",argument_array)
    init_array=np.zeros((size,size))
    init_array2=np.zeros((size,size))
    
    my_list = [['Filename 1', 'Filename 2', 'Type 0 Score', 'Type 1 Score', 'Type 2 Score', 'Type 3 Score', 'Total']]
    
    for i in range(0,size):
        for j in range(i+1,size):
            if(j!=i and init_array[i][j]==0):
                
                type_zero_score=type_zero.compare_files(argument_array[i],argument_array[j])
                type_one_score=type_one.compare_files(argument_array[i],argument_array[j])
                type_two_score=type_two.compare_files(argument_array[i],argument_array[j])
                type_three_score=type_three.compare_files(argument_array[i],argument_array[j])
                # print(type_zero_score,type_one_score)
                # except Exception as e :
                #     print(e)
                #     type_zero_score=[0.5]
                #     type_one_score=[0.5]
                x = len(temp[0]) + 1
                Total = min(100.0, round((w_lev0*type_zero_score[0]+type_one_score[0]*w_lev1+w_lev2*type_two_score[0]+w_lev3*type_three_score[0]), 2))
                print("For Files: ", argument_array[i], "and" ,argument_array[j])
                my_list.append([argument_array[i][x:-3][:17], argument_array[j][x:-3][:17], type_zero_score[0], type_one_score[0], type_two_score[0], type_three_score[0], Total])
                
                # init_array[i][j]=int((w_lev0*type_zero_score[0]+type_one_score[0]*w_lev1))
                # +w_lev3*type_three_score[0])
                
                init_array[i][j]=min(100,int((w_lev0*type_zero_score[0]+type_one_score[0]*w_lev1+w_lev2*type_two_score[0]+w_lev3*type_three_score[0])))
                init_array.astype(int)
                
                # init_array2[i][j]=temp[1]
    # print("\n Similarity matrix using diff shit : \n")
    # print(init_array)
    # print("\n Similarity matrix with levenShteins shit: \n")
    # print(init_array2)
    # print("xxxxx",my_list)
    # print("\n\n\n\n\n\nggggggg\n\n\n\n\n\n\n\n")
    cols = list(map(os.path.basename,argument_array))
    details['sub_files']=len(cols)
    if(file):
        fun(details,my_list)
    
    # df = pd.DataFrame(np.amax(init_array,1),index=cols,columns=['score'])
    df = pd.DataFrame(np.matrix(init_array),index = cols, columns = cols)
    # print(np.amax(init_array,1))
    df.astype('int32')
    html = df.to_html()
    return html

