import pymongo
from hashlib import md5
import os, re, os.path
#client = pymongo.MongoClient("mongodb+srv://444bcb3a3fcf8389296c49467f27e1d6:2fbd38e6c6c4a64ef43fac3f0be7860e@cluster0-fhhlc.mongodb.net/test?retryWrites=true")
client = pymongo.MongoClient("mongodb://localhost:27017")

def login(body):
    
    hash_pass = md5(body['password'].encode()).hexdigest()
    print(body['password'],hash_pass)
    db= client.user_db
    user_col = db.user_col

    #user_col.update_one({'user':'a'},{ "$set": {'password':md5(b'a').hexdigest()} },upsert=True)
    results=user_col.find_one({'user':body['username']})
    if results:
        print(results['password'],hash_pass)
        hash_org = results['password']
        return ((hash_org==hash_pass),results['isAdmin'])
    else:
        return (False,0)


def add_member(body,admin=False):
    user = body['username']
    email = body['email']
    password = md5(body['password'].encode()).hexdigest()
    print(password)
    db = client.user_db
    user_col = db.user_col
    user_col.create_index('user',unique=True)
    
    try:
        if(admin):
            insert_cur = user_col.insert_one({'user':user,'password':password,'email':email,'isAdmin':1})
            return "Done"
        else:
            insert_cur = user_col.insert_one({'user':user,'password':password,'email':email,'isAdmin':0})
            return "Done"
    except:
        return "User Exists"
    
def delete_member(body):
    user = body['username']
    db = client.user_db
    user_col = db.user_col
    if user_col.delete_one({'user':user}).deleted_count==1:
        return 'Success'
    else:
        return 'Failure'

def list_members():
    db = client.user_db
    user_col = db.user_col
    resArr = []
    for i in user_col.find({},{'_id':0,'user':1,'isAdmin':1,'email':1}):
        resArr.append(i)
    return resArr
    #print(resArr)
    
def list_courses(x):
    db = client.user_db
    user_col = db.user_col
    try:
        return user_col.find_one({'user':x},{'_id':0,'courses':1})['courses']
    except:
        return []

def add_course(user,course):
    db = client.user_db
    user_col = db.user_col
    # user_col.create_index('',unique=True)
    if course:
        user_col.find_one_and_update({'user':user},{'$addToSet':{'courses':course}})
        return 'True'
    else :
        return 'False'

def delete_course(user,course_id):
    db = client.user_db
    user_col = db.user_col
    if course_id and user:
        return user_col.find_one_and_update({'user':user},{'$pull':{'courses':course_id}})
    else:
        return 'False'

def update_assignment(ass,file,user,course,thresh=50):
    db = client.user_db
    user_col = db.user_col
    courses_avail = user_col.find_one({'user':user})['courses']
    print(user,courses_avail,course)

    if course in courses_avail:
        ass_col = db.ass_col
        result = ass_col.find_one_and_update({'ass':ass},{'$set':{'file':file,'user':user,'course':course,'thresh':thresh}},upsert=True)
        print(result)
        if result or result==None:
            print("dude eno ")
            return True
        else:
            print("dude eno 2")
            return False
    else:
        
        
        return False


def list_ass(user,course):
    db = client.user_db
    ass_col = db.ass_col
    arr = []
    for i in ass_col.find({'user':user,'course':course},{'_id':0,'ass':1,'thresh':1}):
        arr.append(i)

    return arr
def get_file_name_for_ass(assname,course):
    db = client.user_db
    ass_col = db.ass_col
    print(assname,course)
    result = ass_col.find_one({'ass':assname,'course':course},{'_id':0,'file':1})
    print(result)
    return result['file']



    # db = client['user_db']
    # db = client.test_database
    # print(client.test_database)
    # print()
# get_file_name_for_ass('Ass3','UE15CS333')


def db_init():
    
    client.drop_database('user_db')
    mypath = "dataset" #Enter your path here
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))
    init_admin = dict()
    init_admin['username']='Admin'
    init_admin['email']='plag_admin@pes.edu'
    init_admin['password']='admin_plag'
    add_member(init_admin,admin=True)
