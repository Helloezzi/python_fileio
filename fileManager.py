class FileManager:
    def WriteFile(self, path, str):
        f = open(path, 'w')
        f.write(str)
        f.close()

    def OpenFile(self, path):
        f = open(path, 'r')
        data = f.read()
        print("data:" + data)
        f.close()