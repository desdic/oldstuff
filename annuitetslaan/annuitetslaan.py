#!/usr/bin/env python
""" annuitetslån """

from sys import argv
from getopt import getopt
from datetime import datetime

if __name__ == '__main__':

    BELOOB = None
    RENTE = None
    AFDRAG = None

    OPTS, ARGS = getopt(argv[1:],
                        "",
                        ["beloob=",
                         "rente=",
                         "afdrag="])

    try:

        for opt, arg in OPTS:
            if opt == '--beloob':
                BELOOB = float(arg)
            if opt == '--rente':
                RENTE = float(arg)
            if opt == '--afdrag':
                AFDRAG = float(arg)
    except ValueError as error:
        print("ERR: %s" % (error))
        exit(1)

    if BELOOB is None or RENTE is None or AFDRAG is None:
        print("beløb, rente og afdrag er påkrævet")
        exit(1)

    TODAY = datetime.today()

    YEAR = TODAY.year
    MONTH = TODAY.month
    DAY = TODAY.day

    if DAY != 1:
        MONTH += 1

        if MONTH == 13:
            MONTH = 1
            YEAR += 1

    print("Amortisationstabel")
    print("År\tMåned\tAfdrag\tRente\tRestgæld")
    MONTHS = 1
    RENTESUM = 0
    while True:
        T = 0
        if MONTH in (3, 6, 9, 12):
            T = BELOOB * RENTE
            RENTESUM += T
            BELOOB += T

        if AFDRAG > BELOOB:
            AFDRAG = BELOOB

        BELOOB -= AFDRAG

        print("%04d\t%02d\t%02d\t%0.2f\t%0.2f" % (YEAR,
                                                  MONTH,
                                                  AFDRAG,
                                                  T,
                                                  BELOOB))
        if BELOOB <= 0:
            break

        MONTH += 1
        if MONTH == 13:
            MONTH = 1
            YEAR += 1
        MONTHS += 1

    print("-----------------------------------------")
    print("%02d Måneder\t%02d\t%0.2f\t%0.2f" % (MONTHS,
                                                AFDRAG*MONTHS,
                                                RENTESUM,
                                                (AFDRAG*MONTHS)+RENTESUM))
