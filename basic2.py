students = [
    {"name": "Ali",   "study_hours": 8, "sleep_hours": 7, "practice_tests": 5},
    {"name": "Sara",  "study_hours": 2, "sleep_hours": 4, "practice_tests": 1},
    {"name": "Ravi",  "study_hours": 5, "sleep_hours": 6, "practice_tests": 3},
    {"name": "Mia",   "study_hours": 1, "sleep_hours": 3, "practice_tests": 0},
]

w_study    = 0.9
w_sleep    = 0.1
w_practice = 0.9
bias       = -5

for student in students:
    score = (student["study_hours"]    * w_study) + \
            (student["sleep_hours"]    * w_sleep) + \
            (student["practice_tests"] * w_practice) + \
            bias

    result = "PASS" if score > 5.0 else "FAIL"
    print(f"{student['name']:<6}  Score: {score:.1f}  →  {result}")
