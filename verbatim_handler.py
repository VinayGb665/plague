import sys
from Levenshtein import *
import os
import subprocess
from subprocess import check_output
import pprint
import numpy as np
from comment_handler import remove_comments_and_docstrings

w_lev0 = 0.54
w_lev1 =0.46

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
    #    print(txt1)
        txt1=remove_comments_and_docstrings(txt1)
        txt2=remove_comments_and_docstrings(txt2)
     #   print(txt1)
    ## Levenshteins version

    # levi_report['distance']=round(distance(txt1,txt2),2)
    # levi_report['simseq_ratio']=round(seqratio(t1,t2),2)
    # levi_report['Jaro_sim']=round(jaro_winkler(txt1,txt2),2)

    ## --

    levi_report['sim_ratio']=round(ratio(txt1,txt2),2)
    wc1 = int(mysheller("wc -l "+file1).strip()) #lcount for base file

    cmd = [ 'diff', '-b','-B','-s', file1, file2,'--ignore-blank-lines','--changed-group-format=%i','|','wc','-l' ]
    
    lesse = int(subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').split(" ")[0])

    diff_report['similar_lc'] = lesse
    diff_report['base_lc'] = wc1
    
    if(lesse>0):
        diff_report['sim']=round(lesse/wc1,2)
    else:
        diff_report['sim']=0
    
    return diff_report['sim']



def handle_multiple(argument_array):
    '''
        Input - array of files to be compared   
            runs plag check on each of the file and builds the table array
        Ouput 
    '''
    temp=argument_array
    size=len(argument_array)
    if(size<=1):
        argument_array=os.listdir(argument_array[0])

        size=len(argument_array)
        for i in range(0,size):
            argument_array[i]=temp[0]+'/'+argument_array[i];
    print(argument_array)
    init_array=np.zeros((size,size))
    init_array2=np.zeros((size,size))
    
    for i in range(0,size):
        for j in range(0,size):
            if(j!=i):
                lev0_sim=verbatim_diff(argument_array[i],argument_array[j])
                lev1_sim=verbatim_diff(argument_array[i],argument_array[j],True)
                
                init_array[i][j]=int((lev0_sim*w_lev0+lev1_sim*w_lev1)*100)
                init_array.astype(int)
                # init_array2[i][j]=temp[1]
    # print("\n Similarity matrix using diff shit : \n")
    # print(init_array)
    # print("\n Similarity matrix with levenShteins shit: \n")
    # print(init_array2)
    return (init_array,list(map(os.path.basename,argument_array)))

