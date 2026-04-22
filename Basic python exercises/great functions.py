def get_sorted_n_grades(grade_list, n, top=True):

    sorted_grades = sorted(grade_list, reverse=top)
    if len(sorted_grades) < n:
        return sorted_grades
    return sorted_grades[:n]

grades=[40,30,60,20,43,86,78,30,40,75,32]
print(get_sorted_n_grades(grades, 6))