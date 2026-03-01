dishes = [
    {"name": "Pizza",  "freshness": 9, "taste": 8, "presentation": 8},
    {"name": "Burger", "freshness": 9, "taste": 8, "presentation": 7},
    {"name": "Salad",  "freshness": 5, "taste": 5, "presentation": 6},
    {"name": "Stale",  "freshness": 1, "taste": 2, "presentation": 1}    
]

w_freshness    = 0.9
w_taste        = 0.8
w_presentation = 0.6

bias = 1

for dish in dishes:
    score = (dish["freshness"]    * w_freshness) + \
            (dish["taste"]        * w_taste) + \
            (dish["presentation"] * w_presentation) + \
            bias

    if score > 14:
        result = "Good"
    elif score > 8:
        result = "Average"
    else:
        result = "Bad"

    print(f"{dish['name']:<8}  Score: {score:.1f}  →  {result}")