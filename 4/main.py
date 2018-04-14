from operator import attrgetter
from types import MethodType
from numpy.random import exponential

class Section:
    def __init__(self, lam, now):
        self.lam = lam
        self.time = now + exponential(1 / self.lam)

    def is_working(self, time):
        return self.time > time


class SectionStructure:
    def __init__(self, sections):
        self.sections = sections

    def replace_section(self, old_section, new_section):
        if old_section in self.sections:
            self.sections[self.sections.index(old_section)] = new_section
        else:
            raise ValueError

    def get_lowest(self):
        return min(self.sections, key=attrgetter('time'))


def is_working1(self, time):
    return (self.sections[0].is_working(time) and self.sections[1].is_working(time)) or \
           (self.sections[2].is_working(time) and self.sections[3].is_working(time))


def is_working2(self, time):
    return self.sections[0].is_working(time) and self.sections[1].is_working(time)


def is_working3(self, time):
    return (self.sections[0].is_working(time) or
           (self.sections[2].is_working(time)) or
           (self.sections[4].is_working(time)))


def is_working4(self, time):
    return self.sections[0].is_working(time) or self.sections[1].is_working(time)


def n(eps, quantile, p):
    return int(quantile ** 2 * p * (1 - p) / eps ** 2) #количество реализаций


def main():
    m = 4
    lams = [40 * 10 ** -6,
            10 * 10 ** -6,
            80 * 10 ** -6,
            30 * 10 ** -6]
    ni = [4, 2, 5, 2]
    li = [5, 3, 5, 2]
    print(f"spare sections = {li}")
    stop_time = 8760
    quantile = 2.326  # alpha = 0.99
    eps = 0.0001
    min_p = 0.995
    tests_number = n(eps, quantile, min_p)
    print(f"tests number = {tests_number}")
    fails = 0
    for _ in range(tests_number):
        structures = []
        for i, lam in enumerate(lams):
            structures.append(SectionStructure([Section(lam, 0) for _ in range(ni[i])]))

        structures[0].is_working = MethodType(is_working1, structures[0])
        structures[1].is_working = MethodType(is_working2, structures[1])
        structures[2].is_working = MethodType(is_working3, structures[2])
        structures[3].is_working = MethodType(is_working4, structures[3])

        working = True
        for i in range(m):
            for _ in range(li[i]):
                lowest = structures[i].get_lowest()
                structures[i].replace_section(lowest, Section(lams[i], lowest.time))
            working &= structures[i].is_working(stop_time)

        if not working:
            fails += 1

    success_probability = 1 - fails / tests_number
    new_n = n(eps, quantile, success_probability)
    print(f"success probability = {success_probability}")

if __name__ == '__main__':
    main()
