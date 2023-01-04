a=[]
b=[]
import datetime
instruction=int(input('\nEnter 1 to entry:'
                      '\nEnter 2 to exit:'))

if instruction== 1:
    x=(input('Enter your name:'))
    y=datetime.datetime.now()
    print(y)
    a.append(x)
    a.append(y)
    print('You have successfully enter')
elif instruction== 2:
    x=(input('Enter your name:'))
    print('You can go')
else:
    ()
    
    
