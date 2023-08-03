def check_score(x):
    if x >= 50:
        print("You just passed")
    elif x > 100:
        print("invalid score")
    elif x <= 0:
        print("Invalid score")
    else :
        print("You failed")
check_score(50)
check_score(49)
check_score(0)
check_score(-1)
check_score(51)
check_score(100)

