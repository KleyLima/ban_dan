from os import system
import time

system("clear")

def print_same(ch):
    print(ch, end="")
    return 0

def sequel(chars):
    for ch in chars:
        time.sleep(0.4)
        print_same(ch)
    print()

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total:
        print()



sequel("/ban danilo")


items = list(range(0, 57))
l = len(items)

printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(items):
    time.sleep(0.1)
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
