import sys
from Levenshtein import *
import os
import subprocess
import pprint
import numpy as np

def report_plag_1(file1,file2):
    print("\n**************************\n")
    print("Iteration for : ",os.path.basename(file1),os.path.basename(file2))
    print("---------------")
    t1=open(file1).readlines()
    t2=open(file2).readlines()
    levi_report = dict()
    diff_report = dict()
    txt1 = "".join(t1)
    txt2 = "".join(t2)
    levi_report['distance']=round(distance(txt1,txt2),2)
    levi_report['sim_ratio']=round(ratio(txt1,txt2),2)
    levi_report['simseq_ratio']=round(seqratio(t1,t2),2)
    levi_report['Jaro_sim']=round(jaro_winkler(txt1,txt2),2)
    print("Levenshteins version for :")
    pprint.pprint(levi_report)
    #print("distance:", matching_blocks(editops(txt1,txt2),txt1,txt2))
    #print("distance:", jaro_winkler(txt1,txt2))

   
    print("\nSdiff Version: ")

    
    cmd = [ 'wc ', '-l', file1 ]

    diff_report['total_lc'] = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0].decode('utf-8')
   
    diff_report['total_lc']=diff_report['total_lc'].split(" ")[0].strip()
    # cmd = [ 'sdiff', '-b','-B','-s', sys.argv[1], sys.argv[2],'||','wc','-l' ]
    cmd = "sdiff -b -B -s   "+file1+" "+file2+ " | wc"

    # print("aaaaa",subprocess.Popen( cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE ).communicate()[0].decode('utf-8').strip().split(" "))
    diff_report['similar_lc'] = int(subprocess.Popen( cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE ).communicate()[0].decode('utf-8').strip().split(" ")[0])
    
    diff_report['sim']=round(int(diff_report['similar_lc'])/int(diff_report['total_lc']),2)
    
    pprint.pprint(diff_report)
    print("**************************\n")
    return diff_report['sim']

# cmd = [ 'echo', 'arg1', 'arg2' ]
# print(subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0])


def handle_multiple(argument_array):
    temp=argument_array
    size=len(argument_array)
    if(size<=1):
        argument_array=os.listdir(argument_array[0])

        size=len(argument_array)

    init_array=np.zeros((size,size))
    for i in range(0,size):
        argument_array[i]=temp[0]+'/'+argument_array[i];
        #do_file(argument_array[i])
    
    
    for i in range(0,size):
        for j in range(0,size):
            if(j!=i):
                init_array[i][j]=report_plag_1(argument_array[i],argument_array[j])
    print("\n Similarity matrix : \n")
    print(init_array)

#report_plag_1(sys.argv[1],sys.argv[2])
handle_multiple(sys.argv[1:])