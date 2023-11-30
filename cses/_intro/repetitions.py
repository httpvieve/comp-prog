def max_repetition (sequence):
        
        sequence += " "
        index = 0
        count = 0
        max_count = 1
        current = sequence[index]
        
        while (index < len(sequence)):
                if sequence[index] == current:
                        count = count + 1
                else:
                        if count > max_count:
                                max_count = count
                        count = 1
                current = sequence[index]
                index = index + 1
        return max_count

print (int(max_repetition(input())))