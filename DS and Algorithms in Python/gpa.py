def gpa_calc(input):
    grades = {
        "A+": 4.0, "A": 4.0, "A-": 3.67,
        "B+": 3.3, "B": 3.0, "B-": 2.67,
        "C+": 2.3, "C": 2.0, "C-": 1.67,
        "D+": 1.3, "D": 1.0, "F": 0.0
    }

    grade_sum = 0
    grade_count = 0

    for i in input:
        if input == []:
            return False

        elif i not in grades:
            return False

        else:
            grade_sum += grades[i]
            grade_count += 1

    if grade_count > 0:
        print("Overall GPA is : {0:.3}".format(grade_sum / grade_count))


gpa_calc(["A", "B+", "C+"])
