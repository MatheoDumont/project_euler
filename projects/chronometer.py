import time


def print_chrono_with_func(f, *args, **kwargs):
    chrono = Chrono()
    r=f(*args, **kwargs)
    chrono()
    print(r)
    print(chrono)


class Chrono:
    def __init__(self):
        self.tic = time.time_ns()
        self.tac = None

    def __call__(self):
        self.tac = time.time_ns()

    def __str__(self):
        return "Elapsed Time: {:.4f} {:.4f} (sec) (ms)".format(self.elapsed / 10**9, self.elapsed / 10**6)

    @property
    def elapsed(self):
        return self.tac - self.tic
