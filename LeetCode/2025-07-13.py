from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Sort both players and trainers
        players.sort()
        trainers.sort()
        
        player_pointer = 0
        trainer_pointer = 0
        matches = 0
        
        # Use two pointers to find matches
        while player_pointer < len(players) and trainer_pointer < len(trainers):
            if players[player_pointer] <= trainers[trainer_pointer]:
                # A match is found
                matches += 1
                player_pointer += 1
                trainer_pointer += 1
            else:
                # Move to the next trainer
                trainer_pointer += 1
        
        return matches
