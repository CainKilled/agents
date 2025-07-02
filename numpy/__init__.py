import math

int16 = 'int16'
float32 = 'float32'

class ndarray(list):
    def astype(self, dtype):
        return self

    def tobytes(self):
        return bytes(self)

    def __imul__(self, other):
        for i, v in enumerate(self):
            self[i] = v * other
        return self


def frombuffer(buffer, dtype=None, count=-1):
    data = buffer if count == -1 else buffer[:count]
    return ndarray(data)


def log10(x):
    return math.log10(x)


def clip(a, a_min, a_max, out=None):
    result = ndarray([min(max(v, a_min), a_max) for v in a])
    if out is not None:
        out[:] = result
        return out
    return result
