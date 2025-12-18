# 📜 List Data Structure(리스트 자료 구조)

# When to use?
# - Grouping
# - Keep the order

# countries = ["South Korea", "USA", "Japan", "China"]
# print(countries)


# countries[2] = "Vietnam" # data structure이기 때문에 인덱스로 변경할 수 있음.
# print(countries)

# ---------------------------------------------------------------
# append

# element = "c"
# alphabets = ["b", element, "d"]
# print(alphabets)

# alphabets.append("e")
# print(alphabets)


# +=
# alphabets += ["f", "g"]
# print(alphabets) 

# insert
# alphabets.insert(0, "a")
# print(alphabets) 

# print(countries[0])
# print(countries[len(countries) -1 ]) # => 이걸 줄여서 -1로 표현
# print(countries[-1])


# pop 
# print(countries.pop())
# print(countries)

# print(countries.pop(0))

# ---------------------------------------------------------------
# 📜 list 사용시 접하는 Errors, nested list (에러와 중첩 리스트)


# alphabets = ['a', 'b', 'c']
# print(len(alphabets))
# print(alphabets[3])
# IndexError: list index out of range 


#Nested list (둥지, 리스트안에 리스트)
# alphabets = [['a', 'b'], ['c']]
# print(alphabets)

# ---------------------------------------------------------------
# 📜 for loop

# alphabets = ['a', 'b', 'c', 'd']

# for alphabet in alphabets: 
#     print(alphabet)
#     print(f"{alphabet} is char")


# for char in "South korea":
#     print(char)

# average value
# numbers = [1, 2, 3, 4]
# sum = 0

# for number in numbers: 
#     sum += number

# print(sum / len(numbers))


# max value
# numbers = [1, 2, 3, 4]
# max_num = 0

# for number in numbers:
#     if number > max_num:
#         max_num = number
    
# print(max_num)


# print(max(numbers))
# print(max(1, 5))


# sum = 0

# for i in range(1, 11):
#     sum += i

# odd number? 
# for i in range(1, 11, 2):
#     print(i)



# ---------------------------------------------------------------
# 📜 Function

# https://docs.python.org/3/library/functions.html

def my_func():
    print("Hello World")

my_func()

# 인자와 매개변수를 통해 원하는 내용 호출 가능
# country = 매개변수
def my_func(country):
    print("Hello", country)

# Korea는 인자
my_func(country="Korea")

# !함수를 정의할 때는 매개변수 
# !함수를 호출할 때는 인자


# ---------------------------------------------------------------
# 📜 Indentation
# spaces vs tab
    


# ---------------------------------------------------------------
# 📜 While Loop

# For 
# for action in list_of_actions:
# do action


# While
# while condition is True: 
# do action

value = 5
while value > 0:
    print(value)
    value -= 1
