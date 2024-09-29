import random
again="Y"
while again=="Y" or again=="y":
    b=random.randint(1,6)
    if(b==1):
        print("   \n . \n   ")
    elif(b==2):
        print(".  \n   \n  .")
    elif(b==3):
        print(".  \n . \n  .")
    elif(b==4):
        print(". .\n   \n. .")
    elif(b==5):
        print(". .\n . \n. .")
    else:
        print(". .\n. .\n. .")
    again=input("Do you want to play agin(Y/N):")
