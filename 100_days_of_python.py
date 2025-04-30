# # multiple func with parameters
# def greet_with(name, location):
#     print(f"Hello {name}.")
#     print(f"What is it like in {location}?")

# greet_with("test", "another")

# #############
# # True love game

# def calculate_love_score(name_one:str, name_two:str):
    
#     names = name_one + name_two
#     count_true = 0
#     count_love = 0
#     for char in names.lower():
#         if char in "true":
#             count_true += 1
#     for char in names.lower():
#         if char in "love":
#             count_love += 1
#     print(f"count_true {count_true}")
#     print(f"count_love {count_love}")
#     final_score = int(f"{count_true}{count_love}")
#     print(type(final_score))
#     return final_score


# print(calculate_love_score("Verena Kniesmeijer", "Dennis van Leeuwen")) #output: 1212
# print(calculate_love_score("Angela Yu", "Jack Bauer")) #output: 53
# print(calculate_love_score("Kanye West", "Kim Kardashian")) #output: 42


################
# Grading Program

'''
Scoring criteria:
scores 91 - 100: 'Outstanding'
scores 81 - 90: 'Exceeds Expectations'
scores 71 – 89: 'Acceptable'
scores 70 or lower: 'Fail'
'''

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {
    
}

for student, scores in student_scores.items():
    if 91 <= scores <= 100:
        student_grades[student] = 'Outstanding'
    elif 81 <= scores <= 90:
        student_grades[student] = 'Exceeds Expectations'
    elif 71 <= scores <= 80:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'
        
print(student_grades)



