from math import pi

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

x=int(input('Which Shape: '))
if x==1:
    b=float(input('Base: '))
    h=float(input('Height: '))
    a=0.5*b*h
    print('The area is ', a)
elif x==2:
    l=float(input('Length: '))
    w=float(input('Width: '))
    a=l*w
    print('The area is ', a)
elif x==3:
    s=float(input('Side: '))
    a=s**2
    print('The area is ', a)
elif x==4:
    r=float(input('Radius: '))
    a=pi*r**2
    print('The area is ', a)
elif x==5:
    print('Goodbye!')
else:
    print('Invalid choice. Please select a number between 1 and 5.')