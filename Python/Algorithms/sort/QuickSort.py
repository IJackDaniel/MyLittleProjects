def srt(arr):
    if len(arr) == 1:
        return arr
    elif len(arr) == 0:
        return []
    else:
        num = arr[0]
        less = [i for i in arr if i < num]
        more = [j for j in arr if j > num]
        return srt(less) + srt([num]) + srt(more)
