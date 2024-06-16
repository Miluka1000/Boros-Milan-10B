n = int(input("Adj meg egy számot: "))
while n < 2 or n > 12:
    n = int(input("Adj meg egy számot: "))
fakoriális = 1
for i in range(1,n + 1):
    fakoriális = fakoriális * i
print(f"{fakoriális}")