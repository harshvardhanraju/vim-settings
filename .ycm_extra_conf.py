a = int (raw_input())
Student = {}
for i in range(a):
    #Get the details of all the students
    details = raw_input()
    det = details.split()
    Student[det [0]] = det[1:]
name = raw_input()
marks = Student[name]
avg = (int(marks[0]) + int(marks [1]) +int(marks[2]))/3
#print the output
print "%.2f" %avg
