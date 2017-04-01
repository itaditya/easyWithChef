import subprocess
class File():

    def __init__(self):
        self.project = {"location" : "F:/testing/"}
        self.filePath = ""

    def createFiles(self,quesCode):
        print("----")
        self.filePath = self.project["location"] + quesCode + ".c"
        template = ""
        with open("local/c-template.txt", "r") as fIn:
            template = fIn.read() + "\n"
        with open(self.filePath, "w") as fOut:
            fOut.write(template)

    def openFile(self):
        subprocess.Popen(
            ['subl', self.filePath])

def main():
    app = File()
    app.createFiles("START1")

if __name__ == '__main__':
    main()
