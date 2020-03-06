from win32gui import GetWindowText, GetWindowRect, EnumWindows

window = []

def callback(hwnd, extra):
	global window
	print(GetWindowText(hwnd))
	print(GetWindowRect(hwnd))
	if "夜神模拟器" in GetWindowText(hwnd):
		window = GetWindowRect(hwnd)

def main():
    EnumWindows(callback, None)
    print(window)

if __name__ == '__main__':
    main()