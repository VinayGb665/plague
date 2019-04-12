import sys

import os
import subprocess
from subprocess import check_output
import pprint
import numpy as np
from comment_handler import remove_comments_and_docstrings
from src import type_zero
from src import type_one
from src import type_two
import pandas as pd
w_lev0 = 0.45
w_lev1 = 0.32
w_lev2 = 0.23

def mysheller(cmd):
    return subprocess.Popen(
        cmd,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip().split(" ")[0]

def verbatim_diff(file1,file2,strip=False):
    
    t1=open(file1).readlines()
    t2=open(file2).readlines()

    levi_report = dict()
    diff_report = dict()
    txt1 = "".join(t1)
    txt2 = "".join(t2)
    if(strip==True):
        txt1=remove_comments_and_docstrings(txt1)
        txt2=remove_comments_and_docstrings(txt2)

    wc1 = int(mysheller("wc -l "+file1).strip()) #lcount for base file
    wc2 = int(mysheller("wc -l "+file2).strip()) #lcount for base file 
    wc1=max(wc1,wc2)
    cmd = [ 'diff', '-b','-B','-s', file1, file2,'--ignore-blank-lines','--changed-group-format=%i','|','wc','-l' ]
    
    lesse = int(subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').split(" ")[0])

    diff_report['similar_lc'] = lesse
    diff_report['base_lc'] = wc1
    
    if(lesse>0):
        diff_report['sim']=min(1,round(lesse/wc1,2))
    else:
        diff_report['sim']=0
    
    return diff_report['sim']



def handle_multiple(argument_array):
    '''
        Input - array of files to be compared   
            runs plag check on each of the file and builds the table array
        Ouput 
    '''
    print(argument_array)
    temp=argument_array
    size=len(argument_array)
    if(size<=1):
        # argument_array=os.listdir(argument_array[0])
        
        argument_array=[]
        for root, dirs, files in os.walk("./dataset/"+temp[0]):  
            for filename in files:
                argument_array.append(temp[0]+'/'+filename)
        size=len(argument_array)
    print("Later:",argument_array)
    init_array=np.zeros((size,size))
    init_array2=np.zeros((size,size))
    
    for i in range(0,size):
        for j in range(0,size):
            if(j!=i and init_array[i][j]==0):
                # try:
                type_zero_score=type_zero.compare_files(argument_array[i],argument_array[j])
                type_one_score=type_one.compare_files(argument_array[i],argument_array[j])
                type_two_score=type_two.compare_files(argument_array[i],argument_array[j])
                type_three_score=type_three.compare_files(argument_array[i],argument_array[j])
                # print(type_zero_score,type_one_score)
                # except Exception as e :
                #     print(e)
                #     type_zero_score=[0.5]
                #     type_one_score=[0.5]
                # print(type_zero_score)
                # init_array[i][j]=int((w_lev0*type_zero_score[0]+type_one_score[0]*w_lev1))
                init_array[i][j]=int((w_lev0*type_zero_score[0]+type_one_score[0]*w_lev1+w_lev2*type_two_score[0]))
                init_array.astype(int)
                # init_array2[i][j]=temp[1]
    # print("\n Similarity matrix using diff shit : \n")
    # print(init_array)
    # print("\n Similarity matrix with levenShteins shit: \n")
    # print(init_array2)
    cols = list(map(os.path.basename,argument_array))
    df = pd.DataFrame(np.amax(init_array,1),index=cols,columns=['score'])
    print(np.amax(init_array,1))
    df.astype('int32')
    html = df.to_html()
    return html

