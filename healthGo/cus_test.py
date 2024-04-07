import time


def solution1(matrix):
    answer = [[]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j])


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# solution1(matrix)


def solution2(nums):
    # 점프한 횟수
    jumped_cnt = 0
    # 현재 위치
    location = 0
    while location + 1 == len(nums):
        print("현재위치: ", location)
        # 현재 위치에 징검다리 숫자로 점프할 횟수 지정
        jump_cnt = nums[location]

        # 점프를 했는데 마지막 징검다리 n번째를 초과할 경우 -1후 다시 루프
        if location + jump_cnt > len(nums):
            print("점프했을 때 징검다리 초과")
            location -= 1
            continue
        # 다음 점프할 숫자가 0이면 현재위치 증가 안하고 -1 , 점프횟수 +1
        if nums[location + jump_cnt] == 0:
            print("다음 징검다리 숫자 0")
            location -= 1
            jumped_cnt += 1
            continue
        else:  # 아니면 점프
            print(f"{jump_cnt}만큼 점프")
            location += jump_cnt  # n번 점프했을 때 위치
            jumped_cnt += 1
        if location + 1 == len(nums):
            print("도착")
            print("점프한 횟수 : ", jumped_cnt)
            break
    return jumped_cnt


nums = [7, 8, 9, 1, 1, 4, 0, 7, 2, 1, 5, 8, 0, 1]
solution2(nums)
# print(len(nums))
