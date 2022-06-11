
import time
import platform
import os
import webbrowser
from datetime import date


# Text Colors
CLR_RED = "\033[31m"
CLR_GREEN = "\033[32m"
CLR_YELLOW = "\033[33m"
CLR_BLUE = "\033[34m"
CLR_CYAN = "\033[36m"
CLR_WHİTE = "\033[37m"
RESET_ALL = "\033[0m"

PassGen ="PassGen.zip"
PassGenUrl = "http://www.hypernylium.com/Python-Projects/PassGen.zip"
App_Version = "1.2"
UpdateUrl = "http://www.hypernylium.com/Python-Projects/MainMenu.zip"
Website = "http://hypernylium.com/"
dateNow = date.today()

clear_command = "cls" if platform.system() == "Windows" else "clear"

def WelcomeScreen():
    os.system(clear_command)
    print(CLR_BLUE + "\n\n\n\n\n\n\n                .##......##....########....##..........######......#######.....##.....##....########")
    print("                .##..##..##....##..........##.........##....##....##.....##....###...###....##......")
    print("                .##..##..##....##..........##.........##..........##.....##....####.####....##......")
    print("                .##..##..##....######......##.........##..........##.....##....##.###.##....######..")
    print("                .##..##..##....##..........##.........##..........##.....##....##.....##....##......")
    print("                .##..##..##....##..........##.........##....##....##.....##....##.....##....##......")
    print("                ..###..###.....########....########....######......#######.....##.....##....########" + RESET_ALL)
    time.sleep(0.3)
    os.system(clear_command)
    print(CLR_RED + "\n\n\n\n\n\n\n                .##......##....########....##..........######......#######.....##.....##....########")
    print("                .##..##..##....##..........##.........##....##....##.....##....###...###....##......")
    print("                .##..##..##....##..........##.........##..........##.....##....####.####....##......")
    print("                .##..##..##....######......##.........##..........##.....##....##.###.##....######..")
    print("                .##..##..##....##..........##.........##..........##.....##....##.....##....##......")
    print("                .##..##..##....##..........##.........##....##....##.....##....##.....##....##......")
    print("                ..###..###.....########....########....######......#######.....##.....##....########" + RESET_ALL)
    time.sleep(0.3)
    os.system(clear_command)
    print(CLR_GREEN + "\n\n\n\n\n\n\n                .##......##....########....##..........######......#######.....##.....##....########")
    print("                .##..##..##....##..........##.........##....##....##.....##....###...###....##......")
    print("                .##..##..##....##..........##.........##..........##.....##....####.####....##......")
    print("                .##..##..##....######......##.........##..........##.....##....##.###.##....######..")
    print("                .##..##..##....##..........##.........##..........##.....##....##.....##....##......")
    print("                .##..##..##....##..........##.........##....##....##.....##....##.....##....##......")
    print("                ..###..###.....########....########....######......#######.....##.....##....########" + RESET_ALL)
    time.sleep(0.3)
    os.system(clear_command)
    print(CLR_CYAN + "\n\n\n\n\n\n\n                .##......##....########....##..........######......#######.....##.....##....########")
    print("                .##..##..##....##..........##.........##....##....##.....##....###...###....##......")
    print("                .##..##..##....##..........##.........##..........##.....##....####.####....##......")
    print("                .##..##..##....######......##.........##..........##.....##....##.###.##....######..")
    print("                .##..##..##....##..........##.........##..........##.....##....##.....##....##......")
    print("                .##..##..##....##..........##.........##....##....##.....##....##.....##....##......")
    print("                ..###..###.....########....########....######......#######.....##.....##....########" + RESET_ALL)
    time.sleep(0.3)
    os.system(clear_command)
    print(CLR_YELLOW + "\n\n\n\n\n\n\n                .##......##....########....##..........######......#######.....##.....##....########")
    print("                .##..##..##....##..........##.........##....##....##.....##....###...###....##......")
    print("                .##..##..##....##..........##.........##..........##.....##....####.####....##......")
    print("                .##..##..##....######......##.........##..........##.....##....##.###.##....######..")
    print("                .##..##..##....##..........##.........##..........##.....##....##.....##....##......")
    print("                .##..##..##....##..........##.........##....##....##.....##....##.....##....##......")
    print("                ..###..###.....########....########....######......#######.....##.....##....########" + RESET_ALL)
    time.sleep(0.3)
    os.system(clear_command)
    print(CLR_RED + "\n\n\n\n\n\n\n                .##...........#######........###.......########.....####....##....##.....######..")
    print("                .##..........##.....##......##.##......##.....##.....##.....###...##....##....##.")
    print("                .##..........##.....##.....##...##.....##.....##.....##.....####..##....##.......")
    print("                .##..........##.....##....##.....##....##.....##.....##.....##.##.##....##...####")
    print("                .##..........##.....##....#########....##.....##.....##.....##..####....##....##.")
    print("                .##..........##.....##....##.....##....##.....##.....##.....##...###....##....##.")
    print("                .########.....#######.....##.....##....########.....####....##....##.....######.." + RESET_ALL)
    time.sleep(2)
    os.system(clear_command)
    print(CLR_GREEN + "\n\n\n\n\n\n\n                .##...........#######........###.......########.....####....##....##.....######..")
    print("                .##..........##.....##......##.##......##.....##.....##.....###...##....##....##.")
    print("                .##..........##.....##.....##...##.....##.....##.....##.....####..##....##.......")
    print("                .##..........##.....##....##.....##....##.....##.....##.....##.##.##....##...####")
    print("                .##..........##.....##....#########....##.....##.....##.....##..####....##....##.")
    print("                .##..........##.....##....##.....##....##.....##.....##.....##...###....##....##.")
    print("                .########.....#######.....##.....##....########.....####....##....##.....######.." + RESET_ALL)
    time.sleep(1.5)
    MainScreen()

