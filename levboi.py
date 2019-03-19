import sys
from Levenshtein import *
import os
import subprocess
from subprocess import check_output
import pprint
import numpy as np
def mysheller(cmd):
    return subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip().split(" ")[0]
def report_plag_1(file1,file2):
    # print("\n**************************\n")
    # print("Iteration for : ",os.path.basename(file1),os.path.basename(file2))
    # print("---------------")
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
    # print("Levenshteins version for :")
    # pprint.pprint(levi_report)
    wc1 = int(mysheller("wc -l "+file1).strip())
    #wc2 = int(mysheller("wc -l "+file2).strip())
    #wc3 = max(wc1,wc2)
    
    #uncomm_wc = check_output("sdiff -s -b -B "+file1+" "+file2+"| wc -l ")
    #print(wc1,wc2,wc3)
    cmd = "sdiff -b -B -s   "+file1+" "+file2+ "  | wc"
    cmd = [ 'diff', '-b','-B','-s', file1, file2,'--ignore-blank-lines','--changed-group-format=%i','|','wc','-l' ]
    lesse = int(subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').split(" ")[0])
    diff_report['similar_lc'] = lesse
    diff_report['base_lc'] = wc1
    # print(lesse)
    if(lesse>0):
        diff_report['sim']=round(lesse/wc1,2)
    else:
        diff_report['sim']=0
    # print("\nSdiff Version: ")
    # pprint.pprint(diff_report)
    # print("**************************\n")
    
    return (diff_report['sim'],levi_report['sim_ratio'])
    #########################__PUT_IT_HERE__##############################

 
    #print("distance:", matching_blocks(editops(txt1,txt2),txt1,txt2))
    #print("distance:", jaro_winkler(txt1,txt2))

'''
   

    print("ppppppp",file1)
    cmd = [ 'wc ', '-l', file1 ]
    diff_report['total_lc'] = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0].decode('utf-8').split(" ")[0].strip()


    cmd = [ 'wc ', '-l', file2 ]
    lc_2 = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0].decode('utf-8').split(" ")[0].strip()
   
    #diff_report['total_lc']=diff_report['total_lc']

    total_lc = max(int(lc_2),int(diff_report['total_lc']))
    

   
    
    # cmd = [ 'sdiff', '-b','-B','-s', sys.argv[1], sys.argv[2],'||','wc','-l' ]
    # print("aaaaa",subprocess.Popen( cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE ).communicate()[0].decode('utf-8').strip().split(" "))
    
    
    #--
    diff_report['similar_lc'] = int(total_lc) - int(subprocess.Popen( cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE ).communicate()[0].decode('utf-8').strip().split(" ")[0])
    #--
    try:
        diff_report['sim']=round((int(diff_report['total_lc'])-int(diff_report['similar_lc']))/int(diff_report['total_lc']),2)
    except:
        diff_report['sim']=0
    if diff_report['sim']<0:
        print("Wc1 :",)
    pprint.pprint(diff_report)
    print("**************************\n")
    return diff_report['sim']
'''
   
    
# cmd = [ 'echo', 'arg1', 'arg2' ]
# print(subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0])
 ######################################################################




def handle_multiple(argument_array):
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

        #do_file(argument_array[i])
    
    
    for i in range(0,size):
        for j in range(0,size):
            if(j!=i):
                temp=report_plag_1(argument_array[i],argument_array[j])
                init_array[i][j]=temp[0]
                init_array2[i][j]=temp[1]
    print("\n Similarity matrix using diff shit : \n")
    print(init_array)
    print("\n Similarity matrix with levenShteins shit: \n")
    print(init_array2)
    return (init_array,init_array2)

#report_plag_1(sys.argv[1],sys.argv[2])
#handle_multiple(sys.argv[1:])