# 1st to think, password should be a string value which include numbers and alphabets .etc
# its a variable, length , lowercase, uppercase
# random module must include this project
# for loops since we will going to repeat

from random import randint

password = ""
for i in range(10):
    i = chr(randint(65, 90))
# 65 is ASCII value for A, thus 90 is Z (uppercase)
# str() function is to return the string version of the object
    password = str(password) + i
print(password)

# for here I demonstrate another version of ASCII which include for than alphabets

password_2 = ""
for i in range(5):
    i = chr(randint(0, 127))
    for j in range(5):
        j = chr(randint(65, 90)).lower()
    password_2 = str(password_2) + i +j
print(password_2)
