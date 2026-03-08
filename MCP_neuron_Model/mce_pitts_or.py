def mc_pitts_or(x1 , x2):
  w1,w2 = 1,1
  threshold = 1

  z = x1*w1 + x2*w2
  return 1 if z >= threshold else 0

for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(x1, x2, "→", mc_pitts_or(x1, x2))