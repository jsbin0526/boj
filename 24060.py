def merge_sort(a, p, r): # A[p..r]을 오름차순 정렬한다.
    print(p, r)
    if p < r:
        q = (p + r + 1)//2 # q는 p, r의 중간 지점
        merge_sort(a, p, q) # 전반부 정렬
        merge_sort(a, q + 1, r) # 후반부 정렬
        merge(a, p, q, r) # 병합


# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(a, p, q, r):
    i, j, t = p, q + 1, 0
    tmp = [0 for _ in range(r+1)]
    while (i <= q and j <=r):
        if (a[i] <= a[j]):
            tmp[t] = a[i] # tmp[t] <- A[i]; t++; i++;
            t += 1
            i += 1
        else:
            tmp[t] = a[j] # tmp[t] <- A[j]; t++; j++;
            t += 1
            j += 1
    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp[t] = a[i]
        t += 1
        i += 1
    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp[t] = a[j]
        t += 1
        j += 1
    i, t = p, 0
    while i <= r:  # 결과를 A[p..r]에 저장
        a[i] = tmp[t] 
a = [4, 5, 1, 3, 2]
merge_sort(a, 0, 4)
print(a)