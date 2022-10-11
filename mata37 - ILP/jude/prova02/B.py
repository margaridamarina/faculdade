# for i in range(7):
#     for j in range(i, 7):
#         print("#", end="")
#     print()

# for i in range(7):
#     for j in range(i+1):
#         print("#", end="")
#     print()

a="#"
b=">"

P=int(input())
j=1

for k in range(P-1, -1, -1):
    print((k*b)+(j*a))
    j=j+1