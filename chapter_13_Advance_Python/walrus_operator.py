# := is called walrush operator
l = [1, 2, 3, 4, 5, 6]
if (m := len(l)) > 5:
    print(m)

newList = [doubleValue for value in l if (doubleValue := 2*value) > 5]
print(newList)