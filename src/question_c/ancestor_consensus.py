def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    # List to store the positions of the occurrences
    positions = []
    
    # Start searching from the beginning of dna_string1
    start = 0
    
    while True:
        # Find the index of the next occurrence of dna_string2 in dna_string1
        start = dna_string1.find(dna_string2, start)
        
        # If no more occurrences are found, break the loop
        if start == -1:
            break
        
        # Store the position (convert to 1-based index)
        positions.append(start + 1)
        
        # Move to the next position for the next find
        start += 1
    
    # If there are any positions, return them as separate arguments
    # Otherwise, return an empty tuple
    if positions:
        return tuple(positions)
    else:
        return tuple()  # Empty tuple for no occurrences
