import datetime
import subprocess
from multiprocessing import Process

batcmd = """@ECHO OFF ECHO Hello World! Your first batch file was printed on the screen successfully."""
def data(dataset):
    for d in dataset:
        print("datasets",d)
def flashing(flashcmd):
    subprocess.call(flashcmd, shell=True)
    return 0
def main():
    p = Process(target=flashing, args=(batcmd,))
    p.start()
    p.join()
    print("call multiprocess")
if __name__ == "__main__":
    for x in range(1,10):
        print(x)
    main()
    data(['a','b','c','d'])
'''
this is my initial commit
iam useing this git for learnign purpose
'''
