inp = [1.2, 4.7, 9.9, 3]

w1 = [3.1, 2.2, 7.9, 2]
w2 = [3., 2.2, 6.9, -1.1]
w3 = [3.1, 4.2, 1.9, -6.4]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [inp[0] * w1[0] + inp[1] * w1[1] + inp[2] * w1[2] + inp[3] * w1[3] + bias1,
          inp[0] * w2[0] + inp[1] * w2[1] + inp[2] * w2[2] + inp[3] * w2[3] + bias2,
          inp[0] * w3[0] + inp[1] * w3[1] + inp[2] * w3[2] + inp[3] * w3[3] + bias3]
print(output)
