class Numbers:
        @staticmethod

        def singleDigitSum(sdg, max, idx):
                key = []
      
                for i in range (sdg, max):
                        phrase = str(i)
                        while len (phrase) > 1:
                                count = 0
                                for digit in phrase:
                                        count += int(digit)
                                phrase = str(count)
          
                        if int(phrase) == sdg:
                                key.append(i)
          
                if len(key) >= idx:
                        return key[idx - 1]
                else:
                        return -1
        