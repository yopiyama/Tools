#!/usr/bin/env python
# coding:utf-8

"""
birthday_paradox.py
"""


import sys
import matplotlib.pyplot as plt
import numpy as np


def calc(N):
    """
    Calculation probability

    Parameters
    ----------
    N : int
        number of people
    Returns
    -------
    P : float
        parcentage
    """

    P = 1
    for i in range(N):
        P *= (365 - i)
    P = 1 - P/365**N
    return P


def graph(N):
    """
    plot birthday paradox graph and plot N

    Parameters
    ----------
    N : int
        number of people
    Returns
    -------
    none
    """

    num = np.arange(0, 356, 1)
    P = [1]*356
    for i in range(356):
        P[i] = calc(i)
    plt.plot(num, P)
    plt.plot(N, P[N], marker=".")
    plt.xlabel("Number of person")
    plt.ylabel("Probability")
    plt.title("Birthday paradox")
    plt.grid(True)
    plt.show()


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

    N = int(sys.argv[1])
    P = calc(N)
    print(P)
    graph(N)


if __name__ == "__main__":
    main()
