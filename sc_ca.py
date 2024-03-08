variable = input('Enter the input for which you want the differentiation: ')
print('Use the bracket if you are using the power function (power fn)')
print("For power use ---> ^") 
  
##Defining the power function
def power(a,b):
    value = 1
    while(b!=0):
        value *= a
        b-=1
    return value


def divide(a,b):
    try :
        if(b!=0):
            return a/b
    except :
        return False


def multiply(a,b):
    return(a*b)


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


##Changing the variable to the list 
expression = list(variable)
print(expression)

def expression(variable):
    a = list(variable)
    if(a[len(a)-1] == ' '):
        a.remove(a[len(a)-1])
    return a

list_expression = expression(variable)


        
def checking(value_list,sign_list):

    finaleValue = 0
    ##traverse first for power function
    for i in range(len(sign_list)):
        if(sign_list[i] == '^'):
            value_list[i] = float(value_list[i])
            value_list[i+1] = float(value_list[i+1])
            value_list[i] = power(value_list[i],value_list[i+1])
            value_list.remove(value_list[i+1])
            sign_list.remove(sign_list[i])
            value_list.append(0)
            sign_list.append(0)
    print(value_list)
    print(sign_list)
    
    ##traverse then for * and / function
    for i in range(len(sign_list)):
        try:
            
            if(sign_list[i] == '*' ):
                value_list[i] = float(value_list[i])
                value_list[i+1] = float(value_list[i+1])

                value_list[i] = multiply(value_list[i],value_list[i+1])
                value_list.remove(value_list[i+1])
                sign_list.remove(sign_list[i])
                value_list.append(0)
                sign_list.append(0)
        except:
            print('Error occur maybe cannot divide by zero check your expression once')
        
    print(value_list)
    print(sign_list)
    
            ##traverse then for * and / function
    for i in range(len(sign_list)):
        try:
            
            if(sign_list[i] == '/' ):
                value_list[i] = float(value_list[i])
                value_list[i+1] = float(value_list[i+1])

                value_list[i] = divide(value_list[i],value_list[i+1])
                value_list.remove(value_list[i+1])
                sign_list.remove(sign_list[i])
                value_list.append(0)
                sign_list.append(0)
        except:
            print('Error occur maybe cannot divide by zero check your expression once')

    print(value_list)
    print(sign_list)                
        ##traverse then for + and - 
    # for i in range(len(sign_list)):
    #     if (sign_list[i] == '+' ) :
    #         value_list[i] = float(value_list[i])
    #         value_list[i+1] = float(value_list[i+1])
                
    #         value_list[i] = (value_list[i]+value_list[i+1])
    #         value_list.remove(value_list[i+1])
    #         sign_list.remove(sign_list[i])
    #         value_list.append(0)
    #         sign_list.append(0)
                
    for i in range(len(sign_list)):
        if (sign_list[i] == '-' ) :
            value_list[i] = float(value_list[i])
            value_list[i+1] = float(value_list[i+1])
                
            value_list[i] = (value_list[i]-value_list[i+1])
            value_list.remove(value_list[i+1])
            sign_list.remove(sign_list[i])
            value_list.append(0)
            sign_list.append(0)
                
    for i in value_list:
        i = float(i)
        finaleValue += i
    
    print(value_list,' This is the value list and it must contain only one element and that will be our answer')
    print(sign_list,'This is the sign list ')
    return finaleValue


def evaluation(x):
    value_list = []
    sign_list = []
    a = ''
    
    for i in x:     
        try:
            if(float(i)):
                a+=i
        except:
            value_list.append(a)
            sign_list.append(i)
            a = ''
    value_list.append(a)
    print(sign_list)
    print(value_list)
 

    finaleValue = checking(value_list,sign_list)

    return finaleValue
    
# print(type(evaluation(variable)))
print(evaluation(variable))
