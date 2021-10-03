# --------------------
# PYTHON STARTING PACK
# --------------------
# written by LocalScript
#Basics



# Booleans = "False" "True" ["Not False" "Not True"]


# [TYPE_LIST]
#str = "String"
#bool = "Boolean"
#int = "Integer"
#float = "float"
#[]

# [OPERATOR_LIST]
# EqualityChecker = "=="
# InequalityChecker = "!="
# Greater = ">"
# Less = "<"
# Greather or equals = ">="
# Less or equals = "<="
#[]


# [LIST_PRESETS]           
# Dictionary = "dict"      New dictionary initialized from a mapping object's  (key, value) 
# Tuple = "Tuple"          If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.
# Set = "set"              New empty set object set(iterable) -> new set object
# List = "list"            If no argument is given, the constructor creates a new empty list. The argument must be an iterable if specified.
#[]

#[VALUE_TYPES]
Bool = True
integer = 30
Float = 30.33
string = "Local"

my_list = ["A", "B", "C", "D"]
my_tuple = ("A", "B", "C", "D")
my_dict = {"A":"a", "B":"b", "C":"c", "D":"d"}
my_list_var2 = ([("A",3), ("B",5), ("C", 7)])
my_set = {'A', 'B', 'C', 'D'}
#[]




#print = "print(Any Value)"
def example_code_print():
    print("Hello Word!")

def example_code_print2():
    print(integer)

# Python automaticly converts Integer to Float [30 + 30.33 = 60.33]
def example_code_print2(): 
    print(integer + Float) 

def example_code_print3_errored(): 
    print(integer + Float + "String") # In this code you will get an error because for "+" unsupported format is [STR] so it cant calculate.

#interprinting = print(f"{value}")
def example_code_inter_print():
    print(f"Value is: {integer}")

#Avancedprinting = print(type(value or variable))
def example_code_adv_print():
    print(type(Bool))
    print(type(integer))
    print(type(Float))
    print("List Format")
    print("----------")
    print(type(my_list))
    print("----------")
    print("Dict Format")
    print("----------")
    print(type(my_dict))
    print("----------")
    print("Tuple Format")
    print("----------")
    print(type(my_tuple))
    print("----------")
    print(type(my_list_var2))
    print("----------")
    print("Set Format")
    print("----------")
    print(type(my_set))
    print("----------")

    print("Dict Format Conv")
    print("----------")
    print(dict(my_list_var2))
    print("----------")
    print("Set Format Conv")
    print("----------")
    print(set(my_list_var2))
    print("----------")
    print("List Format Conv")
    print("----------")
    print(list(my_list_var2))
    print("----------")
    print("Tuple Format Conv")
    print("----------")
    print(tuple(my_list_var2))
    print("----------")

    print(type(False))
    print(type(70))
    print(type(70.22))



#IntermediatePrinting = print(TYPE_LIST(NumberValue))
def example_code_inter_print():
    print(bool(Float))

#IntermediatePrinting = print(TYPE_LIST(NumberValue) - For True you will get 1 for False 0 in integer value.)
def example_code_inter_print2():
    print(int(Bool)) 


#sum = "sum(objectvalue) - Adding the list's Values together."
def example_code_sum():
    shoper = [3,2,82.3]
    summarize = sum(shoper)
    print(summarize)


# append = "[Value].append(25) - It places 25 to the end of the list."
def example_code_append():
    shoper = ["kiwis", "peas"]
    shoper.append("chooolate")
    print(shoper)


# insert = "[Value].insert(1, 25) - It places 15 to specified position at the list."
def example_code_insert():
    shopping = ["kiwis", "peas"]
    shopping.insert(0, "lemon")
    print(shopping)


# pop = "[Value].pop() - Removes a value from the end of the list."
def example_code_pop():
    todo = ["call mom", "dishes"]
    todo.pop()
    print(todo)


# While_loop = "While True or [Value] == True false etc. :  or while [Value] < 50  - It will loop until the descripted task is not done. (Current: Until less or equals less than 50 will loop "
def example_code_While_Loop():
    integer = 30
    while integer <= 50:
        integer+=1
        print(integer) #Its starting printing from 31 because I have put printing the Integer after its already added +1 to the number.


# for_loop = " For i in range(NumberValue) It will loop as many times you type in the () after the Range. The "i" is the counter for how many times it was coded.  "
def example_code_For_Loop():
    for i in range(3):
         print(i)
         print("Looping!")

# If statement - "If [VALUETYPES] or Variable [OPERATOR_LIST] [BOOLEANS]:"
def example_code_If_Statement():
    if Bool == True:
        print("Bool was True.")
    
def example_code_If_Statement2():
    if integer < Float:
        print("Integer was less than Float.")

def example_code_If_Statement3():
    if integer != Float:
        print("Integer was not equal to Float.")


# It will run both of the codes since both statement is True
def example_code_If_Statement4():
    if integer != Float:
        print("Integer was not equal to Float.")
    
    if integer <= Float:
        print("Integer was less than Float.")


# Elif statement - "Elif [VALUETYPES] or Variable [OPERATOR_LIST] [BOOLEANS]: - It will run if the previous If Statement statement was False"
def example_code_Elif_Statement():
    if Bool == False: # It will skip that code block because Bool is True not False.
        print("Bool was False.")

    elif Bool == True:   # Elif = Elseif"
        print("Bool was True.")
    

# Else statement - "Else:" - This code is running only when all other previous statment was False or not eligible to run.
def example_code_Else_Statement():
    if Bool == False: # It will skip that code block because Bool is True not False.
        print("Bool was False.")

    elif Bool != True:   # Elif = Elseif"
        print("Bool was not True.")

    else:
        print("Bool was True.")
    
#----------------------------------------------------------------------------------------------------------------------------#
#For more tutorials contact me in the Mimo app "LocalScript"

#Place the Function name and after () to Test a function.
example_code_print()



