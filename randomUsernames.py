import numpy as np
import random
import linecache

# Create a script that generates a random username of the following:
# <adjective><animal>(2 digit num)

def generateUserNames(amount):
        userNamesToReturn = []
        adjectivesFile = open("word-bank/words/english-adjectives.txt", "r")
        animalsFile = open("word-bank/words/animals.txt", "r")
        adjectivesFileCnt = sum(1 for line in adjectivesFile)
        animalsFileCnt = sum(1 for line in animalsFile)

        print("************************ Adjective Count: %i ************************" % adjectivesFileCnt)
        print("************************ Animals Count: %i ************************" % animalsFileCnt)

        for i in range(0, amount):
                adjective = linecache.getline("word-bank/words/english-adjectives.txt", random.randint(0, adjectivesFileCnt - 1))
                animal = linecache.getline("word-bank/words/animals.txt", random.randint(0, animalsFileCnt - 1))
                number = random.randint(0, 99)
                if (number < 10):
                        number = str(0) + str(number)
                # Build the username so that it's presentable like AdjectiveAnimal01
                userName = adjective.title().replace("-", "").strip() + animal.title().replace("-", "").strip() + str(number)
                userNamesToReturn.append(userName.replace(" ", ""))

        return userNamesToReturn

def main():
        print("************************ Usernames Generated ************************")
        amount = 100
        usernames = generateUserNames(amount)
        cnt = 0
        for username in usernames:
                cnt = cnt + 1
                print(str(cnt) + ". " + username)

main()