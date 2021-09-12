'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

#input() function 
'syntax of input statement Is '
input () #wating for Get input value from user 
input ("enter Your name ") #Get user name value 
#Now store input value to Any variable 

user_name = input("enter Your favourite hero name :")
print (user_name) #return favourite hero name 
print (type (user_name)) #return data type 

#Do The  project in input function 
'''project Is 
Get The name from user and stored The name in variable 
Also Get user data of birth ,States store variable name 
and display What type data They give It '''

name =input('enter Your name :')
print ('This Is Your name:',name )
print (type (name))
age=int (input ('enter Your age:'))
print('Your age Is :',age )
print (type(age))
date_of_birth =int (input('enter Your date of birth:',))
print('Your date of birth is :',date_of_birth)
print (type(date_of_birth))

#from This output May What I understand Is Any type of data Get from input
'''python understand It\'s string That Is Why return The
age and date of birth type value It's string ,But I expect age date of birth
type value return integer ,so What to Do '''

#typecasting 
# simple to change age & date f birth type 
