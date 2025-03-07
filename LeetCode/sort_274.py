# H-Index (논문)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 입력된 인용 수 리스트가 비어있으면 H-Index는 0이므로 0을 반환합니다.
        if not citations:
            return 0
        
        # 인용 수 리스트를 내림차순으로 정렬합니다.
        # 이렇게 하면 인용 수가 많은 논문부터 비교하여 H-Index를 계산하기 쉬워집니다.
        citations.sort(reverse=True)
        
        # 정렬된 인용 수 리스트를 순회하면서 H-Index를 계산합니다.
        for idx, citation in enumerate(citations):
            # 현재 논문의 순서(idx + 1)가 해당 논문의 인용 수보다 클 경우 H-Index는 현재 순서입니다.
            if idx + 1 > citation:
                return idx
        
        # 모든 논문이 순서(idx + 1) 이상의 인용 수를 가지고 있는 경우,
        # 전체 논문 수(idx + 1)가 H-Index가 됩니다.
        return idx + 1