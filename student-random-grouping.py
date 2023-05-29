import random

students = ['Student1',
'Student2',
'Student3',
'Student4',
'Student5',
'Student6',
'Student7',
'Student8',
'Student9',
'Student10',
'Student11',
'Student12',
'Student13',
'Student14',
'Student15',
'Student16']

def make_random_groups(students, number_of_groups):
    
    #Shuffle list of students
    random.shuffle(students)
    
    #Create groups
    all_groups = []
    for index in range(number_of_groups):
        group = students[index::number_of_groups]
        all_groups.append(group)
    
    #Format and display groups
    for index, group in enumerate(all_groups):
        print(f"✨Group {index+1} ✨: {' / '.join(group)}\n")
        
make_random_groups(students, 4)

random.shuffle(students)
