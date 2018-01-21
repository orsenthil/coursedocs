def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]


def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]


measurements = [5.0, 6.0, 7.0, 9.0, 10.0]
motion = [1.0, 1.0, 2.0, 1.0, 1.0]

measurement_sig = 4.0
motion_sig = 2.0

mu = 0.0
sig = 0.000000000000000000000001

for mean2, motion_mean2 in zip(measurements, motion):
    mu, sig = update(mu, sig, mean2, measurement_sig)
    mu, sig = predict(mu, sig, motion_mean2, motion_sig)

print([mu, sig])
