import math

//N = 정부의 수
N = int(input())

//M = 각 정부의 예산
M = input()
M = list(map(int, M.split()))

//이분 탐색을 위해 데이터 정렬
M.sort()


//이분 탐색 시 값을 바꿔주기 위한 데이터 그릇 만들기
box = []

for i in range(N) :
    box.append(M[i])


//총 예산

budget = int(input())

// 1. 총 예산이 각 정부의 예산의 합보다 작거나 같으면 그냥 큰 예산  출력

if sum(box) <= budget :
    print(max(box))

// 2. 아니면 이분 탐색으로 적정 값 찾기
else :
    // start, mid, limit 3가지 축 설정
    start = 0
    limit = M[len(M)-1]
    mid = math.floor((start + limit) / 2)

    // 이분 탐색 시작(각 정부의 예산의 합이 총 예산과 같으면 끝
    // mid 가 start와 같거나 mid 가 limit과 같으면 끝
    while sum(box) != budget and mid != start and mid != limit :
        for i in range(N) :
            if M[i] < mid :
                box[i] = M[i]
            else :
                box[i] = mid
        if sum(box) < budget :
            start = mid
            mid = math.floor((start + limit) / 2)
        else :
            limit = mid
            mid = math.floor((start + limit) / 2)
    print(max(box))
