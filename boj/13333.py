import sys


def fun(n, arr):
    for k in range(n, -1, -1):
        cnt = 0

        #   k 이상인 수의 집합
        up = []

        for j in arr:
            if k <= j:
                cnt += 1
                up.append(j)

        if k <= cnt:
            # n - k 조건을 구하기 위한 집합 생성
            set_arr = set(arr)
            set_up = set(up)
            set_down = set_arr - set_up
            if len(set_down) <= k:
                print(k)
                return
    print(0)
    return


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
fun(n, arr)
