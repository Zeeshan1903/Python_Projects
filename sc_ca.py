variable = input('Enter the input for which you want the differentiation: ')
  
###Defining the type of the variable whether integer or not 
def integer_variable(s):
    isInteger = False
    try:
        if(float(s)):
            isInteger = True
        # if(float(s)):
        #     isInteger = True
    except:
        isInteger = False
    return isInteger

# print(integer_variable(variable))
# print(variable)

