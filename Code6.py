def string_frac(in_string):
    if "/" in in_string:
        nd= in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans= n/d
        return ans
    else:
        ans= float(in_string)
        return ans
def one_step_add():
    import random
    a= random.randint(-4,10)
    b= random.randint(2,24)
    print("x + ", a, "= ", b)
    ans= float(input("x = "))
    answer= b-a
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")
def one_step_subtract():
    import random
    a= random.randint(-19,-1)
    b= random.randint(2,24)
    print(a," + x = ", b)
    ans= float(input("x = "))
    answer= b-a
    if ans==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")
def one_step_mult():
    import random
    a= random.randint(1,11)
    b= random.randint(2,24)
    print(a, "x= ", b)
    ans_in= (input("x= "))
    answer= b/a
    if string_frac(ans_in)==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")
        
