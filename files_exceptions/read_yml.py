# imports
import credentials
import yaml

# variables
filepath1 = '../data/credentials.yml'

# functions/steps
with open(filepath1, "r") as stream:
    credentials = yaml.safe_load(stream)

print(credentials)
uname = credentials['qa']
print(uname)

print()
# qa_uname = credentials['qa']['username']
# qa_pword = credentials['qa']['password']
# uat_uname = credentials['uat']['username']
# uat_pword = credentials['uat']['password']
# print('username for qa env:', qa_uname)
# print('password for qa env:', qa_pword)
# print('username for uat env:', uat_uname)
# print('password for uat env:', uat_pword)

# login_page.enter_username(qa_uname)
# login_page.enter_password(qa_pword)

# data for Negative testing:
qa_uname1 = credentials['negative']['case1']['username']
qa_pword1 = credentials['negative']['case1']['password']
qa_uname2 = credentials['negative']['case2']['username']
qa_pword2 = credentials['negative']['case2']['password']
qa_uname3 = credentials['negative']['case3']['username']
qa_pword3 = credentials['negative']['case3']['password']

# uat_uname = credentials['uat']['username']
# uat_pword = credentials['uat']['password']

# print('username for qa env:', qa_uname)
# print('password for qa env:', qa_pword)
# print('username for uat env:', uat_uname)
# print('password for uat env:', uat_pword)
