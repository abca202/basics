# Chapter 10. Files and Exceptions

# with open('filepath') as aliasNameForTheFile:
#     line1 = aliasNameForTheFile.readline()
#     line2 = aliasNameForTheFile.readline()
#     line3 = aliasNameForTheFile.readline()
#
#     all_lines = aliasNameForTheFile.readlines()
#
#     file_content = aliasNameForTheFile()
#
#     aliasNameForTheFile.close() # no need to close when you read a file starting 'with open'


## with open('../data/products.txt') as prod_list: >> instead like this it's better to go the way shown below

filepath1 = '../data/products.txt'
filepath2 = '../data/sample.txt'
filepath = 'c:/dev/basics/data/products.txt'
# filepath = 'c:\\dev\\basics\\data\\products.txt' # won't work in linux os

print("********** READ file ***********")
with open(filepath) as prod_list:
    contents = prod_list.read()
    print("Contents of the file:\n", contents)

with open(filepath) as prod_list:
    print("Now we are trying to loop through the contents")
    all_lines = prod_list.readlines()
    print(all_lines)
print("Printing specific line5:", all_lines[4]) # line5 is fifth item in the 'products.txt' file but it is index4

for line in all_lines:
        print(line)

print("************* WRITE file appending new content **************")
## the function below will delete the existing content and write a new entered one
## however, the existing content needs to be saved in another file so it could be reused when needed
with open(filepath, 'a') as prod_list:
    prod_list.write('Playstation 5\n') # \n will write next item in the next line
    prod_list.write('Learning Python book\n')
    prod_list.write('First head to Selenium Book\n')
    # check the file content
print()

# print("************* WRITE file deleting old content **************")
# with open(filepath, 'w') as prod_list:
#     prod_list.write('spiderman jacket\n') # \n will write next item in the next line
#     prod_list.write('batman mask\n')
#     prod_list.write('smart tv samsung 70"\n')
#     # check the file content

