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

'If You Want slice Every 2 character in string '
#syntax of 
#[start:stope:step]
print (var [0::2])#cag h  tig 

'If You Want slicing 3 or 4 or 5 character Just change step value '
print(var [2::4 ])#a i , starting 2 value print and then Every 4 Word value print 

'suppose If You Want print indeX and rindex '
#index-print strating (|)
#rindex -print end or second (|)

'index slicing '
var2 ='change The |price -200 |turmeric '
#print Only staring index change The value Only 
print (var2 [:var2.index ('|')]) #You got change The 

'suppose You Want print price index value '
print (var2 [var2.index ('|'):var2.rindex('|')]) #You gor |price 200 ,You Want skip The | 
print (var2 [var2.index ('|')+1:var2.rindex('|')])#You got price 200 

'print Last index '
print (var2 [var2.rindex('|')+1:])#You got tumeric 

'If You print Want whole string index'
print (var2 [:])