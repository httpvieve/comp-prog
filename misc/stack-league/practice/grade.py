grade = float(input())
id_valid = False
if grade < 0 and grade > 10 :
        print("Invalid input!")
else:
        dec = grade - int(grade)
        if dec == 0 or dec == 0.5:
                is_valid = True
                if is_valid:
                        if grade >= 8.5:
                                conv = "A"
                        elif grade >= 7.5 and grade <= 8.0:
                                conv = "B"
                        elif grade >= 6.5 and grade <= 7.0:
                                conv = "C"
                        elif grade >= 5.5 and grade <= 6.0:
                                conv = "D"
                        else:
                                conv = "F"
                        print("Grade " + str(conv))
        else:
                print("Grades should be rounded to the nearest half point.")    
        