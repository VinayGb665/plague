import pymongo
from hashlib import md5
client = pymongo.MongoClient("mongodb+srv://444bcb3a3fcf8389296c49467f27e1d6:2fbd38e6c6c4a64ef43fac3f0be7860e@cluster0-fhhlc.mongodb.net/test?retryWrites=true")

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
        return(hash_org==hash_pass)
    else:
        return False


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

        


    
    
    # db = client['user_db']
    # db = client.test_database
    # print(client.test_database)
    # print()
test_dict =dict()
test_dict['username']='SMD'
test_dict['email']='ss@ss.com'
test_dict['course_code']='UE15CS102'
test_dict['password']="a"
delete_course('SMD','UE15CS102')
#list_members()
# add_course(test_dict)
print(list_courses('SMD'))
print(add_member(test_dict,admin=True))
#print(delete_member(test_dict))
# 
# login(test_dict)