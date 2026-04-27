def operators_code():
    print("\n Python Operator Code \n")

    #Taking input from the user
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    #Arithmatic Operators
    print("\nArithmatic Operators \n")
    print("Addition(a+b)=", a+b)
    print("Subtraction(a-b)=", a-b)
    print("Multiply(a*b)=", a*b)
    print("Division(a/b)=", a/b)
    print("Modulous(a%b)=", a%b)
    print("exponent(a**b)=", a**b)

    #Comparision Operators
    print("\nComparison Operators \n")
    print("a==b :", a==b)
    print("a!=b :", a!=b)
    print("a>b :", a>b)
    print("a<b :", a<b)
    print("a>=b :", a>=b)
    print("a<=b :", a<=b)

    #Logical Operators
    print("\nLogical Operators \n")
    print("a>0 and b>0 :", a>0 and b>0 )
    print("a>0 or b>0 :", a>0 or b>0 )
    print("not(a>b) :", not(a>b))

    #Assignment Operators
    print("\nAssignment Operators \n")
    x=a
    print("Initial x:", x)
    x+=b
    print("x+=b:", x)
    x-=b
    print("x-=b:", x)
    x*=b
    print("x*=b:", x)
    x//=b
    print("x//=b:", x)

    print("\nBitwise Operators \n")
    print("a & b:", a & b)
    print("a | b:", a | b)
    print("a ^ b:", a ^ b)
    print("~a:", ~a)
    print("a << 1:", a << 1)
    print("a >> 1:", a >> 1)



operators_code()
