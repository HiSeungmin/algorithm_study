# Top K Frequent Elements

def topKFrequent(nums, k):
    # 숫자의 빈도를 저장할 딕셔너리를 생성합니다.
    num_dict = defaultdict(int)

    # nums 리스트의 각 숫자의 빈도를 계산합니다.
    for num in nums:
        num_dict[num] += 1
    
    # 빈도를 키로 하고, 해당 빈도를 가진 숫자들을 값으로 저장할 딕셔너리를 생성합니다.
    frecuent_dict = defaultdict(list)

    # 각 숫자와 해당 빈도를 frecuent_dict에 저장합니다.
    for num, frec in num_dict.items():
        frecuent_dict[frec].append(num)
    
    # 결과를 저장할 리스트를 초기화합니다.
    result = []

    # 빈도(key)를 기준으로 내림차순으로 정렬하여 가장 높은 빈도부터 처리합니다.
    for freq_key in sorted(frecuent_dict.keys(), reverse=True):
        num_list = frecuent_dict[freq_key]  # 현재 빈도의 숫자 리스트를 가져옵니다.

        # 결과 리스트에 숫자들을 추가합니다.
        result += num_list

        # 남아야 하는 K값에서 현재 추가한 숫자들의 개수를 뺍니다.
        k -= len(num_list)

        # 만약 K가 0이 되면, 원하는 만큼의 숫자를 찾았으므로 반복문을 종료합니다.
        if k == 0:
            break

    # 결과 리스트를 반환합니다.
    return result

print(topKFrequent([1,1,1,2,2,3],2))