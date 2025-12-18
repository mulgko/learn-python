# hanman
# Here is the word []
# Guess the char?
# [b,_,t,m,a,_]
# [b,a,t,m,a,n]


# words = "lemon"
# def hang_fnc(n): 
#     wordArry = []
#     answerArry = []

#     for word in words: 
#         wordArry.append(word)

#     wordArryNum = len(wordArry)

#     for _ in range(wordArryNum):
#         answerArry.append('_')

#     if n in wordArry:
#         index = wordArry.index(n)
#         answerArry[index] = n

#     print(answerArry)

# hang_fnc(n='m')



# solution
question = list("banana")
lst = []

for i in range(0, len(question)):
    lst.append('_')

print("Here is the word")
print(lst)
num_of_try = 10

while True:
    char = input("Guess the char?")
    i = 0
    for elem in question:
        if elem == char:
            lst[i] = char
            i += 1
        print(lst)

        if "_" not in lst: 
            print("You won")
            break
        if num_of_try < 1:
            print("You lost")
            break
        num_of_try -= 1


