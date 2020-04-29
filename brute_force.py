from itertools import permutations
from typing import List

bottom_row = [1,2,5,6,7,11]

def calc_pyramid(rows):
    """recursive function that will calculate the next rows"""
    top_row = rows[-1]
    if len(top_row) == 1:
        # we are at the top of the pyramid now so break out of the recursion
        return rows
    next_row_up = []
    for i in range(len(top_row)-1):
        next_row_up.append(top_row[i] + top_row[i+1])
    rows.append(next_row_up)
    return calc_pyramid(rows)

result = calc_pyramid([bottom_row])
print(result)

def find_candidate_solution(bottom_row_numbers: List[int], top_number: int):
    for bottom_row_candidate in permutations(bottom_row_numbers, len(bottom_row_numbers)):
        result = calc_pyramid([list(bottom_row_candidate)])
        top_number_found = result[-1][0]
        if top_number_found == top_number:
            print("found a candidate solution")
            print(result)
            return result

find_candidate_solution(bottom_row_numbers=bottom_row, top_number=200)