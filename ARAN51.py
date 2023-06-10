
def lagrange(x, y):
    p = ""
    for i in range(len(x)):
        a = ""
        b = 1
        if i != 0:
            p = p + " + "
        for j in range(0, i):
            a = a + "(x - ({})) * ".format(x[j])
            b = b * (x[i] - x[j])
        for j in range(i + 1, len(x)):
            a = a + "(x - ({})) * ".format(x[j])
            b = b * (x[i] - x[j])
        p = p + "({}) * ".format(y[i]) + "(" + a + "(1) / ({}))".format(b)
    return p


xi = [0.855687260013478, -4.981911943628653, 5.353393106241569, -1.246552618391358, -5.966205145742132,
      -4.61079639108801, 1.4471739275027424, 1.9315701805685155, -5.038549559937583, 2.02333620328654]
sinxi = [0.7550217306390838, 0.9638980274005456, -0.8014956942367758, -0.9478919459260277, 0.31169859292053964,
         0.9948439098799354, 0.9923684776878301, 0.9356239347296401, 0.9472795050334992, 0.899339440427479]
print(lagrange(xi, sinxi))