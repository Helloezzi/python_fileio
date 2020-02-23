class FileManager:
    def __init_(self):
        self.result = 0

    def WriteFile(self, path, str):
        f = open(path, 'x')
        f.write(str)
        f.close()

    def OpenFile(self, path):
        f = open(path, 'r')
        data = f.read()
        print(data)
        f.close()