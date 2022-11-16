import os
import sys
import time
import subprocess
import shutil
from dependencies.terminalClear import terminalClear
from dependencies.divider import divider
from dependencies.loadingMessage import openingAnimation, openingAnimationPt2, rgbLoadingBar, loadingBar, loadingMessage
from dependencies.openingSFX import opening
from threading import *
from colorama import Fore

def Pyflix():

    openingSound = Thread(target=opening, daemon=True)
    openingSound.start()
    
    time.sleep(0.00045)

    openingAnimation(0.24)
    openingAnimationPt2(0.08)

    if os.path.exists(".\\settings\\settings.py"):
        with open(".\\settings\\settings.py", "r") as file:
            fullscreenPreference = file.read()
    else:
        fullscreenPreference = True

    if os.path.exists(".\\Movies") == False:

        time.sleep(0.75)
        print("\n")
        divider()
        
        print(f"It looks like it is the first time you are using {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}.")
        time.sleep(0.75)
        print(f"Please wait while {Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET} finishes the setup...")
        time.sleep(0.75)
        divider()
        rgbLoadingBar(0.75)
        print(f"{Fore.YELLOW}Setup Complete!{Fore.RESET}")
        time.sleep(0.5)
        print(f"{Fore.YELLOW}Launching pyflix now.{Fore.RESET}")
        time.sleep(1)

        try:
            os.system("mkdir Movies")
        except:
            subprocess.call(["mkdir", "Movies"])

    terminalClear(1)

    while True:
        print(f"""                   ~~{Fore.YELLOW}Py{Fore.RESET}{Fore.BLUE}flix{Fore.RESET}~~
{Fore.RED}%%>==========================================<%%{Fore.RESET}
{Fore.YELLOW}|{Fore.RESET} 1. Watch Movie                               {Fore.YELLOW}|{Fore.RESET}
{Fore.YELLOW}|{Fore.RESET} 2. List all Movies                           {Fore.YELLOW}|{Fore.RESET}
{Fore.YELLOW}|{Fore.RESET} 3. Add Movies from Directory                 {Fore.YELLOW}|{Fore.RESET}
{Fore.YELLOW}|{Fore.RESET} 4. Settings                                  {Fore.YELLOW}|{Fore.RESET}
{Fore.YELLOW}|{Fore.RESET} 5. Exit                                      {Fore.YELLOW}|{Fore.RESET}                                  
{Fore.RED}%%>==========================================<%%{Fore.RESET}
        """)

        userInput = input(f"What {Fore.YELLOW}mode{Fore.RESET} do you want to select? {Fore.YELLOW}(1-5){Fore.RESET} -> ")

        if userInput == "1" or userInput == 1:

            terminalClear(0.75)
            movieName = input(f"What is the name of the movie you want to view? {Fore.YELLOW}(Case Sensitive){Fore.RESET} -> ")

            if os.path.exists(f".\\Movies\\{movieName}.mp4") and fullscreenPreference == True:
                subprocess.call(["cmd", "/c", "start", "/max", f".\\Movies\\{movieName}.mp4"])
                terminalClear(0.75)
            
            if os.path.exists(f".\\Movies\\{movieName}.mp4"):
                if " " in movieName:
                    newMovieName = movieName.split(2, " ")
                    subprocess.call(["cmd", "/c", "start", f""])
                subprocess.call(["cmd", "/c", "start", f".\\Movies\\{newMovieName}.mp4"])
                terminalClear(0.75)

            else:
                terminalClear(0)
                print(f"{Fore.RED}ERROR: An error occured when trying to open {movieName}.mp4!{Fore.RESET}")
                terminalClear(1)
                continue
        
        if userInput == "2" or userInput == 2:

            terminalClear(0)
            print(f"                                                ~~{Fore.YELLOW}MOVIE LIST{Fore.RESET}~~")
            divider()
            if len(os.listdir(".\\Movies\\")) == 0:
                print(f"{Fore.YELLOW}It seems you haven't added any movies yet to your movie folder yet.{Fore.RESET}")
            
            elif len(os.listdir(".\\Movies\\")) > 10:
                for movies in os.listdir(".\\Movies\\"):
                    rgbLoadingBar(0.025)
                    print(f"{Fore.YELLOW}{movies}{Fore.RESET}")
            
            else:
                for movies in os.listdir(".\\Movies\\"):
                    rgbLoadingBar(0.065)
                    print(f"{Fore.YELLOW}{movies}{Fore.RESET}")

            divider()
            exitPrompt = input(f"Do you want to return to the main menu now? {Fore.YELLOW}(Y/N){Fore.RESET} -> ").title()

            if exitPrompt == "Y" or exitPrompt == "Yes":
                terminalClear(0)
                loadingBar(0.15)
                terminalClear(0.2)
                continue

            if exitPrompt == "N" or exitPrompt == "No":

                divider()
                time.sleep(5)
                exitPrompt = exitPrompt = input(f"Do you want to return to the main menu now? {Fore.YELLOW}(Y/N){Fore.RESET} -> ").title()

            terminalClear(0.75)

        if userInput == "3" or userInput == 3:

            movieName = input(f"What is the name of the move you want to add? {Fore.YELLOW}(Case Sensitive){Fore.RESET} -> ")
            movieName = f"{movieName}.mp4"
            
            originalMoviePath = glob.glob(movieName)
            try:
                if os.path.exists(originalMoviePath):
                    shutil.copy(originalMoviePath, f".\\Movies\\{movieName}")
            except:
                for root, dirs, files in os.walk("C:\\"):
                    for name in files:
                        if name == movieName:
                            originalMoviePath = os.path.abspath(os.path.join(root, name))
                            shutil.copy(originalMoviePath, f".\\Movies\\{movieName}.mp4")
                            continue
                        else:
                            print(f"{Fore.RED}ERROR: Couldn't find {movieName} in any directory.")
                            continue

        if userInput == "4" or userInput == 4:

            settingLoop = True

            while settingLoop == True:

                terminalClear(0.5)

                print(f"""{Fore.YELLOW}1.{Fore.RESET} Open video in fullscreen at start time
{Fore.YELLOW}2.{Fore.RESET} Return to Menu
                """)

                settingsUserInput = input(f"What {Fore.YELLOW}mode{Fore.RESET} do you want to select? {Fore.YELLOW}(1-2){Fore.RESET} -> ")

                if settingsUserInput == "1" or settingsUserInput == 1:

                    terminalClear(0.5)

                    userInput = input(f"Do you want to {Fore.YELLOW}prioritize{Fore.RESET} fullscreen mode at watch time? {Fore.YELLOW}(Y/N){Fore.RESET} -> ").title()

                    if userInput == "Y" or userInput == "Yes":

                        fullscreenPreference = "True"

                        if os.path.exists(".\\settings"):
                            with open(".\\settings\\settings.py", "w")as file:
                                file.write(fullscreenPreference)
                        else:
                            try:
                                os.system("mkdir settings")
                                with open(".\\settings\\settings.py", "w")as file:
                                    file.write(fullscreenPreference)
                            except:
                                subprocess.call(["mkdir", "settings"])
                                with open(".\\settings\\settings.py", "w")as file:
                                    file.write(fullscreenPreference)
                    
                    if userInput == "N" or userInput == "No":
                        terminalClear(0.1)
                            
                if settingsUserInput == "2" or settingsUserInput == 2:
                    terminalClear(0)
                    settingLoop = False
                    loadingBar(0.15)
                    terminalClear(0.1)

        if userInput == "5" or userInput == 5:

            terminalClear(0)
            loadingMessage(0.3)
            time.sleep(0.2)
            sys.exit()

if __name__ == "__main__":
    Pyflix()
