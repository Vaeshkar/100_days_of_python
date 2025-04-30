student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

# # Sum() version
# total_score = sum(student_scores)
# print(total_score)

# # Naive version
# sum = 0
# for score in student_scores:
#     sum += score
#
# print(sum)

# Headline
print("Testing the min() Versions")

# Min() version
print("min() version:", min(student_scores))

# Min Naive version
min_score = student_scores[0]
for num in student_scores:
    if num <= min_score:
        min_score = num
print(f"min() naive: {min_score}\n")

# Headline
print("Testing the max() Versions")

# Max() version
print("max() version:", max(student_scores))

# Max Naive version
max_score = student_scores[0]
for num in student_scores:
    if num >= max_score:
        max_score = num
print(f"min() naive: {max_score}")
