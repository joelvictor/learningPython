
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
# for s in word:
#     print(s)

# Write a while loop that does the same thing!
# count = 0
# while count < len(word):
#     print(word[count])
#     count+=1


#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
# count=100
# while count <= 140:
#     if count%2==0:
#         print(count)
#     count+=1



# Write a for loop that does the same thing (with range())
# for i in range(100, 141 ):
#     if i%2==0:
#         print(i)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
passphrase = "sillygoose"
password = input("Insert the write password: ") 
while password != passphrase:
    password = input("Insert the write password: ") 
