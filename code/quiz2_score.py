def quiz2_score(a,b,c,d):
    average_a = (a + b) /2
    average_c = (c + d) / 2
    while average_a > average_c:
        return average_a
    else:
        return average_c

print(quiz2_score(1,3,5,7))