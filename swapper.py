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


#def solve(candidate_numbers, target_sum: int):
    #for i in range(candidate_numbers):

    #initial_bins = 
    #while True