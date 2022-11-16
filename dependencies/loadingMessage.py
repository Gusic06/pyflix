import time
import os
import sys
import threading
from colorama import Fore

def loadingMessage(speed):
    animation = [".", "..", "..."]
    for x in range(1, 4):
        for i in range(0, 3):
            animationThing = animation[i-len(animation)]
            sys.stdout.write(f"\r{Fore.RED}Exiting program now{animationThing}{Fore.RESET} ")
            time.sleep(speed)
            i += 1

def loadingBar(speed):
    animation = [".", "..", "..."]
    for x in range(1, 4):
        for i in range(0, 3):
            animationThing = animation[i-len(animation)]
            sys.stdout.write(f"\r{Fore.RED}Exiting to main menu now{animationThing}{Fore.RESET} ")
            time.sleep(speed)
            i += 1

def rgbLoadingBar(speed):
    animation = [
    f"[{Fore.LIGHTCYAN_EX}={Fore.RESET}       ]",
    f"[{Fore.CYAN}=={Fore.RESET}      ]",
    f"[{Fore.LIGHTBLUE_EX}==={Fore.RESET}     ]",
    f"[{Fore.BLUE}===={Fore.RESET}    ]",
    f"[{Fore.LIGHTMAGENTA_EX}====={Fore.RESET}   ]",
    f"[{Fore.MAGENTA}======{Fore.RESET}  ]",
    f"[{Fore.LIGHTYELLOW_EX}======={Fore.RESET} ]",
    f"[{Fore.YELLOW}========{Fore.RESET}]",
    f"[{Fore.LIGHTGREEN_EX} ======={Fore.RESET}]",
    f"[{Fore.GREEN}  ======{Fore.RESET}]",
    f"[{Fore.LIGHTRED_EX}   ====={Fore.RESET}]",
    f"[{Fore.RED}    ===={Fore.RESET}]",
    f"[{Fore.LIGHTCYAN_EX}     ==={Fore.RESET}]",
    f"[{Fore.CYAN}      =={Fore.RESET}]",
    f"[{Fore.LIGHTMAGENTA_EX}       ={Fore.RESET}]"
    ]
    i = 0
    duration = 8
    counter = 0
    for i in range(0, 8):
        animationThing = animation[i-len(animation)]
        sys.stdout.write(f"\r{animationThing} ")
        time.sleep(speed)
        i += 1
        duration = duration - 1
        counter = counter + 1
        if duration == 0:
            sys.stdout.write(f"\r{Fore.YELLOW}[========]{Fore.RESET} ")

def openingAnimation(speed):
    frame1 = f"""







           {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"""
    frame2 = f"""
    
    
    
    
    
    
           {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"""
    frame3 = f"""
    
    
    
    
    
           {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"""
    frame4 = f"""
    
    
    
    
           {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"""
    frame5 = f"""
    
    
    
           {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"""
    frame6 = f"""
    
    
           {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"""
    frame7 = f"""
    
           {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"""
    frame8 = f"""
           {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"""
    frame9 = f"""           {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"""

    animation = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9]

    for i in range(0, 9):
       os.system("cls")
       animationThing = animation[i % len(animation)]
       sys.stdout.write(f"{animationThing}\r")
       time.sleep(speed)
       i += 1
def openingAnimationPt2(speed):
       frame1 = f"         o {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"
       frame2 = f"        to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"
       frame3 = f"      e to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}" 
       frame4 = f"     me to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"
       frame5 = f"    ome to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"
       frame6 = f"   come to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"
       frame7 = f"  lcome to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"
       frame8 = f" elcome to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"
       frame9 = f"Welcome to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"
       frame10 = f"Welcome to {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}"

       animation = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10]

       duration = 10
       for animationDuration in range(0, 10):
              animationThing = animation[animationDuration - len(animation)]
              sys.stdout.write(f"\r{animationThing} ")
              time.sleep(speed)
              animationDuration += 1
              duration = duration - 1
              

if __name__ == "__main__":
    test = float(input("Speed: "))
    loadingMessage(test)