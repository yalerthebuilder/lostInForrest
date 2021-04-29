# this program is to calculate the average, min and highest steps of each map stimulation
def selector(file1, file2, file3, file4, file5):
    print("Enter 1 for 300 map results")
    print("Enter 2 for 500 map results")
    print("Enter 3 for hard map results")
    print("Enter 4 for hell map results")
    print("Enter 5 for customized map results")
    option = input("Which results you want to analyze:\n ")
    while True:
        if option not in ["1", "2", "3", "4", "5"]:
            print("Option not valid, re-enter your option")
            option = input("Which results you want to analyze:\n ")

        if option == "1":
            file = file1
            break
        elif option == "2":
            file = file2
            break
        if option == "3":
            print("3 slected")
            file = file3
            break
        if option == "4":
            file = file4
            break
        if option == "5":
            file = file5
            break
    return file


def dataSorter(dataList):
    print("Your highest steps: " + str(max(dataList)))
    print("Your lowest steps: " + str(min(dataList)))
    print("Your average steps: " + str(sum(dataList) / len(dataList)))


def returnData():
    file1 = "results/300results.txt"
    file2 = "results/500results.txt"
    file3 = "results/hardresults.txt"
    file4 = "results/hellresults.txt"
    file5 = "results/randomMap.txt"
    file = selector(file1, file2, file3, file4, file5)
    counter = 0
    player2_dataList = []
    player3_dataList = []
    player4_dataList = []
    with open(file, "r") as r:
        content = r.readlines()
        for line in content:
            counter += 1
            dataLine = line.split(" ")
            if dataLine[2] == "two":
                player2_dataList.append(int(dataLine[0]))
            if dataLine[2] == "three":
                player3_dataList.append(int(dataLine[0]))
            if dataLine[2] == "four":
                player4_dataList.append(int(dataLine[0]))

        if len(player2_dataList) > 0:
            print("For Player 2:")
            dataSorter(player2_dataList)
        if len(player3_dataList) > 0:
            print("For Player 4:")
        if len(player4_dataList) > 0:
            print("For Player 4:")
            dataSorter(player3_dataList)

    anotherSearch = input("Want start another search? 'y' for yes, 'any key' for no")
    if anotherSearch in ["y", "yes", "Y", "YES", "Yes"]:
        returnData()
    else:
        print("Thanks for using data analyser")

    if counter == 0:
        print("Oops, your data is empty, want try another file?")
        returnData()


returnData()
