import os
import time
def terminalClear(seconds):
    time.sleep(seconds)
    os.system("cls")
if __name__ == "__main__":
    terminalClear(1)