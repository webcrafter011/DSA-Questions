# ‘Arr’ = {{1, 3}, {2, 4}, {3, 5}, {6, 7}}


def overlapIntervals(arr):
    arr.sort(key=lambda x: x[0])
    ans = []
    for i in range(len(arr)):
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])

    return ans
