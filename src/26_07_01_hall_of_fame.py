import heapq
from typing import List


def solution(k: int, score: List[int]) -> List[int]:
    """명예의 전당 문제 — 최소힙을 사용해 O(N log k)으로 최적화된 풀이

    Args:
        k: 명예의 전당에 유지할 최대 점수 개수
        score: 하루별 점수 리스트

    Returns:
        매일의 명예의 전당에서 가장 낮은 점수의 리스트

    시간복잡도: O(N log k)
    """
    heap: List[int] = []
    answer: List[int] = []

    for s in score:
        heapq.heappush(heap, s)
        if len(heap) > k:
            heapq.heappop(heap)
        # heap[0]은 현재 명예의 전당(크기 <= k)에서의 최솟값
        answer.append(heap[0])

    return answer
