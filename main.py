from fileManager import *

instance = FileManager()

str = input()

instance.WriteFile("C:/Dev/Python/filemanager/test.txt", str)

instance.OpenFile("C:/Dev/Python/filemanager/test.txt")