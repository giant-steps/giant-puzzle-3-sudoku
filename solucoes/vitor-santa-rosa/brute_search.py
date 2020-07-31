#!/usr/bin/env python3.7


"""
https://gscap.com.br/puzzle/
https://gscap.com.br/solucao-do-giant-puzzle-3/

234165789
517928436
689734125
153492678
968357241
742816953
321549867
475681392
896273514
100%|██████████████████████████████████| 187579/187579 [09:43<00:00, 321.66it/s]
"""


import itertools
import math
import numpy as np
import sympy
import tqdm
import toolz
import warnings


warnings.filterwarnings('ignore')


class GSCPuzzle003Problem:

    def __init__(self):
        super().__init__()
        self.order = self._make_order()
        assert len(set(self.order)) == len(self.order)

    def initial_state(self):
        grid = np.full((9, 9), np.nan)
        grid[2, 8] = 5
        grid[0, 5] = 5
        return (0, self._grid2tuple(grid))

    def is_final_state(self, state):
        i, _ = state
        return i >= 9*9

    def actions(self, state):
        if state[0] >= 9*9:
            return

        for action in range(1, 9+1):
            if self._valid_state(self.next_state(state, action)):
                yield action

    def next_state(self, state, action):
        i, tup = state
        loc = self.order[i]
        grid = self._tuple2grid(tup)

        grid[loc//9, loc%9] = action
        return (i+1, self._grid2tuple(grid))

    @classmethod
    def _valid_state(cls, state):
        _, tup = state
        grid = cls._tuple2grid(tup)

        sudoku_nonrepeating_rules = [
            *[grid[i, :] for i in range(9)],
            *[grid[:, j] for j in range(9)],
            *[
                grid[i:i+3, j:j+3]
                for i, j in itertools.product(range(0, 9, 3), repeat=2)
            ],
        ]
        for slice_ in sudoku_nonrepeating_rules:
            for k, v in zip(*np.unique(slice_, return_counts=True)):
                if not np.isnan(k) and v > 1:
                    return False

        divisibility_rules = [
            (grid[0, ::-1], 22),
            (grid[1, :], 2),
            (grid[2, :], 125),
            (grid[4, :], 29),
            (grid[4, ::-1], 79),
            (grid[7, :], 8),
            (grid[7, ::-1], 2),

            (grid[:, 0], 4),
            (grid[::-1, 0], 257),
            (grid[:, 2], 2),
            (grid[::-1, 2], 17),
            (grid[:, 5], 11),
            (grid[::-1, 5], 5),
            (grid[:, 6], 127),
            (grid[::-1, 6], 877),
            (grid[:, 8], 4),
        ]
        for dividend_slice, divisor in divisibility_rules:
            dividend = ''.join(map(cls._int_str, list(dividend_slice)))
            if dividend.isdigit():
                if int(dividend) % divisor != 0:
                    return False
            # else:
            #     upper = int(dividend.replace(' ', '9'))
            #     lower = int(dividend.replace(' ', '1'))
            #     if (
            #         int(upper/divisor) == int(lower/divisor)
            #         and int(lower/divisor) > lower/divisor
            #     ):
            #         return False

        even_rules =[
            grid[0, 0],
            grid[1, 8],
            grid[7, 0],
            grid[7, 8],
            grid[8, 0],
            grid[8, 2],
            grid[8, 8],
        ]
        if any(not np.isnan(x) and x % 2 != 0 for x in even_rules):
            return False

        magic_rules = [
            grid[3, 3:6].sum(),
            grid[4, 3:6].sum(),
            grid[5, 3:6].sum(),
            grid[3:6, 3].sum(),
            grid[3:6, 4].sum(),
            grid[3:6, 5].sum(),
            grid[[[3, 4, 5], [3, 4, 5]]].sum(),
            grid[[[3, 4, 5], [5, 4, 3]]].sum(),
        ]
        # there is only one magic square with n=3, with v=15
        # https://oeis.org/A006052
        for magic_val in magic_rules:
            if not np.isnan(magic_val) and magic_val != 15:
                return False
        # magic_vals = set(map(str, magic_rules))
        # if 'nan' not in magic_vals and len(magic_vals) > 1:
        #     return False

        # the only possible values for this col
        # for i in range(0, 10**9+1, 877):
        #     s = str(i)
        #     if (
        #         len(s) == 9 and '0' not in s and len(set(s)) == 9
        #         and i % 877 == 0 and int(s[::-1]) % 127 == 0
        #     ):
        #         print(s)
        possibles_877_127 = [
            '329745861',
            '532674891',
            '538926147',
            '729368451',
            '923417856',
        ]
        current = np.array(
            list(''.join(map(cls._int_str, list(grid[::-1, 6])))))
        if not any(
            ((current == ' ') | (np.array(list(possible)) == current)).all()
            for possible in possibles_877_127
        ):
            return False

        return True

    @classmethod
    def _repr_state(cls, state, grid_mode=False):
        filled = np.sum(~np.isnan(cls._tuple2grid(state[1])))
        s = ''.join(map(cls._int_str, state[1]))

        if grid_mode:
            return '\n'.join([s[i:i+9] for i in range(0, len(s), 9)])
        else:
            return f'|{s}|\t{filled/9*9:.04f} completed'

    @staticmethod
    def _make_order():
        # inv = np.arange(9*9)[list(map(int, """
        #     38 52 44    53 54 21    22 55 56
        #     37 57 43    58 59 20    23 60 61
        #     36 48 42    50 51 19    24 49 10

        #     30 32 33    06 05 04    25 62 63
        #     11 12 13    02 01 00    14 15 16
        #     31 34 35    07 08 03    26 64 65

        #     39 66 45    77 78 18    27 76 73
        #     40 67 46    69 70 17    28 71 72
        #     41 68 47    79 80 09    29 75 74
        # """.split()))]
        # return np.arange(len(inv))[np.argsort(inv)]
        
        rule_count = math.factorial(9)*np.ones((9, 9))

        rule_count[0, ::-1] *= 1/22
        rule_count[1, :] *= 1/2
        rule_count[2, :] *= 1/125
        rule_count[4, :] *= 3/29 * 1/10000
        rule_count[4, ::-1] *= 3/79 * 1/10000
        rule_count[7, :] *= 1/8
        rule_count[7, ::-1] *= 1/2

        rule_count[:, 0] *= 1/4
        rule_count[::-1, 0] *= 1/257
        rule_count[:, 2] *= 1/2
        rule_count[::-1, 2] *= 1/17
        rule_count[:, 5] *= 3/11 * 1/10000
        rule_count[::-1, 5] *= 3/5 * 1/10000
        rule_count[:, 6] *= 1/127
        rule_count[::-1, 6] *= 1/877 * 1/10
        rule_count[:, 8] *= 1/4

        rule_count[3:6, 3:6] *= 8/math.factorial(9)
        rule_count[3:6, 3:6] = 0

        rule_priority = np.full_like(rule_count, 0)
        rule_priority[0, 0] = -1
        rule_priority[1, 8] = -1
        rule_priority[7, 0] = -1
        rule_priority[7, 8] = -1
        rule_priority[8, 0] = -1
        rule_priority[8, 2] = -1
        rule_priority[8, 8] = -1
        rule_priority[4, :] = -3
        rule_priority[:, 5] = -4
        rule_priority[:, 6] = -5
        rule_priority[3:6, 3:6] = -6

        rule_count = rule_count/np.max(rule_count) + rule_priority

        return list(
            map(
                lambda tup: 9*tup[1][0]+tup[1][1],
                sorted(
                    map(
                        lambda tup: tuple(reversed(tup)),
                        np.ndenumerate(rule_count)))))

    @staticmethod
    def _grid2tuple(grid):
        return tuple(grid.reshape((9*9)))

    @staticmethod
    def _tuple2grid(tup):
        return np.array(tup).reshape((9, 9))

    @staticmethod
    def _int_str(x):
        return ' ' if np.isnan(x) else str(int(x))

    @staticmethod
    def _patch2grid(slice_, patch):
        grid = np.full((9, 9), np.nan)
        grid[slice_] = patch
        return grid

    @staticmethod
    def _grid_compatible(grid1, grid2):
        return (np.isnan(grid1) | np.isnan(grid2) | (grid1 == grid2)).all()


def main():
    problem = GSCPuzzle003Problem()
    states = {problem.initial_state()}
    final_states = set()
    final_primes = set()
    best_val, best_arg = 0, None
    pbar = tqdm.tqdm(ncols=80)
    done = 0

    while states:
        state = states.pop()
        filled = np.sum(~np.isnan(problem._tuple2grid(state[1])))

        if filled > best_val or filled == 1:
            best_val, best_arg = filled, state
            print()
            print(problem._repr_state(state, grid_mode=True))

        if problem.is_final_state(state):
            final_states.add(state)
        else:
            for action in problem.actions(state):
                states.add(problem.next_state(state, action))

        done += 1
        pbar.total = done + len(states)
        pbar.update(1)
    else:
        pbar.close()

    for state in final_states:
        grid = problem._tuple2grid(state[1])
        diag = int(''.join(map(problem._int_str, grid[[range(9), range(9)]])))
        final_primes.update(set(sympy.ntheory.factorint(diag).keys()))

    with open('./final_states.txt', 'w') as outfile:
        print(*map(problem._repr_state, final_states), sep='\n', file=outfile)
    with open('./final_primes.txt', 'w') as outfile:
        print(*sorted(final_primes), sep='\n', file=outfile)


if __name__ == "__main__":
    main()
