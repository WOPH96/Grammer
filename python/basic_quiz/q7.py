
for i in range(1,51):
    with open("q7txt//{}주차".format(i),"w",encoding="utf8") as file:
        file.write("- {} 주차 주간보고 - \n".format(i))
        file.write("부서 : \n")
        file.write("이름 :  \n")
        file.write("업무 요약 : \n")