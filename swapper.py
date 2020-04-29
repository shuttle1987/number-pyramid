def calculate_value(row):
    """Calculate the top value of the pyramid for a given row"""
    if len(row) == 1:
        # at the top of the pyramid
        return row[0]
    next_row_up = []
    for i in range(len(row)-1):
        next_row_up.append(row[i] + row[i+1])
    next_row_up

    return calculate_value(next_row_up)


assert calculate_value([1,2,5,6,7,11]) == 167

results = {}

def bins_to_value(bins):
    low = []
    high = []
    mid = []
    for values in bins:
        if len(values) == 2:
            low.append(values[0])
            high.append(values[1])
        else:
            mid = values[0]
    row = low + mid + list(reversed(high))
    return calculate_value(row)

assert bins_to_value(((1,11),(2,7),(5,6))) == 167

class CantSwap(Exception):
    """raise when a swap cannot be made"""


def swap_nested_tuple(data, indexes1, indexes2):
    new_data = list(list(bin) for bin in data)
    new_data[indexes1[0]][indexes1[1]], new_data[indexes2[0]][indexes2[1]] = new_data[indexes2[0]][indexes2[1]], new_data[indexes1[0]][indexes1[1]]
    return tuple(tuple(sorted(bin)) for bin in new_data)

def swap_to_smaller(candidate_numbers):
    """Swap candidates in bins such that overall value is lowered"""
    num_bins = len(candidate_numbers)
    swap_found = False
    for i in range(num_bins):
        smaller_bin = candidate_numbers[i]
        for j in range(i+1, num_bins):
            print("i, j", i, j)
            larger_bin = candidate_numbers[j]
            print("Smaller bin", smaller_bin, "larger bin", larger_bin)
            
            if smaller_bin[0] < larger_bin[0]:
                sol = swap_nested_tuple(candidate_numbers, (i,0), (j,0))
                if sol not in results:
                    swap_found = True
            elif smaller_bin[1] < larger_bin[0]:
                sol = swap_nested_tuple(candidate_numbers, (i,1), (j,0))
                if sol not in results:
                    swap_found = True
            elif smaller_bin[0] < larger_bin[1]:
                sol = swap_nested_tuple(candidate_numbers, (i,0), (j,1))
                if sol not in results:
                    swap_found = True
            elif smaller_bin[1] < larger_bin[1]:
                sol = swap_nested_tuple(candidate_numbers, (i,1), (j,1))
                print("*****",sol)
                if sol not in results:
                    swap_found = True
            if swap_found:
                return sol
    raise CantSwap(f"Couldn't swap to make smaller: {str(candidate_numbers)}")

def swap_to_larger(candidate_numbers):
    """Swap candidates in bins such that overall value is increased"""
    num_bins = len(candidate_numbers)
    new_solution = [list(bin) for bin in candidate_numbers]
    swap_found = False
    for i in range(num_bins):
        smaller_bin = candidate_numbers[i]
        for j in range(i+1, num_bins):
            larger_bin = candidate_numbers[j]
            if smaller_bin[0] > larger_bin[0]:
                sol = swap_nested_tuple(candidate_numbers, (i,0), (j,0))
                if sol not in results:
                    swap_found = True
            elif smaller_bin[1] > larger_bin[0]:
                sol = swap_nested_tuple(candidate_numbers, (i,1), (j,0))
                if sol not in results:
                    swap_found = True
            elif smaller_bin[0] > larger_bin[1]:
                sol = swap_nested_tuple(candidate_numbers, (i,0), (j,1))
                if sol not in results:
                    swap_found = True
            elif smaller_bin[1] > larger_bin[1]:
                sol = swap_nested_tuple(candidate_numbers, (i,1), (j,1))
                if sol not in results:
                    swap_found = True
            if swap_found:
                return sol

    raise CantSwap(f"Couldn't swap to make larger: {str(candidate_numbers)}")

def solve(candidate_numbers, target_sum: int):
    current_candidate = tuple(tuple(sorted(bin)) for bin in candidate_numbers)
    while True:
        print("currently trying", current_candidate)
        result = bins_to_value(current_candidate)
        print("value", result)
        results[current_candidate] = result
        print(results)
        if result == target_sum:
            return candidate_numbers
        elif result > target_sum:
            current_candidate = swap_to_smaller(candidate_numbers)
        else:
            current_candidate = swap_to_larger(candidate_numbers)

solve(candidate_numbers=((1,5),(2,7),(11,6)), target_sum=167)