def inversion_by_merge_sort(a):

    if len(a)==1:
        return a,0

    mid = len(a)//2
    left,left_count_inversion = inversion_by_merge_sort(a[:mid])
    right,right_count_inversion = inversion_by_merge_sort(a[mid:])

    i = 0
    j = 0
    c=[]
    count_inversion = left_count_inversion+right_count_inversion

    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            c.append(left[i])
            i+=1

        elif left[i]>right[j]:
            c.append(right[j])
            j+=1
            count_inversion += (len(left)-i)

        else:
            c.append(left[i])
            i+=1

    c += left[i:]
    c += right[j:]

    return c,count_inversion

n = int(input())
a = list(map(int, input().split()))
print(inversion_by_merge_sort(a)[-1])