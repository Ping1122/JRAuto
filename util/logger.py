from enum import Enum

Types = Enum("Types", "error warning info debug verbose")

typeMessageHeader = {
	Types.error : "Error: ",
	Types.warning : "Warning: ",
	Types.info: "",
	Types.verbose: "",
	Types.debug: "Debug: ",
}

def log(message, type):
	print(typeMessageHeader[type] + message)
