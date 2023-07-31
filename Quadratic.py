import math
a=float(input('Enter a:'))
b=float(input('Enter b:'))
c=float(input('Enter c:'))

if a==0:
    print("Input correct quadratic equation")
else:
    dis=b*b-4*a*c
    number=math.sqrt(abs(dis))
    den=2*a

    if dis>0:
        print("real and different roots")
        print((-b+numer)/(den))
        print((-b-numer)/(den))
    elif dis==0:
        print("real and same root")
        print(-b/(den))
    else:
        print("Complex Roots or imaginary roots")
        print(-b/(den),"+i",number)
        print(-b/(den),"-i",number)
