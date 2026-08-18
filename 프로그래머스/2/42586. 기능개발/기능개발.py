def solution(progresses, speeds):
    answer = []
    
    days = []
    
    for progress, speed in zip(progresses, speeds):
        remain = 100 - progress
        
        day = (remain + speed - 1) // speed
        days.append(day)
    
    deploy_day = days[0]
    count = 1
    
    for i in range(1, len(days)):
        if days[i] <= deploy_day:
            count += 1
        else:
            answer.append(count)
            deploy_day = days[i]
            count = 1
    
    answer.append(count)
    
    return answer