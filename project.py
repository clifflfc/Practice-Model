
partnerdata = [
['north1',2,3,4,9,'True','north'],
['north2',3,2.9,5,7,'True','north'],
['north3',2,3,4,10,'True','north'],
['central',2,3,4,9,'False','central'],
['south1',2,3,4,9,'True','south'],
['south2',3,2.9,5,7,'True','south'],
['east1',2,3,4,9,'True','east']
]

def bestpartner(weight,region,cod):
    weightchoice = 0
    sublist = []
    sublist2 = []
    sublist3 = []
    bestprice = 0
    bestscore = 0


    #to determine weight category
    if int(weight) < 5:
        weightchoice = 1
    elif 5 < int(weight) < 20:
        weightchoice = 2
    elif int(weight) > 20:
        weightchoice = 3

    #to filter based on COD & region requirement
    for i in partnerdata:
        if str(cod) == i[5] and str(region) == i[6]:
            sublist.append(i)


    if len(sublist) == 0:
        print ("No Partner")

    else:
        #to filter for min cost
        for i in sublist:
            if bestprice == 0:
                bestprice = i[weightchoice]
            elif i[weightchoice] < bestprice:
                bestprice = i[weightchoice]

        #to filter out partners matching min cost
        for i in sublist:
            if i[weightchoice] == bestprice:
                sublist2.append(i)

        for i in sublist2:
            if len(sublist2) == 1:
                print('The best partner is')
                print(i[0])
                return(i[0])

            if len(sublist2) > 1:
                if bestscore == 0:
                    bestscore = i[4]
                elif i[4] > bestscore:
                    bestscore = i[4]

        for i in sublist2:
            if i[4] == bestscore:
                print('The best partner is')
                print(i[0])
                return(i[0])


def find_partner():

##weight validation
    valid = False
    while not valid:
        weight = input('Please input the parcel weight: ')

        if len(weight) == 0 or int(weight) > 100:
            continue
        valid = True

#region validation
    valid = False
    while not valid:
        region = input('Please input the parcel region (Please enter either north, south, east, west, central): ')
        if len(region) == 0 or str.isalpha(region) == False:
            continue
        valid = True

#COD validation
    valid = False
    while not valid:
        cod = input('Is COD required? (Please enter True or False): ')
        if len(cod) == 0 or str.isalpha(region) == False:
            continue
        valid = True


    return bestpartner(weight, region, cod)

find_partner()
