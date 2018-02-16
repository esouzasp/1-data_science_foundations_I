#----------------------------------------
def dateIsBefore(y1, m1, d1, y2, m2, d2):
    if y1 < y2:
        return True
    if y1 == y2:
        if m1 < m2:
            return true
        if m1 == m2:
            return d1 < d2
    return false
    