def MainScreen():
    os.system(clear_command)
    print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Main Menu \n" + RESET_ALL)
    print(CLR_CYAN + "   Please enter what you desire to do" + RESET_ALL)
    print(CLR_YELLOW + "\n   if you need help type 'help' " + RESET_ALL)
    input_ = input("\n ====> ")

    #~~~~~ About ~~~~~~#
    if input_ == "about":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "App Information \n" + RESET_ALL)
        print(CLR_RED + "    App version: " + App_Version + RESET_ALL + "\n\n")
        print(CLR_BLUE +"    .##.....##.##....##.########..########.########..##....##.##....##.##.......####.##.....##.##.....##")
        print(CLR_BLUE +"    .##.....##..##..##..##.....##.##.......##.....##.###...##..##..##..##........##..##.....##.###...###")
        print(CLR_BLUE +"    .##.....##...####...##.....##.##.......##.....##.####..##...####...##........##..##.....##.####.####")
        print(CLR_BLUE +"    .#########....##....########..######...########..##.##.##....##....##........##..##.....##.##.###.##")
        print(CLR_BLUE +"    .##.....##....##....##........##.......##...##...##..####....##....##........##..##.....##.##.....##")
        print(CLR_BLUE +"    .##.....##....##....##........##.......##....##..##...###....##....##........##..##.....##.##.....##")
        print(CLR_BLUE +"    .##.....##....##....##........########.##.....##.##....##....##....########.####..#######..##.....##" + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()
    if input_ == "About":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "App Information \n" + RESET_ALL)
        print(CLR_RED + "    App version: " + App_Version + RESET_ALL + "\n\n")
        print(CLR_BLUE +"    .##.....##.##....##.########..########.########..##....##.##....##.##.......####.##.....##.##.....##")
        print(CLR_BLUE +"    .##.....##..##..##..##.....##.##.......##.....##.###...##..##..##..##........##..##.....##.###...###")
        print(CLR_BLUE +"    .##.....##...####...##.....##.##.......##.....##.####..##...####...##........##..##.....##.####.####")
        print(CLR_BLUE +"    .#########....##....########..######...########..##.##.##....##....##........##..##.....##.##.###.##")
        print(CLR_BLUE +"    .##.....##....##....##........##.......##...##...##..####....##....##........##..##.....##.##.....##")
        print(CLR_BLUE +"    .##.....##....##....##........##.......##....##..##...###....##....##........##..##.....##.##.....##")
        print(CLR_BLUE +"    .##.....##....##....##........########.##.....##.##....##....##....########.####..#######..##.....##" + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()
    if input_ == "ABOUT":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "App Information \n" + RESET_ALL)
        print(CLR_RED + "    App version: " + App_Version + RESET_ALL + "\n\n")
        print(CLR_BLUE +"    .##.....##.##....##.########..########.########..##....##.##....##.##.......####.##.....##.##.....##")
        print(CLR_BLUE +"    .##.....##..##..##..##.....##.##.......##.....##.###...##..##..##..##........##..##.....##.###...###")
        print(CLR_BLUE +"    .##.....##...####...##.....##.##.......##.....##.####..##...####...##........##..##.....##.####.####")
        print(CLR_BLUE +"    .#########....##....########..######...########..##.##.##....##....##........##..##.....##.##.###.##")
        print(CLR_BLUE +"    .##.....##....##....##........##.......##...##...##..####....##....##........##..##.....##.##.....##")
        print(CLR_BLUE +"    .##.....##....##....##........##.......##....##..##...###....##....##........##..##.....##.##.....##")
        print(CLR_BLUE +"    .##.....##....##....##........########.##.....##.##....##....##....########.####..#######..##.....##" + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()

    #~~~~~ Website ~~~~~~#
    if input_ == "website":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Web Launcher \n" + RESET_ALL)
        webbrowser.open(Website)
        time.sleep(1)
        print(CLR_GREEN + "   Launched Website " + RESET_ALL)
        time.sleep(7)
        MainScreen()
    if input_ == "Website":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Web Launcher \n" + RESET_ALL)
        webbrowser.open(Website)
        time.sleep(1)
        print(CLR_GREEN + "   Launched Website " + RESET_ALL)
        time.sleep(7)
        MainScreen()
    if input_ == "WEBSITE":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Web Launcher \n" + RESET_ALL)
        webbrowser.open(Website)
        time.sleep(1)
        print(CLR_GREEN + "   Launched Website " + RESET_ALL)
        time.sleep(7)
        MainScreen()

    #~~~~~ PassGen ~~~~~~#
    if input_ == "PassGen":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "PassGen \n" + RESET_ALL)
        print(CLR_CYAN + "    please confirm you want to download the following" + RESET_ALL + CLR_YELLOW + " PassGen.zip " + RESET_ALL + CLR_CYAN +  "y/n" + RESET_ALL)
        input_ = input(CLR_YELLOW +"\n====> " + RESET_ALL)
        if input_ == "y":
            webbrowser.open(PassGenUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(7)
            MainScreen()
        if input_ == "Y":
            webbrowser.open(PassGenUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(7)
            MainScreen()
        if input_ == "n":
            MainScreen()
        if input_ == "N":
            MainScreen()
    if input_ == "passgen":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "PassGen \n" + RESET_ALL)
        print(CLR_CYAN + "    please confirm you want to download the following" + RESET_ALL + CLR_YELLOW + " PassGen.zip " + RESET_ALL + CLR_CYAN +  "y/n" + RESET_ALL)
        input_ = input(CLR_YELLOW +"\n====> " + RESET_ALL)
        if input_ == "y":
            webbrowser.open(PassGenUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(7)
            MainScreen()
        if input_ == "Y":
            webbrowser.open(PassGenUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(7)
            MainScreen()
        if input_ == "n":
            MainScreen()
        if input_ == "N":
            MainScreen()
    if input_ == "Passgen":
            os.system(clear_command)
            print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "PassGen \n" + RESET_ALL)
            print(CLR_CYAN + "    please confirm you want to download the following" + RESET_ALL + CLR_YELLOW + " PassGen.zip " + RESET_ALL + CLR_CYAN +  "y/n" + RESET_ALL)
            input_ = input(CLR_YELLOW +"\n====> " + RESET_ALL)
            if input_ == "y":
                webbrowser.open(PassGenUrl)
                time.sleep(1)
                print(CLR_GREEN + "\n   Launched " + RESET_ALL)
                time.sleep(7)
                MainScreen()
            if input_ == "Y":
                webbrowser.open(PassGenUrl)
                time.sleep(1)
                print(CLR_GREEN + "\n   Launched " + RESET_ALL)
                time.sleep(7)
                MainScreen()
            if input_ == "n":
                MainScreen()
            if input_ == "N":
                MainScreen()
    if input_ == "PASSGEN":
            os.system(clear_command)
            print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "PassGen \n" + RESET_ALL)
            print(CLR_CYAN + "    please confirm you want to download the following" + RESET_ALL + CLR_YELLOW + " PassGen.zip " + RESET_ALL + CLR_CYAN +  "y/n" + RESET_ALL)
            input_ = input(CLR_YELLOW +"\n====> " + RESET_ALL)
            if input_ == "y":
                webbrowser.open(PassGenUrl)
                time.sleep(1)
                print(CLR_GREEN + "\n   Launched " + RESET_ALL)
                time.sleep(7)
                MainScreen()
            if input_ == "Y":
                webbrowser.open(PassGenUrl)
                time.sleep(1)
                print(CLR_GREEN + "\n   Launched " + RESET_ALL)
                time.sleep(7)
                MainScreen()
            if input_ == "n":
                MainScreen()
            if input_ == "N":
                MainScreen()

    #~~~~~ Termination ~~~~~~#
    if input_ == "q":
        os.system(clear_command)
        print(CLR_RED + "\n\n\n          Terminating App" + RESET_ALL)
        time.sleep(1)
        os.system(clear_command)
        exit()
    if input_ == "Q":
        os.system(clear_command)
        print(CLR_RED + "\n\n\n          Terminating App" + RESET_ALL)
        time.sleep(1)
        os.system(clear_command)
        exit()
    if input_ == "exit":
        os.system(clear_command)
        print(CLR_RED + "\n\n\n          Terminating App" + RESET_ALL)
        time.sleep(1)
        os.system(clear_command)
        exit()
    if input_ == "Exit":
        os.system(clear_command)
        print(CLR_RED + "\n\n\n          Terminating App" + RESET_ALL)
        time.sleep(1)
        os.system(clear_command)
        exit()
    if input_ == "EXİT":
        os.system(clear_command)
        print(CLR_RED + "\n\n\n          Terminating App" + RESET_ALL)
        time.sleep(1)
        os.system(clear_command)
        exit()

    #~~~~~ Update ~~~~~~#
    if input_ == "update":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Updater \n" + RESET_ALL)
        print(CLR_CYAN + "    please confirm you want to update your software y/n" + RESET_ALL)
        input___ = input(CLR_YELLOW +"\n====> " + RESET_ALL)
        if input___ == "y":
            webbrowser.open(UpdateUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(7)
            MainScreen()
        if input___ == "Y":
            webbrowser.open(UpdateUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(7)
            MainScreen()
        if input___ == "n":
            MainScreen()
        if input___ == "N":
            MainScreen()
    if input_ == "Update":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Updater \n" + RESET_ALL)
        print(CLR_CYAN + "    please confirm you want to update your software y/n" + RESET_ALL)
        input___ = input(CLR_YELLOW +"\n====> " + RESET_ALL)
        if input___ == "y":
            webbrowser.open(UpdateUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(7)
            MainScreen()
        if input___ == "Y":
            webbrowser.open(UpdateUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(7)
            MainScreen()
    if input_ == "UPDATE":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Updater \n" + RESET_ALL)
        print(CLR_CYAN + "    please confirm you want to  update your software y/n" + RESET_ALL)
        input___ = input(CLR_YELLOW +"\n====> " + RESET_ALL)
        if input___ == "y":
            webbrowser.open(UpdateUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(7)
            MainScreen()
        if input___ == "Y":
            webbrowser.open(UpdateUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(7)
            MainScreen()

    #~~~~~ Time ~~~~~~#
    if input_ == "time":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Time \n" + RESET_ALL)
        print (time.strftime(CLR_YELLOW + "    %I:%M:%S") + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()
    if input_ == "Time":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Time \n" + RESET_ALL)
        print (time.strftime(CLR_YELLOW + "    %I:%M:%S") + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()
    if input_ == "TİME":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Time \n" + RESET_ALL)
        print (time.strftime(CLR_YELLOW + "    %I:%M:%S") + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()

    #~~~~~ Date ~~~~~~#
    if input_ == "date":
        os.system(clear_command)
        print(CLR_YELLOW + "\n  Today date is: ", dateNow, RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()
    if input_ == "Date":
        os.system(clear_command)
        print(CLR_YELLOW + "\n  Today date is: ", dateNow, RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()
    if input_ == "DATE":
        os.system(clear_command)
        print(CLR_YELLOW + "\n  Today date is: ", dateNow, RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()

    #~~~~~ Help ~~~~~~#
    if input_ == "help":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Help" + RESET_ALL)
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Help\n" + RESET_ALL)
        print(CLR_GREEN + "   +----------------+-----------------------------------------------------------+" + RESET_ALL)
        print(CLR_GREEN + "   |    COMMANDS    |                           OUTPUT                          |" + RESET_ALL)
        print(CLR_GREEN + "   +----------------+-----------------------------------------------------------+" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    Help      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the help section that you are viewing right now" + RESET_ALL + CLR_GREEN + " |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    about     " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up app info" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    website   " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Sends you to my website" + RESET_ALL + CLR_GREEN + "                                   |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    PassGen   " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Downloads my program" + RESET_ALL + CLR_CYAN + " PassGen" + RESET_ALL + CLR_GREEN + "                              |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    exit(q)   " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Closes app" + RESET_ALL + CLR_GREEN + "                                                |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    update    " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Downloads update files" + RESET_ALL + CLR_GREEN + "                                    |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    time      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the time" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    date      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the date" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   +----------------+-----------------------------------------------------------+" + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()
    if input_ == "Help":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Help" + RESET_ALL)
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Help\n" + RESET_ALL)
        print(CLR_GREEN + "   +----------------+-----------------------------------------------------------+" + RESET_ALL)
        print(CLR_GREEN + "   |    COMMANDS    |                           OUTPUT                          |" + RESET_ALL)
        print(CLR_GREEN + "   +----------------+-----------------------------------------------------------+" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    Help      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the help section that you are viewing right now" + RESET_ALL + CLR_GREEN + " |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    about     " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up app info" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    website   " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Sends you to my website" + RESET_ALL + CLR_GREEN + "                                   |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    PassGen   " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Downloads my program" + RESET_ALL + CLR_CYAN + " PassGen" + RESET_ALL + CLR_GREEN + "                              |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    exit(q)   " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Closes app" + RESET_ALL + CLR_GREEN + "                                                |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    update    " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Downloads update files" + RESET_ALL + CLR_GREEN + "                                    |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    time      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the time" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    date      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the date" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   +----------------+-----------------------------------------------------------+" + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()
    if input_ == "HELP":
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Help" + RESET_ALL)
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Help\n" + RESET_ALL)
        print(CLR_GREEN + "   +----------------+-----------------------------------------------------------+" + RESET_ALL)
        print(CLR_GREEN + "   |    COMMANDS    |                           OUTPUT                          |" + RESET_ALL)
        print(CLR_GREEN + "   +----------------+-----------------------------------------------------------+" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    Help      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the help section that you are viewing right now" + RESET_ALL + CLR_GREEN + " |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    about     " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up app info" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    website   " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Sends you to my website" + RESET_ALL + CLR_GREEN + "                                   |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    PassGen   " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Downloads my program" + RESET_ALL + CLR_CYAN + " PassGen" + RESET_ALL + CLR_GREEN + "                              |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    exit(q)   " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Closes app" + RESET_ALL + CLR_GREEN + "                                                |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    update    " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Downloads update files" + RESET_ALL + CLR_GREEN + "                                    |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    time      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the time" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    date      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the date" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   +----------------+-----------------------------------------------------------+" + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            MainScreen()
        if input__ == "y":
            MainScreen()

MainScreen()