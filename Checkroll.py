data = [241, 34, 67, 89, 78, 56, 77, 88]
roll = int(input('enter number:'))

if roll not in data:
    data.append(roll)
    
else:
    print("already exists")

print(data)