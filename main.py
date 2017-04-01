import subprocess
from modules.menu import Menu
from modules.network import Network
from modules.file import File

def main():
    menu = Menu()
    menu.LevelMenu()
    type = menu.ProbTypes[menu.ProbLevel]
    print("Fetching {} Problems".format(type.upper()))
    network = Network()
    file = File()
    try:
        network.fetchQuesList(type)
        choice = menu.QuesMenu(network.quesList)
        network.fetchQues(network.quesList[choice]["quesLink"])
        code = network.quesList[choice]["quesCode"]
        # file.createFiles(code)
        # file.openFile()
        network.runAns(code,"ad")
        raw_input(">>> ").lower().rstrip()
    finally:
        # pass
        network.driver.quit()


if __name__ == '__main__':
    main()
