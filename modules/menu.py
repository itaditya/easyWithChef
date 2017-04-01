import subprocess
import sys
class Menu():

    def __init__(self):
        self.ProbLevel = 0
        self.ProbTypes = ["school","easy","medium","hard","extcontest"]

    def LevelMenu(self):
        while True:
            print("\nSelect Ques Type\n(B)eginner\n(E)asy\n(M)edium\n(H)ard\n(P)eers\n(Q)uit")
            choice = raw_input(">>> ").lower().rstrip()
            if choice=="q":
                sys.exit()
            elif choice=="b":
                self.ProbLevel = 0
                break
            elif choice=="e":
                self.ProbLevel = 1
                break
            elif choice=="m":
                self.ProbLevel = 2
                break
            elif choice=="h":
                self.ProbLevel = 3
                break
            elif choice=="p":
                self.ProbLevel = 4
                break
            else:
                print("Invalid choice, please choose again\n")

        print("==================")

    def QuesMenu(self,quesList):
        while True:
            total = len(quesList)
            print("Select Question 1 to {} or  0 to quit".format(total))
            print("S.No.\t Name\t\t Code\n")
            for i,ques in enumerate(quesList):
                print("{})\t {} \t {} \n".format(i+1,ques["quesName"],ques["quesCode"]))
            choice = int(raw_input(">>> ").lower().rstrip())
            if choice==0:
                sys.exit()
            elif choice > 0 and choice <= total:
                return(choice - 1)
            else:
                print("Invalid choice, please choose again\n")

        print("==================")
        

def main():
    app = Menu()


if __name__ == '__main__':
    main()
