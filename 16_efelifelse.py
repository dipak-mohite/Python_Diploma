marks = int(input("Enter Marks in percentage : "))
if marks<=35 and marks>0 :
    print("Fail")
elif marks<=60 and marks>35 :
    print("C Grade")
elif marks<=75 and marks>60 :
    print("B Grade")
elif marks<=100 and marks>75 :
    print("A Grade")
else :
    print("Enter Valid Marks [in range of 0-100]")
    