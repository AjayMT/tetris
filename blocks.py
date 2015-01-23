
class Matrix:
    def __init__(self, w_or_arr, h=None):
        self._data = []
        if type(w_or_arr) is list:
            self._populate(w_or_arr)
            return

        self.w, self.h = w_or_arr, h

        for i in range(self.w * self.h):
            self._data.append(None)

    def __getitem__(self, i):
        x = i % self.w if self.w > 0 else 0
        y = i / self.w if self.w > 0 else 0

        return (x, y, self._data[i])

    def __str__(self):
        s = ''
        for l in self.as_2d_list():
            s += ' '.join([str(n) for n in l]) + '\n'

        return s

    def _populate(self, arr):
        self.h = len(arr)
        self.w = len(arr[0]) if self.h > 0 else 0

        for i in arr:
            for j in i:
                self._data.append(j)

    def _index(self, x, y):
        return x + (y * self.w)

    def as_2d_list(self):
        l = []
        for y in range(self.h):
            l.append([self.get(x, y) for x in range(self.w)])

        return l

    def get(self, x, y):
        return self._data[self._index(x, y)]

    def set(self, x, y, v):
        self._data[self._index(x, y)] = v


blocks = [
    # line
    [
        Matrix([
            [1],
            [1],
            [1],
            [1]
        ]),
        Matrix([
            [1, 1, 1, 1]
        ]),
        Matrix([
            [1],
            [1],
            [1],
            [1]
        ]),
        Matrix([
            [1, 1, 1, 1]
        ]),
        (200, 0, 0)
    ],
    # small T
    [
        Matrix([
            [0, 1, 0],
            [1, 1, 1]
        ]),
        Matrix([
            [1, 0],
            [1, 1],
            [1, 0]
        ]),
        Matrix([
            [1, 1, 1],
            [0, 1, 0]
        ]),
        Matrix([
            [0, 1],
            [1, 1],
            [0, 1]
        ]),
        (0, 200, 0)
    ],
    # L
    [
        Matrix([
            [1, 0],
            [1, 0],
            [1, 1]
        ]),
        Matrix([
            [1, 1, 1],
            [1, 0, 0]
        ]),
        Matrix([
            [1, 1],
            [0, 1],
            [0, 1]
        ]),
        Matrix([
            [0, 0, 1],
            [1, 1, 1]
        ]),
        (200, 200, 0)
    ],
    # mirror L
    [
        Matrix([
            [0, 1],
            [0, 1],
            [1, 1]
        ]),
        Matrix([
            [1, 0, 0],
            [1, 1, 1]
        ]),
        Matrix([
            [1, 1],
            [1, 0],
            [1, 0]
        ]),
        Matrix([
            [1, 1, 1],
            [0, 0, 1]
        ]),
        (100, 25, 100)
    ],
    # block
    [
        Matrix([
            [1, 1],
            [1, 1]
        ]),
        Matrix([
            [1, 1],
            [1, 1]
        ]),
        Matrix([
            [1, 1],
            [1, 1]
        ]),
        Matrix([
            [1, 1],
            [1, 1]
        ]),
        (0, 100, 200)
    ],
    # s
    [
        Matrix([
            [0, 1, 1],
            [1, 1, 0]
        ]),
        Matrix([
            [1, 0],
            [1, 1],
            [0, 1]
        ]),
        Matrix([
            [0, 1, 1],
            [1, 1, 0]
        ]),
        Matrix([
            [1, 0],
            [1, 1],
            [0, 1]
        ]),
        (50, 200, 200)
    ],
    # mirror s
    [
        Matrix([
            [1, 1, 0],
            [0, 1, 1]
        ]),
        Matrix([
            [0, 1],
            [1, 1],
            [1, 0]
        ]),
        Matrix([
            [1, 1, 0],
            [0, 1, 1]
        ]),
        Matrix([
            [0, 1],
            [1, 1],
            [1, 0]
        ]),
        (200, 50, 200)
    ]
]
