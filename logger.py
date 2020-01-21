from enum import Enum 
from colorama import Fore, Style    

Types = Enum("Types", "error warning info debug")
typeMessageHeader = {
	Types.error : Fore.RED + "Error: ",
	Types.warning : Fore.YELLOW + "Warning: ",
	Types.info: Fore.GREEN + "Info: ",
	Types.debug: Fore.BLUE + "Debug: ",
}

def log(message, type):
	print(typeMessageHeader[type] + message + Style.RESET_ALL)

