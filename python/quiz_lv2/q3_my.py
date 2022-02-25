#영화예매 시스템
seats =[]
for i in range(1,21):
    seats.append(f"A{i}")

print(seats)

for seat in seats:
    num = int(seat.lstrip("A"))
    if num % 2 == 1:
        print(seat,end=" ")