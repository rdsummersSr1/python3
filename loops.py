def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """
    u_student_scores = []
    for score in student_scores:
        u_student_scores.append(round(score))
    return u_student_scores


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    count = 0
    print(student_scores)
    fail_count = 0
    for score in student_scores:
         if score <= 40 :
            fail_count += 1
    return fail_count
    




def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    above_threshold = []
    for score in student_scores:
        if score >= threshold:
            above_threshold.append(score)
    return above_threshold


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:


             41 <= "D" <= 55 14
             56 <= "C" <= 70 14
             71 <= "B" <= 85 14
             86 <= "A" <= 100 14
    """
    thresholds = []
    intervals = []
    failing = 41
    # 100 - 41 = 59  59 / 4 = 15
    # 100 41 56 71 86   
    # 97 41 55 69 83 97-41 56/4 14
    # 85 41 52 63 74 85 85-41 44/4 11
    # 92 41 54 67 80 92-41 51/4 13
    # 81 41 51 61 71 81-41 40/4 10
    interval = 0
    interval = round((highest-failing) /4 ) 
    intervals.append(failing)
    intervals.append(failing + interval*1)
    intervals.append(failing + interval*2)
    intervals.append(failing + interval*3)
    return intervals       




def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format 
    ["<rank>. <student name>: <score>"].
     [82], ['Betty']), 
    ['1. Betty: 82']
    [88, 73], ['Paul', 'Ernest']), 
    ['1. Paul: 88', '2. Ernest: 73']
    """
    rank = 1
    stud_rank = []
    num_students = len(student_scores)
    for i in range(0, num_students):
        name = student_names[i]
        score = student_scores[i]
        stud_rank.append(f"{rank}. {name}: {score}")
        rank += 1
    return stud_rank
  
 
       
    
def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
  #   
    first = []
    student_names = []
    score = []
    print (student_info)
    for name in student_info:
        print('1', 'name', name[0])
        print ('2','score',name[1])
        print(type(name[1]))
        score = int(name[1])
        print(type(score))
        if (score == 100 ):
            print('3', score)
            print(name)
            return name
    return first