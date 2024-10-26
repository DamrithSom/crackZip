import zipfile
import tkinter as tk
from tkinter import filedialog
from colorama import Fore, Style
import time
root = tk.Tk()
root.withdraw() 
def zip_file():  
    print(f"""{Fore.GREEN}
    ██████╗░░█████╗░░█████╗░███████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝
    ██║░░██║██║░░██║██║░░██║█████╗░░
    ██║░░██║██║░░██║██║░░██║██╔══╝░░
    ██████╔╝╚█████╔╝╚█████╔╝███████╗
    ╚═════╝░░╚════╝░░╚════╝░╚══════╝
    {Fore.RED}Coded By: {Fore.CYAN}Damrith Som
    {Fore.RED}Github: {Fore.CYAN} github.com/damrithsom
    {Fore.RED}Version: {Fore.CYAN}1.0""")  
    print("Cracking Zip Files")
    input("Press Enter to continue for selecting files and password list")
    files = filedialog.askopenfilename(title="Select Zip File")
    password = filedialog.askopenfilename(title="Select Password List")
    try:
        with zipfile.ZipFile(files) as file:
            with open(password, "r") as passfiles:
                pwd_ = passfiles.read().splitlines() 
                for _ in pwd_:
                    time.sleep(0.1)
                    try:
                        file.extractall(pwd=_.encode())
                        print(f"[{Fore.GREEN}+{Fore.GREEN}]Password found: {Fore.GREEN}{_}{Fore.GREEN}")
                        break
                    except Exception as e:
                        print(f"[{Fore.RED}-{Fore.RED}]Password not found: {Fore.RED}{_}{Fore.RED}")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    # for _ in range(1):
    #     threading.Thread(target=zip_file).start()
    zip_file()


