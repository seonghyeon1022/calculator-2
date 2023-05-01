def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def remainder(x,y):
    return x % y

def factorial(x):
    fact = 1
    for i in range(1, x+1, 1):
        fact *= i
    return fact

print("수정한 계산기!")


print("사칙연산을 선택 하세요.")
print("1.더하기")
print("2.빼기")
print("3.곱하기")
print("4.나누기")
print("5.나머지 구하기")
print("6.팩토리얼")

choice = input("선택 하세요(1/2/3/4/5/6):")



if choice == "1":
    num1 = int(input("첫번째 숫자 : "))
    num2 = int(input("두번째 숫자 : "))
    print(num1,"+",num2,"=", add(num1,num2))
    
elif choice == "2":
    num1 = int(input("첫번째 숫자 : "))
    num2 = int(input("두번째 숫자 : "))
    print(num1,"-",num2,"=", subtract(num1,num2))
          
elif choice == "3":
    num1 = int(input("첫번째 숫자 : "))
    num2 = int(input("두번째 숫자 : "))
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == "4":
    num1 = int(input("첫번째 숫자 : "))
    num2 = int(input("두번째 숫자 : "))
    print(num1,"/",num2,"=", divide(num1,num2))
                        
elif choice == "5":
    num1 = int(input("첫번째 숫자 : "))
    num2 = int(input("두번째 숫자 : "))
    print(num1,"%",num2,"=", remainder(num1,num2))
                                
elif choice == "6":
    num1 = int(input("첫번째 숫자 : "))
    print(num1,"! =", factorial(num1))

else:
    print("잘못된 선택")

