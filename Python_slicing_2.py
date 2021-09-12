'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

#python slicing method 

'seperate One Word from line of sentence '

#syntax of slicing Is 
'[start :stop]'
#for example 
name ='This Is python slicing Try method '

#find index value in name variable 
print (name[0])#return 't 'string 

#find string value in name variable 
print (name.index('d ')) #return 32 value 

#full line print
name1 = (name [:]) #store index value to Variable
print (name1 )     #print Variable name 

#or You Can print direct 
print(name[:]) #This index print entire line 

#suppose You Need Some kind of Word 
'for example '#i Need python slicing Word 
print (name[8 :23])#8 is start Word  number 23 Is end Word number 

'You Can Also slice The Word in statement '
#syntax of slice Word is
#[start :stop :step ]
print (name [::])#This syntax print enter line 

#You Want cut 1 number 
print (name [::1 ]) #1 value Is Not cut Any Word 

#It's start Actually 2 number 
print (name [::2 ])#ti spto lcn r ehd 

#3 Word You Want cut in The line 
print (name [::3 ])

#suppose You Want cut Some particular Word start point 
#mention start index value 

print (name[8:32:3 ])#8 Is start line 32 Is  end line 3 is cut Word 3 character 


