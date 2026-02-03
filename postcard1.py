import webbrowser
import os

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
file_path = os.path.abspath("postcard.html")

webbrowser.get(chrome_path).open("file://" + file_path)
print("Postcard opened in Chrome 🌹")