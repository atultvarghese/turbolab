def server_cost(start,end):
    dmystart = start.split(" ")
    dmyend = end.split(" ")
    days = (int(dmyend[0]) - int(dmystart[0]))
    month = (int(dmyend[1]) - int(dmystart[1]))
    year = (int(dmyend[2]) - int(dmystart[2]))
    if year > 1:
        return 20000

    elif month > 1:
            return month * 1000
    elif days > 1:
            return days * 30
    else:
        return 20

if __name__ == "__main__":
    # start = input()
    # end = input()
    start = "6 6 2020"
    end = "9 6 2020"
    print(server_cost(start,end))