print("Use of assert statement")
def negativeCheck(num):
    assert num>=0 ,"Negative number is not allowed"
    return(num*num)

print(negativeCheck(-10))
