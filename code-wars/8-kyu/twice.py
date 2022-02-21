def twice_as_old(dad_years_old, son_years_old):
        dif_1 = dad_years_old - 2 * son_years_old
        dif_2 = 2 * son_years_old - dad_years_old
        if dif_1 < 0:
                return dif_2
        else:
                return dif_1