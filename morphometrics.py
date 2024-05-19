# This is an code analysis of the Fisher Iris Data set.
# In this file, we code for
# Author: Laura Lyons.

# This code was based off Programming and Scription: Lab06- Topic Functions.
# Reference: https://github.com/andrewbeattycourseware/pands-course-material/blob/main/code/topic06-functions/lab06.06-together1.py

def displayMenu():
    print("Which variable do you wish to estimate?")
    print("\t(sl) Sepal Length")
    print("\t(sw) Sepal Width")
    print("\t(pl) Petal Width")
    print("\t(pw) Petal Width")
    print("\t(q) Quit")
    choice = input("Type one option (sl/sw/pl/pw/q):").strip()
    return choice


def calculate_sl(sepal_length):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()

    return modules
def displayModules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}") 


def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);


#main program
students = []
choice = displayMenu()
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()
        
        