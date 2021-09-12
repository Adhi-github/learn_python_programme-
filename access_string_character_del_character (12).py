'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#accessing character into The string 

var ="Hello World"

'access First character into The string '
print ('print first character var name Is  ',var [0]) #You got H character 

'access Last character character'
print ('Last charter Is ',var [-1])#You got d 

'access intial string '
print ('intial string ',var) #Hello world 

#change string character 

#var [2]='J' #You got error Because string object Does not support item assignment 
print (var)
var1='Change The string '
var=var1 
print (var )#Now You got change The string 

'If  you Want del string '
#use keyword del 
#del var1  #del var1 string value 
#print (var1 ) #You got name error ,var1 Is Not defined 

'string slicing '
#syntax of slicing 
#[start :stop ]

'random string value Get '
print(var [0:6 ])#You got change 

'reverse slicing '
print (var [3:-4]) #nge The str 

'print whole string in index method  '
print (var [:])#change The string 
#or 
print (var [0:-1])

'If You Want print reverse side '
print (var [::-1])#reverse side print 
