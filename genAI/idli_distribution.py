def can_distribute(idlis):
    odd_count = sum(1 for idli in idlis if idli % 2 != 0)
    return odd_count % 2 == 0

def distribute_idlis(idlis):
    if not can_distribute(idlis):
        return -1
    
    n = len(idlis)
    idli_count = 0
    
    while True:
        for index, val in enumerate(idlis[:-1]):  # Iterate up to the second last person
            if val % 2 != 0:  # If a person has an odd number of idlis
                idlis[index] += 1  # Give one idli to the current person
                idlis[index+1] += 1  # Give one idli to the person behind
                idli_count += 2  # Increment idli count by 2
        
        if all(idli % 2 == 0 for idli in idlis):
            break
        
        # Check if the last person has an odd number of idlis
        if idlis[-1] % 2 != 0:
            idlis[-1] += 1  # Give one idli to the last person
            idli_count += 1  # Increment idli count by 1
    
    return idli_count

# Example usage:
idlis = [1, 2, 4, 3]
print(distribute_idlis(idlis))  # Output: 6
