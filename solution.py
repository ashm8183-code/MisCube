from collections import deque

s = input().replace(" ", "")

solved = list("yyyyrrrrwwwwoooobbbgggg")

stickers = []

for x, z in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
    stickers.append(((x, 1, z), (0, 1, 0)))

for x, y in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
    stickers.append(((x, y, 1), (0, 0, 1)))

for x, z in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
    stickers.append(((x, -1, z), (0, -1, 0)))

for x, y in [(1, -1), (-1, -1), (1, 1), (-1, 1)]:
    stickers.append(((x, y, -1), (0, 0, -1)))

for y, z in [(1, -1), (1, 1), (-1, -1), (-1, 1)]:
    stickers.append(((-1, y, z), (-1, 0, 0)))

for y, z in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
    stickers.append(((1, y, z), (1, 0, 0)))


def rotate(pos, axis, direction):

    x, y, z = pos

    if axis == "x":
        if direction == 1:
            return (x, -z, y)
        return (x, z, -y)

    if axis == "y":
        if direction == 1:
            return (z, y, -x)
        return (-z, y, x)

    if direction == 1:
        return (-y, x, z)

    return (y, -x, z)


place = {}

for i in range(24):
    place[stickers[i]] = i


moves = []

faces = [
    ("y", 1),
    ("y", -1),
    ("z", 1),
    ("z", -1),
    ("x", -1),
    ("x", 1)
]

for axis, layer in faces:

    for direction in [1, -1]:

        move = list(range(24))

        for i in range(24):

            pos, normal = stickers[i]

            if axis == "x":
                value = pos[0]
            elif axis == "y":
                value = pos[1]
            else:
                value = pos[2]

            if value == layer:

                new_pos = rotate(pos, axis, direction)
                new_normal = rotate(normal, axis, direction)

                new_i = place[(new_pos, new_normal)]

                move[new_i] = i

        moves.append(move)


corners = {}

for i in range(24):

    pos = stickers[i][0]

    if pos not in corners:
        corners[pos] = []

    corners[pos].append(i)

corners = list(corners.values())


def check(state):

    wrong = []

    for i in range(24):
        if state[i] != solved[i]:
            wrong.append(i)

    if len(wrong) != 3:
        return None

    for corner in corners:

        if set(corner) == set(wrong):

            colors = []

            for i in corner:
                colors.append(state[i])

            return "".join(sorted(colors))

    return None


queue = deque()
queue.append((tuple(s), 0))

visited = set()
visited.add(tuple(s))

while queue:

    state, depth = queue.popleft()

    result = check(state)

    if result is not None:
        print(result)
        break

    if depth == 4:
        continue

    for move in moves:

        new_state = []

        for i in range(24):
            new_state.append(state[move[i]])

        new_state = tuple(new_state)

        if new_state not in visited:

            visited.add(new_state)
            queue.append((new_state, depth + 1))
