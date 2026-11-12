a = int(input("Enter your age: "))

# If elif else ladder
if(a>=18):
    print("you are above the age of consent")
    print("good for you")

elif(a<0):
    print("you are entering an invaild negative age")

elif(a==0):
    print("you are entering o which is not a valid age")

else:
    print("you are bleow the age of consent")

print("End of program")

