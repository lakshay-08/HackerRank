"""
Find The Percentage

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    mark=list(student_marks[query_name])
    c=0
    s=0
    for i in mark:
     c+=1
     s=s+i
    avg=s/c    
    print("{:.2f}".format(avg))