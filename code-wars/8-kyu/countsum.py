def count_positives_sum_negatives(arr):
        result = []
        if len(arr) > 0:
            result = [0, 0]
            for num in arr:
                if num > 0:
                    result[0] += 1                        
                elif num < 0:
                    result[1] += num
        return result
                