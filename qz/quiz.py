from answer import correct_answer
from qustion import qustions
import random

def quiz():
    a=[]
    for i in range(20):
        b=random.choice(list(qustions.items()))
    
        if len(a)==10:
            break
    
        if b in a:
            continue
        else:
            a.append(b)

    score=0
    for i in a:
        print(i[1])
        d=input("please answer the questions")
        if d==correct_answer[i[0]]:
            score+=1
    print(f"your score is_____________________{score}_____________________")