from components.monitor import Monitor

def main():
    img = Monitor().takeScreenshot()
    filename = input("enter file name")
    img.save(f"./stateImages/{filename}.png")

if __name__== "__main__":
    main()
