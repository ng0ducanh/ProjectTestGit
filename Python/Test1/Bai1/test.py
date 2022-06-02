a = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num2 = float(num)
        a.append(num2)
    except:
        print("Sai")
        continue

print("Maximum is", max(a))
print("Minimum is", min(a))