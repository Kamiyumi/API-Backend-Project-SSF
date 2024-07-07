import math
from decimal import Decimal

def wilks_coeff(a, b, c, d, e, f, x):
    if isinstance(x, Decimal):
        x = float(x)
    return 500 / (a + b * x + c * x**2 + d * x**3 + e * x**4 + f * x**5)

def wilks_coeff_male(bw):
    a = -216.0475144
    b = 16.2606339
    c = -0.002388645
    d = -0.00113732
    e = 7.01863e-06
    f = -1.291e-08
    if isinstance(bw, Decimal):
        bw = float(bw)
    bw = min(bw, 201.9)
    bw = max(bw, 40)
    return wilks_coeff(a, b, c, d, e, f, bw)

def wilks_coeff_female(bw):
    a = 594.31747775582
    b = -27.23842536447
    c = 0.82112226871
    d = -0.00930733913
    e = 0.00004731582
    f = -0.00000009054
    if isinstance(bw, Decimal):
        bw = float(bw)
    bw = min(bw, 154.53)
    bw = max(bw, 26.51)
    return wilks_coeff(a, b, c, d, e, f, bw)

def dots(is_male, bodyweight, total):
    if isinstance(bodyweight, Decimal):
        bodyweight = float(bodyweight)
    if isinstance(total, Decimal):
        total = float(total)
    male_coeff = [-307.75076, 24.0900756, -0.1918759221, 0.0007391293, -0.000001093]
    female_coeff = [-57.96288, 13.6175032, -0.1126655495, 0.0005158568, -0.0000010706]

    denominator = male_coeff[0] if is_male else female_coeff[0]
    coeff = male_coeff if is_male else female_coeff
    max_bw = 210 if is_male else 150
    bw = min(max(40, bodyweight), max_bw)

    for i in range(1, len(coeff)):
        denominator += coeff[i] * (bw**i)

    score = (500 / denominator) * total
    return score

def wilks(is_male, bodyweight, total):
    if isinstance(bodyweight, Decimal):
        bodyweight = float(bodyweight)
    if isinstance(total, Decimal):
        total = float(total)
    if is_male:
        return wilks_coeff_male(bodyweight) * total
    return wilks_coeff_female(bodyweight) * total

#Women: =LIFT*500/(-0.00000255986906*BW^4+0.00116119212*BW^3-0.205352889*BW^2+17.3690866*BW+55.4261)
#Men: =LIFT*500/(-0.000000793954283*BW^4+0.000493457474*BW^3-0.1231642956*BW^2+16.0233664*BW+45.59224)

def para(is_male, bodyweight, total):
    if isinstance(bodyweight, Decimal):
        bodyweight = float(bodyweight)
    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    if is_male:
        A = -0.000000793954283 * (bodyweight ** 4)
        B = 0.000493457474 * (bodyweight ** 3)
        C = 0.1231642956 * (bodyweight ** 2)
        D = 16.0233664 * bodyweight
        E = 45.59224
    else:
        A = -0.00000255986906 * (bodyweight ** 4)
        B = 0.00116119212 * (bodyweight ** 3)
        C = 0.205352889 * (bodyweight ** 2)
        D = 17.3690866 * bodyweight
        E = 55.4261
    return (total * 500) / (A + B - C + D + E)


def ipfgl(is_male, is_equipped, discipline, bodyweight, total):
    if isinstance(bodyweight, Decimal):
        bodyweight = float(bodyweight)
    if isinstance(total, Decimal):
        total = float(total)
    A = 0
    B = 0
    C = 0
    if is_male:
        if is_equipped:
            if discipline == "S":
                return 0
            elif discipline == "B":  # Equipped bench, male
                A = 381.22073
                B = 733.79378
                C = 0.02398
            elif discipline == "D":
                return 0
            elif discipline == "T":  # Equipped powerlifting, male
                A = 1236.25115
                B = 1449.21864
                C = 0.01644
            else:
                return 0
        else:
            if discipline == "S":
                return 0
            elif discipline == "B":  # Classic benchpress, male
                A = 320.98041
                B = 281.40258
                C = 0.01008
            elif discipline == "D":
                return 0
            elif discipline == "T":  # Classic powerlifting, male
                A = 1199.72839
                B = 1025.18162
                C = 0.00921
            else:
                return 0
    else:
        if is_equipped:
            if discipline == "S":
                return 0
            elif discipline == "B":  # Equipped Bench, female
                A = 221.82209
                B = 357.00377
                C = 0.02937
            elif discipline == "D":
                return 0
            elif discipline == "T":  # Equipped powerlifting, female
                A = 758.63878
                B = 949.31382
                C = 0.02435
            else:
                return 0
        else:
            if discipline == "S":
                return 0
            elif discipline == "B":  # Classic benchpress, female
                A = 142.40398
                B = 442.52671
                C = 0.04724
            elif discipline == "D":
                return 0
            elif discipline == "T":  # Classic powerlifting, female
                A = 610.32796
                B = 1045.59282
                C = 0.03048
            else:
                return 0

    return total * 100.0 / (A - B * math.e ** (-C * bodyweight))
