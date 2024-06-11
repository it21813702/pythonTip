def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    tip = dollars * percent

    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # accept a str $##.##
    # remove the leading $
    d = d.lstrip("$")

    # return the amount as a float
    d = float(d)
    return d


def percent_to_float(p):
    # accept a str as input (formatted as ##%)
    # remove the trailing %
    p = p.rstrip("%")

    # return the percentage as a float.
    p = float(p) / 100
    return p

main()
