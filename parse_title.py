import csv


def check_if_stock(str): #checks if given string is an existing stock
    inputs = str.lower()
    result = False

    with open('list_stocks.csv', 'r') as csv_file:# opens csv file
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            split_name = line[2].split(" ") #splits full stock name

            if(split_name[0].lower() == inputs): # checks if first word in full stock name is same as given string
                result = True

            if (line[1].lower() == inputs): #checks if ticker is the same
                result = True
    return result


def parse_title(title): # preforms check_if_stock on all phrases in a title and returns all results in list
    title_list = title.split(" ")
    list_stocks_title = []
    for x in range(0, len(title_list)):
        if(check_if_stock(title_list[x]) == True): # checks if word is a stock
            list_stocks_title.append(title_list[x].lower()) #adds to list

    return list_stocks_title

def false_positive(list_stock):
    blacklist_words = [
        "YOLO", "TOS", "CEO", "CFO", "CTO", "DD", "BTFD", "WSB", "OK", "RH",
        "KYS", "FD", "TYS", "US", "USA", "IT", "ATH", "RIP", "BMW", "GDP",
        "OTM", "ATM", "ITM", "IMO", "LOL", "DOJ", "BE", "PR", "PC", "ICE",
        "TYS", "ISIS", "PRAY", "PT", "FBI", "SEC", "GOD", "NOT", "POS", "COD",
        "AYYMD", "FOMO", "TL;DR", "EDIT", "STILL", "LGMA", "WTF", "RAW", "PM",
        "LMAO", "LMFAO", "ROFL", "EZ", "RED", "BEZOS", "TICK", "IS", "DOW"
        "AM", "PM", "LPT", "GOAT", "FL", "CA", "IL",
        "PDFUA", "MACD", "HQ",
        "OP", "DJIA", "PS", "AH", "TL", "DR", "JAN", "FEB", "JUL", "AUG",
        "SEP", "SEPT", "OCT", "NOV", "DEC", "FDA", "IV", "ER", "IPO", "RISE"
        "IPA", "URL", "MILF", "BUT", "SSN", "FIFA", "USD",
        "CPU", "AT",
        "GG", "ELON", "A", "FOR", "DD"
    ]
    for i in range(0, len(list_stock)):#use a better algorithm alphabetical search
        for j in range(0, len(blacklist_words)):
            if (blacklist_words[j] == list_stock[i].upper()):
                list_stock[i] = '';


