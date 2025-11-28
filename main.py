
# 🚀 print 사용하기  

# print("Hello") 

# print("Hello", " ", "Python")

# print({print("Hello", " ", "Python")})

# print([1, 2, 3, 4, 5])

# print((1, 2, 3, 4, 5))


# print(42)
# print(3.14)
# print(False)

# print('home', 'user','documents', sep= `/`)



# print("What is wrong here?)

# print(("Somenting wrong hree")

# ---------------------------------------------------------------

# ✅ Input 명령어 사용  

# name = input("What is your name?")
# print("Here is my name, " + name) 

# ---------------------------------------------------------------


# 🔧 변수 사용하기 

# x, y = 10, 20 

# print(x)
# print(y)

# ---------------------------------------------------------------


# 🧾 primitive data type 

#- Intergers
# profile_number = 2030
# print(profile_number)

# - Floats
#     score = float(100.0)
#     print(score)

# - Boolean(True or False) 
#     is_active = True 

# - String(str)

# teacher_name = "John Doe"
# course_name = 'Python'
# lecture_name = """
# Cisca
# Oladipo
# """
# print(lecture_name)

# ---------------------------------------------------------------


# 📃 String subscript  
# print(teacher_name[3]) # 특정한 위치에 있는 문자를 찾아내는 것. 

# print(teacher_name[len(teacher_name)-1])


# check object type
# print(type(profile_number))

# print(type(teacher_name))




# ---------------------------------------------------------------



# ❌ Type error (자료형 타입 에러 처리하기)
# print("Hello" + 1 + "World") # ERR TypeError: can only concatenate str (not "int") to str

# print(type(1)) 
# print(type(str(1)))

# print("Hello " + str(1) + " World")


# ---------------------------------------------------------------

# 🔢 Mathmatical operation (수학연산자)
# print(3 + 1)

# float
# print(3 / 2) # = 1.5
# print(3 / 1) # = 3.0



# floor division 

# print(3 // 2) # = 1
# print( 7 // 2) # = 3

# Exponents
# print(3**3)


# Modulo
# print(60 % 13) # = 8 

# print(12.5 % 5.5) # = 1.5



# PEMDAS
# Parentheses () 
# Exponents
# Multiplication
# Division
# Addition
# Subtraction
# And Left to Right


# sum = 0
# sum += 1 # sum = sum + 1  
# print(sum)


# ---------------------------------------------------------------


# 📜 f-string 

# old style

name = "Kim"
age = 30 
# print("Hello, %s." % name) # %s는 문자열 값을 위한 플레이스 홀더  / %연산자는 문자열 뒤에 오며, 플레이스홀더를 대체할 값을 지정
# =>  이 방법은 여러 값을 삽입하거나 특정 형식에 (숫자의 소수점 자릿수)를 지정해야 할 때 유용했지만 현재 Python에서는 덜 선호가 됩니다.  

# print("Hello, %s, I am %s" % (name, age)) # 문제는 이것이 많아지면 순서가 헷갈리고 가독성이 심히 안 좋아진다.

# Python 2.6
# print("Hello, {}. I am {}.".format(name, age))
# print("Hello, {1}. I am {0}.".format(age, name))


# 딕셔너리
person = { 'name': 'Kim', 'age' : 17}
print("Hello, {name}. i am {age}.".format(name=person['name'], age=person['age']))

print("Hello, {name}. I am{age}.".format(**person))

