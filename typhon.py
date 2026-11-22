def add(m, u):
    return m + u

m = int(input("1st number: "))
u = int(input("2nd number: "))

result = add(m, u)
print(f"SUM: {result}")
print()

def sub(m, u):
    if m > u:
        return m - u
    else:
        return TypeError

m = int(input("1st number: "))
u = int(input("2nd number: "))

result = sub(m, u)
print(f"VALUE: {result}")

print("VISCA BARCA Y VISCA CATALUNYA")