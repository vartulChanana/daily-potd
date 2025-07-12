from typing import List
from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dfs(players_tuple, round_num):
            players = list(players_tuple)
            i, j = 0, len(players) - 1
            next_rounds = set()
            
            while i < j:
                a, b = players[i], players[j]
                if {a, b} == {firstPlayer, secondPlayer}:
                    return (round_num, round_num)

                winners = []
                for x, y in zip(range(len(players) // 2), range(len(players) - 1, len(players) // 2 - 1, -1)):
                    p1, p2 = players[x], players[y]
                    if {p1, p2} == {firstPlayer, secondPlayer}:
                        return (round_num, round_num)
                    if firstPlayer in (p1, p2) or secondPlayer in (p1, p2):
                        winners.append((firstPlayer if p1 == firstPlayer or p2 == firstPlayer else secondPlayer,))
                    else:
                        winners.append((p1, p2))

                if len(players) % 2 == 1:
                    winners.append((players[len(players) // 2],))

                min_round = float('inf')
                max_round = float('-inf')

                def generate_winners(index, current):
                    nonlocal min_round, max_round
                    if index == len(winners):
                        next_players = tuple(sorted(current))
                        e, l = dfs(next_players, round_num + 1)
                        min_round = min(min_round, e)
                        max_round = max(max_round, l)
                        return
                    for player in winners[index]:
                        generate_winners(index + 1, current + [player])

                generate_winners(0, [])
                return (min_round, max_round)

        return list(dfs(tuple(range(1, n + 1)), 1))

