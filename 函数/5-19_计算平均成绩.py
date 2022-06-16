def avergescore(score):
    scoresum=0.0
    for n in score:
        scoresum+=n
    return  scoresum/len(score)
stulsore=[99,80,70]
stu2sore=[77,85]
print("三科成绩的平均的分是"+str(avergescore(stulsore)))
print("两科成绩的平均分是"+str(avergescore(stu2sore)))