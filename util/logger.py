from colorama import Fore, Style
from enum import Enum

Types = Enum("Types", "error warning info debug verbose")

typeMessageHeader = {
	Types.error : Fore.RED + "Error: ",
	Types.warning : Fore.YELLOW + "Warning: ",
	Types.info: Fore.GREEN,
	Types.verbose: Fore.CYAN,
	Types.debug: Fore.BLUE + "Debug: ",
}

def log(message, type):
	print(typeMessageHeader[type] + message + Style.RESET_ALL)
