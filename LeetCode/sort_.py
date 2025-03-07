# Meeting Room

def canAttendMeetings(intervals):
    # intervals를 시작 시간을 기준으로 정렬
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        # 이전 회의의 끝 시간이 다음 회의의 시작 시간보다 크면 겹침
        if intervals[i-1][1] > intervals[i][0]:
            return False
    
    return True

canAttendMeetings([[0,30],[5,10],[15,20]])