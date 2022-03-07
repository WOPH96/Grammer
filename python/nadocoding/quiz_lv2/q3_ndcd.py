#영화예매 시스템

# for i in range(1,21):
#     if i%2 == 1:
#         print("A" + str(i), end=" ")

for i in range(1,21)[::2]: # 2칸씩 건너뜀 slicing
    print("A" + str(i), end=" ")