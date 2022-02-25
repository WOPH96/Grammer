
def std_weight(height, gender):
    if gender == "남":
        return height*height*22
    else:
        return height * height *21

h = input("키 입력(cm): ")
g = input("성별 입력(남/여) : ")

print("키 {}cm 남자의 표준 체중은 {:.2f}kg 입니다.".format(h,std_weight(float(h)/100,g)))