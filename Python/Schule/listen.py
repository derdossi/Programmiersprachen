mess = [34, 33, 47, 56, 66, 44, 88, 55, 52, 30]

sum = mess[0] + mess[1] + mess[2] + mess[3] + \
    mess[4] + mess[5] + mess[6] + mess[7] + mess[8] + mess[9]


def mess_avg_50(liste: list):
    sum = 0
    for i in mess:
        if i > 50:
            sum += i
        return sum


def avg():
    return sum / len(mess)


print(avg())
