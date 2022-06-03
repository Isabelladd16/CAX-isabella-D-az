print('enter the cashier name:')
name=input()  
print('welecome', name)
print('add your items:')
print('first item')
item1=input()
print('add the price')
price1=int (input())
print('second item')
item2=input() 
print('add the price')
price2=int (input())
print('third item')
item3=input() 
print('add the price')
price3=int (input())
print('fourth item')
item4=input() 
print('add the price')
price4=int (input())
print('fith item')
item5=input() 
print('add the price')
price5=int (input())

subtotal= price1+price2+price3+price4+price5
print('subtotal', subtotal)

iva=subtotal*0.16

total=iva
print('your total is', total)



