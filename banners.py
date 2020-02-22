import random

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

figlet_ansi_shadow = """

 █████╗  █████╗ ██████╗     ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████║███████║██████╔╝    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══██║██╔══██║██╔═══╝     ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║██║  ██║██║         ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝         ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                                                                 
"""

figlet_big = """
                     _____    ______ _           _           
     /\        /\   |  __ \  |  ____(_)         | |          
    /  \      /  \  | |__) | | |__   _ _ __   __| | ___ _ __ 
   / /\ \    / /\ \ |  ___/  |  __| | | '_ \ / _` |/ _ \ '__|
  / ____ \  / ____ \| |      | |    | | | | | (_| |  __/ |   
 /_/    \_\/_/    \_\_|      |_|    |_|_| |_|\__,_|\___|_|   
                                                             
                                                               
"""

figlet_bloody = """
 ▄▄▄      ▄▄▄       ██▓███       █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███  
▒████▄   ▒████▄    ▓██░  ██▒   ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▒██  ▀█▄ ▒██  ▀█▄  ▓██░ ██▓▒   ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
░██▄▄▄▄██░██▄▄▄▄██ ▒██▄█▓▒ ▒   ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
 ▓█   ▓██▒▓█   ▓██▒▒██▒ ░  ░   ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
 ▒▒   ▓▒█░▒▒   ▓▒█░▒▓▒░ ░  ░    ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒   ▒▒ ░ ▒   ▒▒ ░░▒ ░         ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
  ░   ▒    ░   ▒   ░░           ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
      ░  ░     ░  ░                    ░           ░    ░       ░  ░   ░     
                                                      ░                      
                                                                             
"""

figlet_doom = """
      ___    ___  ______  ______ _           _           
     / _ \  / _ \ | ___ \ |  ___(_)         | |          
    / /_\ \/ /_\ \| |_/ / | |_   _ _ __   __| | ___ _ __ 
    |  _  ||  _  ||  __/  |  _| | | '_ \ / _` |/ _ \ '__|
    | | | || | | || |     | |   | | | | | (_| |  __/ |   
    \_| |_/\_| |_/\_|     \_|   |_|_| |_|\__,_|\___|_|   
                                                     
                                                     
"""

figlet_drpepper = """
     ___  ___  ___   ___  _         _           
    | . || . || . \ | __><_>._ _  _| | ___  _ _ 
    |   ||   ||  _/ | _> | || ' |/ . |/ ._>| '_>
    |_|_||_|_||_|   |_|  |_||_|_|\___|\___.|_|        

"""

figlet_standard = """
     _        _    ____    _____ _           _           
    / \      / \  |  _ \  |  ___(_)_ __   __| | ___ _ __ 
   / _ \    / _ \ | |_) | | |_  | | '_ \ / _` |/ _ \ '__|
  / ___ \  / ___ \|  __/  |  _| | | | | | (_| |  __/ |   
 /_/   \_\/_/   \_\_|     |_|   |_|_| |_|\__,_|\___|_|  
 
"""                                                      

def get_banner():
    print(random.choice([figlet_ansi_shadow, figlet_big, figlet_doom, figlet_drpepper, figlet_standard]))
    print(f"{YELLOW}  [***********************************************************]  \n")
    print(f"{WHITE}      [{RED}DISCLAIMER{WHITE}] : {RED}Illegal use is stricly prohibited")
    print(f"{WHITE}      [{RED}AUTHOR{WHITE}] : {WHITE}Pushpender Singh")
    print(f"{WHITE}      [{RED}TOOl NAME{WHITE}] : {RED}AAPFinder {WHITE}(Advanced Admin Page Finder)")
    print(f"{WHITE}      [{RED}GITHUB{WHITE}] : {GREEN}https://github.com/Technowlogy-Pushpender\n")
    print(f"{YELLOW}  [***********************************************************]  \n")