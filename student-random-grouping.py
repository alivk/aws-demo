import random
import time

students = [
    'Student1', 'Student2', 'Student3', 'Student4', 'Student5',
    'Student6', 'Student7', 'Student8', 'Student9', 'Student10',
    'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16'
]

def make_random_groups(students, number_of_groups):
    # Shuffle list of students
    random.shuffle(students)
    
    # Create groups
    all_groups = []
    for index in range(number_of_groups):
        group = students[index::number_of_groups]
        all_groups.append(group)
    
    # Format and display groups
    for index, group in enumerate(all_groups):
        print(f"✨Group {index+1} ✨: {' / '.join(group)}\n")

def show_loading(duration=10):
    for i in range(duration):
        print(f"Creating AWS JAM groups in progress... {int((i/duration)*100)}%", end='\r')
        time.sleep(1)
    print("Creating AWS JAM groups completed... 100%")
    print("-----------------------------------------")
    print("\n")

number_of_groups = int(input("How many AWS JAM groups do you need? "))

# Show loading progress for 10 seconds
show_loading()

make_random_groups(students, number_of_groups)
