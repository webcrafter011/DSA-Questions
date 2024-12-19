# To Find: No of subarrays with k xor(^)

array = [4, 2, 2, 6, 4]
k = 6

count = 0
xr = 0
dict = {0: 1}
for i in range(len(array)):
    xr = xr ^ array[i]
    if xr ^ k in dict:
        count += dict[xr ^ k]
    if xr in dict:
        dict[xr] += 1
    else:
        dict[xr] = 1

print(count)