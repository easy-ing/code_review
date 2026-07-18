def solution(number):
    """삼총사 문제 — 투포인터 기반 최적화로 O(N^2) 시간복잡도

    Args:
        number: 정수 리스트

    Returns:
        세 수의 합이 0이 되는 서로 다른 인덱스 조합의 개수

    구현 설명:
        정렬 후 고정 포인터(i)와 양쪽 포인터(left, right)를 사용합니다.
        합이 0일 때 같은 값들의 중복 처리를 통해 인덱스 조합을 정확히 계산합니다.
    """
    number.sort()
    n = len(number)
    count = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            s = number[i] + number[left] + number[right]
            if s == 0:
                # 같은 값들 처리
                if number[left] == number[right]:
                    m = right - left + 1
                    count += m * (m - 1) // 2
                    break
                else:
                    cntL = 1
                    cntR = 1
                    while left + 1 < right and number[left] == number[left + 1]:
                        cntL += 1
                        left += 1
                    while right - 1 > left and number[right] == number[right - 1]:
                        cntR += 1
                        right -= 1
                    count += cntL * cntR
                    left += 1
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1

    return count
