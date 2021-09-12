'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
'string slicing |index slicing  method '

str_name ='aroma |500 |dry skin '
#Now You Just slice The name price &product 
'How to Do That '

#string slicing 
slicing_name =str_name[0:5 ] #store The index value to variable name
#0 is starting index ,5 Is end index value , [] mention index 
print (slicing_name) #output got aroma 

#or use index slicing 

slicing_name=str_name[:str_name.index('|')]
print(slicing_name)#output You got aroma 

'If you Want price value How to print That '

slicing_price=str_name[str_name.index ('|'):str_name.rindex ('|')]
print (slicing_price)#output Is |500 

'If You Want Only 500 index ,Just add +1 into The staring index part '

slicing_price =str_name[str_name.index('|')+1:str_name.rindex ('|')]
print (slicing_price)

#3rd index print 
slicing_product_name =str_name[str_name.rindex('|')+1:]#rindex Is used to Get  Last part slicing (|) 
print (slicing_product_name)#output Is dry skin ,rindex +1 print dryskin : After colon Is print end string 
