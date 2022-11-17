from colorama import Fore
from playsound import playsound
import os
import sys
import time

def secretMenu():
    print(f"""{Fore.RED}
%%>=====================SECRET~MENU=====================<%%
| 1. Play Opening Animation                               |
| 2. Play Loading Bar Animation                           |
| 3. Listen to OpeningSFX                                 |
| 4. Exit                                                 |                             
%%>=====================================================<%%
{Fore.RESET}""")

def secretOpeningAnimation(speed):
    frame1 = f"""







           {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"""
    frame2 = f"""
    
    
    
    
    
    
           {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"""
    frame3 = f"""
    
    
    
    
    
           {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"""
    frame4 = f"""
    
    
    
    
           {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"""
    frame5 = f"""
    
    
    
           {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"""
    frame6 = f"""
    
    
           {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"""
    frame7 = f"""
    
           {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"""
    frame8 = f"""
           {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"""
    frame9 = f"""           {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"""

    animation = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9]

    for i in range(0, 9):
       os.system("cls")
       animationThing = animation[i % len(animation)]
       sys.stdout.write(f"{animationThing}\r")
       time.sleep(speed)
       i += 1

def secretOpeningAnimationPt2(speed):
    frame1 = f"         o {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"
    frame2 = f"        to {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"
    frame3 = f"      e to {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}" 
    frame4 = f"     me to {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"
    frame5 = f"    ome to {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"
    frame6 = f"   come to {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"
    frame7 = f"  lcome to {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"
    frame8 = f" elcome to {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"
    frame9 = f"Welcome to {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"
    frame10 = f"Welcome to {Fore.RED}Py{Fore.RESET}{Fore.RED}flix{Fore.RESET}"

    animation = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10]

    duration = 10
    for animationDuration in range(0, 10):
            animationThing = animation[animationDuration - len(animation)]
            sys.stdout.write(f"\r{animationThing} ")
            time.sleep(speed)
            animationDuration += 1
            duration = duration - 1

def secretLoadingBar(speed):
    animation = [
    f"[{Fore.RED}={Fore.RESET}       ]",
    f"[{Fore.RED}=={Fore.RESET}      ]",
    f"[{Fore.RED}==={Fore.RESET}     ]",
    f"[{Fore.RED}===={Fore.RESET}    ]",
    f"[{Fore.RED}====={Fore.RESET}   ]",
    f"[{Fore.RED}======{Fore.RESET}  ]",
    f"[{Fore.RED}======={Fore.RESET} ]",
    f"[{Fore.RED}========{Fore.RESET}]",
    f"[{Fore.RED} ======={Fore.RESET}]",
    f"[{Fore.RED}  ======{Fore.RESET}]",
    f"[{Fore.RED}   ====={Fore.RESET}]",
    f"[{Fore.RED}    ===={Fore.RESET}]",
    f"[{Fore.RED}     ==={Fore.RESET}]",
    f"[{Fore.RED}      =={Fore.RESET}]",
    f"[{Fore.RED}       ={Fore.RESET}]"
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
              sys.stdout.write(f"\r{Fore.RED}[========]{Fore.RESET} ")

def secretOpeningSound():
    playsound("./assets/openingSFX.mp3")
