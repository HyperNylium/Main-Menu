from tkinter import *
from tkinter.ttk import *
import customtkinter
import platform
import os
import time
import webbrowser
from datetime import date

customtkinter.set_appearance_mode("Dark")

# Text Colors
CLR_RED = "\033[31m"
CLR_GREEN = "\033[32m"
CLR_YELLOW = "\033[33m"
CLR_BLUE = "\033[34m"
CLR_CYAN = "\033[36m"
CLR_WHİTE = "\033[37m"
RESET_ALL = "\033[0m"

App_Version = "1.2"
PassGen ="PassGen.zip"
Website = "http://hypernylium.com/"
PassGenUrl = "http://www.hypernylium.com/Python-Projects/PassGen.zip"
UpdateUrl = "http://www.hypernylium.com/Python-Projects/MainMenu.zip"
dateNow = date.today()
GithubURL = "https://github.com/HyperNylium"
DiscordURL = "https://discord.gg/4FHTjAgw95"
instagramURL = "https://www.instagram.com/hypernylium__gg/"
YoutubeURL = "https://www.youtube.com/channel/UCpJ4F4dMn_DIhtrCJwDUK2A"

clear_command = "cls" if platform.system() == "Windows" else "clear"

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry('300x550+1100+50')
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        topMenu = Menu(self)
        self.config(menu=topMenu)

        submenu1 = Menu(topMenu)
        topMenu.add_cascade(menu=submenu1, label="File")
        nestedMenu = Menu(submenu1)
        submenu1.add_cascade(menu=nestedMenu, label='Sosial Media')
        nestedMenu.add_command(label="Github" , command=self.github)
        nestedMenu.add_command(label="Instagram" , command=self.instagram)
        nestedMenu.add_command(label="Discord" , command=self.discord)
        nestedMenu.add_command(label="YouTube" , command=self.youtube)
        submenu1.add_command(label="Commands", command=self.commands)
        submenu1.add_command(label="About", command=self.about)
        submenu1.add_command(label="Exit", command=quit)

        self.button_1 = customtkinter.CTkLabel(text="")
        self.button_1.grid(pady=20, padx=80)

        self.button_2 = customtkinter.CTkButton(text="PassGen", fg_color=("gray75", "gray30"), command=self.PassGen)
        self.button_2.grid(pady=15, padx=80)

        self.button_3 = customtkinter.CTkButton(text="Website", fg_color=("gray75", "gray30"), command=self.website)
        self.button_3.grid(pady=15, padx=80)

        self.button_3 = customtkinter.CTkButton(text="Time", fg_color=("gray75", "gray30"), command=self.time)
        self.button_3.grid(pady=15, padx=80)

        self.button_4 = customtkinter.CTkButton(text="Date", fg_color=("gray75", "gray30"), command=self.date)
        self.button_4.grid(pady=15, padx=80)

        self.button_5 = customtkinter.CTkButton(text="Update", fg_color=("gray75", "gray30"), command=self.update)
        self.button_5.grid(pady=15, padx=80)


    def about(self):
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
           os.system(clear_command)
           print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)
        if input__ == "y":
           os.system(clear_command)
           print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)

    def website(self):
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Web Launcher \n" + RESET_ALL)
        webbrowser.open(Website)
        time.sleep(1)
        print(CLR_GREEN + "   Launched Website " + RESET_ALL)
        time.sleep(3)
        os.system(clear_command)
        print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)

    def PassGen(self):
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "PassGen \n" + RESET_ALL)
        print(CLR_CYAN + "    please confirm you want to download the following" + RESET_ALL + CLR_YELLOW + " PassGen.zip " + RESET_ALL + CLR_CYAN +  "y/n" + RESET_ALL)
        input_ = input(CLR_YELLOW +"\n====> " + RESET_ALL)
        if input_ == "y":
            webbrowser.open(PassGenUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(3)
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)

        if input_ == "Y":
            webbrowser.open(PassGenUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(3)
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)
        if input_ == "n":
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)
        if input_ == "N":
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)

    def quit(self):
        os.system(clear_command)
        print(CLR_RED + "\n\n\n          Terminating App" + RESET_ALL)
        time.sleep(1)
        os.system(clear_command)
        self.destroy()

    def update(self):
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Updater \n" + RESET_ALL)
        print(CLR_CYAN + "    please confirm you want to update your software y/n" + RESET_ALL)
        input___ = input(CLR_YELLOW +"\n====> " + RESET_ALL)
        if input___ == "y":
            webbrowser.open(UpdateUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(3)
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)
        if input___ == "Y":
            webbrowser.open(UpdateUrl)
            time.sleep(1)
            print(CLR_GREEN + "\n   Launched " + RESET_ALL)
            time.sleep(3)
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)
        if input___ == "n":
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)
        if input___ == "N":
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)

    def time(self):
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Time \n" + RESET_ALL)
        print (time.strftime(CLR_YELLOW + "    %I:%M:%S") + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)
        if input__ == "y":
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)

    def commands(self):
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
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    Quit      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Closes app" + RESET_ALL + CLR_GREEN + "                                                |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    update    " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Downloads update files" + RESET_ALL + CLR_GREEN + "                                    |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    time      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the time" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   | " + RESET_ALL + CLR_CYAN + "    date      " + RESET_ALL + CLR_GREEN + " | " + RESET_ALL + CLR_YELLOW + "Brings up the date" + RESET_ALL + CLR_GREEN + "                                        |" + RESET_ALL)
        print(CLR_GREEN + "   +----------------+-----------------------------------------------------------+" + RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)
        if input__ == "y":
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)

    def date(self):
        os.system(clear_command)
        print(CLR_YELLOW + "\n  Today date is: ", dateNow, RESET_ALL)
        time.sleep(3)
        print(CLR_YELLOW + "\n  When you ready to go back to " + RESET_ALL + CLR_CYAN + "Main Menu " + RESET_ALL + CLR_YELLOW + "press 'Y' " + RESET_ALL)
        input__ = input("\n ====> ")
        if input__ == "Y":
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)
        if input__ == "y":
            os.system(clear_command)
            print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)

    def github(self):
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Web Launcher \n" + RESET_ALL)
        webbrowser.open(GithubURL)
        time.sleep(1)
        print(CLR_GREEN + "   Launched Website " + RESET_ALL)
        time.sleep(3)
        os.system(clear_command)
        print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)

    def youtube(self):
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Web Launcher \n" + RESET_ALL)
        webbrowser.open(YoutubeURL)
        time.sleep(1)
        print(CLR_GREEN + "   Launched Website " + RESET_ALL)
        time.sleep(3)
        os.system(clear_command)
        print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)

    def discord(self):
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Web Launcher \n" + RESET_ALL)
        webbrowser.open(DiscordURL)
        time.sleep(1)
        print(CLR_GREEN + "   Launched Website " + RESET_ALL)
        time.sleep(3)
        os.system(clear_command)
        print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)
    
    def instagram(self):
        os.system(clear_command)
        print(CLR_CYAN + "\n You are in " + RESET_ALL + CLR_YELLOW + "Web Launcher \n" + RESET_ALL)
        webbrowser.open(instagramURL)
        time.sleep(1)
        print(CLR_GREEN + "   Launched Website " + RESET_ALL)
        time.sleep(3)
        os.system(clear_command)
        print(CLR_GREEN + "\n   Awaiting commands" + RESET_ALL)



    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()