import numpy as np
import pandas as pd

def solution():
    r = np.random.uniform(size=1)
    if r <= 1/3:
        return "A"
    if r > 1/3 and r <= 2/3:
        return "B"
    if r > 2/3:
        return "C"

def selection():
    r = np.random.uniform(size=1)
    if r <= 1/3:
        return "A"
    if r > 1/3 and r <= 2/3:
        return "B"
    if r > 2/3:
        return "C"

def open_door(selection):
        if selection == "A":
            r = np.random.uniform(size=1)
            if r < 0.5:
                return "B"
            if r >= 0.5:
                return "C"
        if selection == "B":
            r = np.random.uniform(size=1)
            if r < 0.5:
                return "C"
            if r >= 0.5:
                return "A"
        if selection == "C":
            r = np.random.uniform(size=1)
            if r < 0.5:
                return "B"
            if r >= 0.5:
                return "A"

def reshuffle(prior):
    if prior == "A":
        r = np.random.uniform(size=1)
        if r < 0.5:
            return "B"
        if r >= 0.5:
            return "C"
    if prior == "B":
        r = np.random.uniform(size=1)
        if r < 0.5:
            return "A"
        if r >= 0.5:
            return "C"
    if prior == "C":
        r = np.random.uniform(size=1)
        if r < 0.5:
            return "A"
        if r >= 0.5:
            return "B"

def score(n):
    tbl = [['Trial', 'Solution', 'Selection', 'Open Door', 'Reshuffle', 'Result']]
    for x in range(n):
        a = solution()
        b = selection()
        c = open_door(b)
        d = reshuffle(c)
        if d == a:
            e = "Win"
        else:
            e = "Loss"
        tbl.append([x+1, a, b, c, d, e])
    return tbl

def montey_hall_simple(n):
    print('Simple Monty Hall Problem Simulation')
    print('What does the behavioral data look like versus the simulation?')
    print('https://behavioralscientist.org/steven-pinker-rationality-why-you-should-always-switch-the-monty-hall-problem-finally-explained/')

    print('Begin Simulation w/ Reshuffle')
    print('n = {}'.format(n))
    tbl = score(n)
    df = pd.DataFrame(tbl[1:n+2], columns = tbl[0])
    print(df)
    numerator = sum(df['Result'] == 'Win')
    print(numerator/n)

montey_hall_simple(1000000)
