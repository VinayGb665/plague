from services.db_con import *
test_dict =dict()
test_dict['username']='ad1'
test_dict['email']='ss@ss.com'
test_dict['course_code']='UE15CS102'
test_dict['password']="a"
print(add_member(test_dict,admin=True))
#delete_course('SMD','UE15CS102')
list_ass('SMD','UE15CS333')
#list_members()
add_course('SMD','UE15CS333')
print(list_courses('SMD'))
# print(add_member(test_dict,admin=True))
#print(delete_member(test_dict))
# 

# login(test_dict)