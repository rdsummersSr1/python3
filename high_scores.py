def latest(scores):
    return scores[-1]




def personal_best(scores):
    print(max(scores))
    return max(scores)




def personal_top_three(scores):
    scores1 = ''
    scores1 = sorted(scores, reverse=True)
    print('1',sorted(scores, reverse=True))
    i = 0
    result =scores1[:3]
    return result
    for score in scores1:
        i+=1
        if i == 1:
           print('1',score)
           result += str(score) 
        if i > 1 and i <= 3:
           print('2',score)
           result += ', ' + str(score) 
    print('2',result)
    return str(result)