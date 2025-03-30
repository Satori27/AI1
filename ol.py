INF = 1e18

def solve(v, dist):
    a = -1 / 2

    D = v * v - 4 * a * -dist
    if D < 0:
        return INF
    time = v - D ** (1 / 2)
    return time

def is_possible(left, dist, points, usk):
    speed = usk
    for i in range(1, len(points)):
        time = solve(speed, points[i] - points[i - 1])
        left -= time
        speed -= time
        speed += usk
        if (left < 0 or speed < 0):
            return False
    time = solve(speed, dist - points[-1])
    left -= time
    if left > 0:
        return True
    else:
        return False
        

L, n, t = list(map(int, input().split()))
boosts = list(map(int, input().split()))

l = 0
m = 0
r = INF
answer = INF

while (abs(l - r) > 1e-8):
    m = (r + l) / 2

    poss = is_possible(t, L, boosts, m)

    if (poss):
        r = m
        answer = m
    else:
        l = m

print(answer)