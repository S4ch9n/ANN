def mc_pitts_and(x1, x2):
    w1, w2    = 1, 1   # fixed weights
    threshold = 2       # fixed threshold

    z = x1*w1 + x2*w2  # weighted sum

    return 1 if z >= threshold else 0

# Test all combinations
for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(x1, x2, "→", mc_pitts_and(x1, x2))