from typing import List

MAX_STONE_LIST_LEN = 30
MAX_STONE_WEIGHT = 1000
MIN_REFERENCE_LENGTH = 1


class LatStoneWeight:
    def find_weight(self, stones: List[int]) -> int:
        """
        Responsible for finding the weight of the last stone by iterating over the available stone weight.
        :param stones: List of stone weights.
        :return: Integer containing the weight of the last stone.
        :raises: No exceptions raised custom.
        """
        imm_max_weight = 0
        last_stone_weight = 0
        max_weight = 0

        if (MIN_REFERENCE_LENGTH <= len(stones) <= MAX_STONE_LIST_LEN) and (MIN_REFERENCE_LENGTH <= max(stones) <= MAX_STONE_WEIGHT):
            while len(stones) > 1:
                max_weight = stones.pop(stones.index(max(stones)))
                imm_max_weight = stones.pop(stones.index(max(stones)))

                stones.append(max_weight - imm_max_weight)

            last_stone_weight = stones[0]

        return last_stone_weight
