import subprocess
from modules.menu import Menu
from modules.network import Network

def main():
    menu = Menu()
    menu.LevelMenu()
    type = menu.ProbTypes[menu.ProbLevel]
    print("Fetching {} Problems".format(type.upper()))
    network = Network()
    network.fetchQues(type)
    print("Questions ")
    print("S.No.\t Name\t Code\n")
    for i,ques in enumerate(network.quesList):
        print("\t {} \t {} \n".format(ques["quesName"],ques["quesCode"]))

if __name__ == '__main__':
    main()
