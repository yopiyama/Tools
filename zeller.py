# coding : utf-8
"""
zeller script
"""

import math


def zeller(date):
    """
    zeller

    Parameters
    ----------
    date : list[int, int, int]
        date[year, month, day]
    Returns
    -------
    week : str
    Days of the target date
    """

    week_list = ["Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday"]
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    if month == 1:
        month = 13
        year -= 1
    elif month == 2:
        month = 14
        year -= 1

    Y = year % 100
    C = math.floor(year/100)
    a = math.floor(26*(month+1)/10)
    g = 5 * C + math.floor(C/4)
    D = ((day + a + Y + math.floor(Y/4) + g + 5) % 7)

    return week_list[D]


def main():
    """
    main

    Parameters
    ----------
    none
    Returns
    -------
    none
    """

    print("yyyy/mm/dd >>>  ", end="")
    date = input().split("/")
    week = zeller(date)
    print(date[0] + "/" + date[1] + "/" + date[2] + "/ is " + week)


if __name__ == "__main__":
    main()
