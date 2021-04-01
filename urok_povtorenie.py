trata = 0


def podschet(day):
    global trata
    trata += day

podschet(17)
podschet(20)
podschet(21)
print(trata)


def podschet2(*trata1):
    sum = 0
    for day in trata1:
        sum += day
    return sum

print(podschet2(56, 14, 17, 56))
