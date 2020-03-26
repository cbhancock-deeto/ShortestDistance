# Cody Hancock | Student ID: #001087330

import Package
import csv

class Truck:
    # complexity: O(1)
    def __init__(self, packagesHeld):
       
        self.__packagesHeld = packagesHeld
        self.__timeDriving = 0
        self.__distanceDriven = 0
        self.__currentPkg = 0
        self.__currentMeridiem = 'AM'

    # receives an organized package List
    # sets status of packages to 'in route'
    # complexity: O(n)
    def loadTruck(self, packageList):
        self.__packagesHeld = packageList
        self.__currentPkg = 0
       
    # goes through and unloads each package, updating the time with each delivery
    # time should be received in format 'HH:MM'
    # complexity: O(n^2 + 3n) -> O(n^2)
    def truckRoute(self, leaveTime):

        # splice time to set hours and minutes
        self.__currentHour, minAndMerid = leaveTime.split(':')
        self.__currentHour = int(self.__currentHour)
        self.__currentMinute, self.__currentMeridiem = minAndMerid.split(' ')
        self.__currentMinute = float(self.__currentMinute)

        # complexity: O(n^2)
        self.sortPackages()

        # complexity: O(n)
        for pkg in self.__packagesHeld:
            packages_hash_table[hashing_func(pkg.pkgID)].pkgStatus = "in route"
            packages_hash_table[hashing_func(pkg.pkgID)].timeLeftHub = leaveTime

        # complexity: O(n)
        for pkg in range(len(self.__packagesHeld)):
            self.unloadCurrentPackage()

        # return to HUB
        self.__currentPkg -= 1

        distanceAddress = self.__packagesHeld[self.__currentPkg].pkgAddress
        
        # complexity: O(n)
        distanceToHub = float(self.findDistance(distanceAddress,distancesList[0][2]))

        self.__distanceDriven += distanceToHub
        self.__packagesHeld = []
        self.updateTime(distanceToHub)


    #complexity: O(1)
    def setPreviousAddress(self, currPackage):
        prevAddress = ""
        if currPackage == 0:
            prevAddress = str(distancesList[0][2])
        else:
            inputHash2 = self.__packagesHeld[currPackage - 1].pkgID
            idValue2 = hashing_func(inputHash2)
            prevAddress = str(packages_hash_table[idValue2].pkgAddress)
        return prevAddress

    # unloads the current package the truck is delivering
    # adds the time traveled to the __timeDriving class variable
    # adds the distance traveled to the __distanceDriven class variable
    # sets current package status to 'delivered'
    # sets the following package to current package
    # updates time associated with truck
    # complexity: O(n + 2) -> O(n)
    def unloadCurrentPackage(self):
       
        inputHash = self.__packagesHeld[self.__currentPkg].pkgID
        
        # complexity: O(1)
        idValue = hashing_func(inputHash)
        packages_hash_table[idValue].pkgStatus = "delivered"

        pkgNumber = self.__currentPkg

        prevAddress = self.setPreviousAddress(pkgNumber)
        currentAddress = str(packages_hash_table[idValue].pkgAddress)

        # complexity: O(n)
        newDistance = self.findDistance(prevAddress,currentAddress)

        # complexity: O(1)
        self.updateTime(float(newDistance))
        self.__distanceDriven += float(newDistance)

        packages_hash_table[idValue].timeDelivered = self.currentTime


      #E  print("current pkg: " + str(self.__currentPkg + 1) + " | package ID: " + self.__packagesHeld[self.__currentPkg].pkgID)
      #  print("new distance driven: " + str(newDistance) + " | total distance driven: " + str(self.distanceDriven))
      #  print("address: " + self.__packagesHeld[self.__currentPkg].pkgAddress + " | zip: " + self.__packagesHeld[self.__currentPkg].pkgZip)
     #   print("time delivered: " + self.currentTime + " | time due: " + str(packages_hash_table[idValue].pkgTime) + "\n")

        self.__currentPkg +=1

    # receives distance between current delivery and previous delivery,
    # using 18 mph as an assumption
    # complexity: O(1)
    def updateTime(self, newDistance):
        # 18 mph = 0.3 miles/minute 
        # -> 0.3/1 = 3.3333 minutes/mile ->  gets total minutes traveled for delivery
        mpm = 3.3333
        newTime = mpm * newDistance
        
        # use newTime to update currentHour, currentMinute, and currentMeridiem
        self.__currentMinute += newTime

        if self.__currentMinute >= 60:
            self.__currentMinute -= 60
            self.__currentHour += 1
        
        if self.__currentHour > 12:
            self.__currentHour -= 12
            self.__currentMeridiem = "PM"
        elif self.__currentHour == 12:
            self.__currentMeridiem = "PM"

    # mutators and accessors 
    @property
    def distanceDriven(self):
        return self.__distanceDriven
    @distanceDriven.setter
    def distanceDriven(self,distanceDriven):
        self.__distanceDriven = distanceDriven

    @property
    def currentMeridiem(self):
        return self.__currentMeridiem
    @currentMeridiem.setter
    def currentMeridiem(self,currMer):
        self.__currentMeridiem = currMer

    @property
    def timeToCheck(self):
        return self.__timeToCheck
    @timeToCheck.setter
    def timeToCheck(self,ttC):
        self.__timeToCheck = ttC

    @property
    def checkingTime(self):
        return self.__checkingTime
    @checkingTime.setter
    def checkingTime(self,ct):
        self.__checkingTime = ct

    @property
    def currentTime(self):
        mins = int(self.__currentMinute)
        if mins < 10:
            mins = '0' + str(mins)
        merid = str(self.currentMeridiem)
        currTime = str("0") + str(self.__currentHour) + ":" + str(mins) + " " + merid
        return currTime

    # finds the corresponding distance between the two points based on
    # string comparison from the distancesList
    # complexity: O(2n) -> O(n)
    def findDistance(self, address1, address2):
        counterX = 0
        # complexity: O(n)
        for x in distancesList:
            if str(address1) in str(x[0]):
                break
            counterX+=1

        counterY = 0
        # complexity: O(n)
        for y in distancesList[0]: 
            if str(address2) in str(y):
                break
            counterY+=1
        if distancesList[counterX][counterY]:
            return distancesList[counterX][counterY]
        return distancesList[counterY-1][counterX+1]

    # Loops through the pkgList and finds the package closest to the input address
    # complexity: O(n)
    def findLowestDistance(self,address,pkgList):
        lowestDistance = 10000
        counter = 0
        # O(n) complexity
        for pkg in range(len(pkgList)):
            distance = self.findDistance(address,pkgList[pkg].pkgAddress)
            if float(distance) < float(lowestDistance):
                lowestDistance = distance
                lowestDistanceID = counter
            counter+=1
        return lowestDistanceID


    # use a greedy algorithm to sort the packages in __packagesHeld
    # after loading truck - based on whichever package after is
    # the shortest distance
    # complexity: O(n + 2n^2) -> O(n^2)
    def sortPackages(self):
        # initialize a new package list
        tempPackageList = []
        tempPackageList2 = []
        tempPackageList3 = []

        # sort the early delivery packages into new package list first, removing them from package list
        # complexity: O(n)
        for pkg in self.__packagesHeld:
            if "EOD" not in pkg.pkgTime:
                if "9:00 AM" in pkg.pkgTime:
                    tempPackageList3.append(pkg)
                else:
                    tempPackageList.append(pkg)
            else:
                tempPackageList2.append(pkg)
        
        self.__packagesHeld = []

        sortedList1 = []
        sortedList2 = []


        # The first location will have WGU as the previous address
        prevAddress = str(distancesList[0][2])

        # find lowest distance
        # complexity: O(n * n) -> O(n^2)
        for pkgNumber in range(len(tempPackageList)):
            shortestDistanceID = self.findLowestDistance(prevAddress,tempPackageList)
            sortedList1.append(tempPackageList[shortestDistanceID])
            tempPackageList.remove(tempPackageList[shortestDistanceID])
            prevAddress = sortedList1[pkgNumber].pkgAddress

        tempPackageList = sortedList1

        # complexity: O(n * n) -> O(n^2)
        for pkgNumber2 in range(len(tempPackageList2)):
            shortestDistanceID = self.findLowestDistance(prevAddress,tempPackageList2)
            sortedList2.append(tempPackageList2[shortestDistanceID])
            tempPackageList2.remove(tempPackageList2[shortestDistanceID])
            prevAddress = sortedList2[pkgNumber2].pkgAddress

        tempPackageList2 = sortedList2

        # Add the two lists together to create optimally sorted packagelist
        self.__packagesHeld = tempPackageList3 + tempPackageList + tempPackageList2 


def pkgNotOnTime(pkg, numLate):
    print("packageID " + pkg.pkgID + " was not delivered on time")
    print("Actual delivery time: " + pkg.timeDelivered + " | Required delivery time: " + pkg.pkgTime)
    numLate += 1

def onTime():

  #  hrsToCheck, minAndMeridToCheck = ttC.split(':')
  #  minToCheck, meridToCheck = minAndMeridToCheck.split(' ')
    numberLate = 0
    for pkg in packages_hash_table:
        if pkg is None:
            continue
        # if time to be delivered is EOD then continue
        if 'EOD' in pkg.pkgTime:
            continue

        hrDelivered, mmDelivered = pkg.timeDelivered.split(':')
        minDelivered, meridDelivered = mmDelivered.split(' ')
        hrRequired, mmRequired = pkg.pkgTime.split(':')
        minRequired, meridRequired = mmRequired.split(' ')

        # if timeDelivered > requiredDeliveryTime ---> print "package x was not delivered on time"
        if int(hrRequired) < int(hrDelivered):
            pkgNotOnTime(pkg,numberLate)

        elif int(hrRequired) == int(hrDelivered):
            if int(minRequired) < int(minDelivered):
                pkgNotOnTime(pkg,numberLate)
            else:
                continue

        else:
            continue


    print(str(numberLate) + " packages delivered late")



# Hash function
# 41 was used as number of buckets for hash as is standard for a direct
# hash function (number of keys + 1)
def hashing_func(key):
    val = int(key) % 41
    return val

# hash table insert function
def insert_func(hashTbl, insertObj):

    key = insertObj.pkgID
    hashVal = hashing_func(key)
    hashTbl[hashVal] = insertObj

# lookup function
# input: hash table, packageID, package address, package time delivery requirement, package city, package zip code, package weight, and status of delivery
# returns: packageID, package address, package time delivery requirement, package city, package zip code, package weight, and status of delivery

def lookup_func(hashTbl, pkID, pkAddress, pkDeliveryDeadline, pkCity, pkZip, pkWeight, pkStatus):
    key = hashing_func(int(pkID))
    package = hashTbl[key]

    return package.pkgID, package.pkgAddress, package.pkgTime, package.pkgCity, package.pkgZip, package.pkgValue, package.pkgStatus


packages_hash_table = [None] * 41

# open file PkgVals.csv and parse the information into list of packages
# complexity: O(n)
with open('PkgVals.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # complexity: O(n)
    for row in csv_reader:
        pckg = Package.Package(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        
        # utilize insert function
        insert_func(packages_hash_table,pckg)


# open file distTable.csv and parse the information into a 2-dimensional list of distances between locations
# complexity: O(n^2)
with open('distTable.csv') as csv_file2:
    csv_reader2 = csv.reader(csv_file2,delimiter=',')
    
    #initialize 2-d array as none for each value:
    distancesList = [[None for x in range(30)] for y in range(30)] 
    counterRow = 1
    counter = 1
    #complexity O(n^2)
    for vals in csv_reader2:
        for x in vals:
            distancesList[counterRow-1][counter-1] = x
            counter += 1
            
        counter = 1
        counterRow+=1

# load packages onto trucks
# first packages chosen based on time due
# returns at end of 
t1r1PkgList = [packages_hash_table[15], packages_hash_table[13],\
    packages_hash_table[14],packages_hash_table[16],packages_hash_table[19],\
    packages_hash_table[20],packages_hash_table[40],packages_hash_table[1],\
    packages_hash_table[34],packages_hash_table[31],packages_hash_table[2],\
    packages_hash_table[4],packages_hash_table[5],packages_hash_table[7],\
    packages_hash_table[37],packages_hash_table[29]]

# second load for truck 1
t1r2PkgList = [packages_hash_table[27],packages_hash_table[28],\
    packages_hash_table[8],packages_hash_table[32],packages_hash_table[33],\
    packages_hash_table[35],packages_hash_table[10],packages_hash_table[9]]

# first load for truck 2
t2r1PkgList = [packages_hash_table[3], packages_hash_table[6], packages_hash_table[39],\
    packages_hash_table[11], packages_hash_table[12],packages_hash_table[17],\
    packages_hash_table[18],packages_hash_table[21],packages_hash_table[22],\
    packages_hash_table[23],packages_hash_table[24],packages_hash_table[25],\
    packages_hash_table[26],packages_hash_table[30],packages_hash_table[36],\
    packages_hash_table[38]]

yesOrNot = input("Would you like to run regular program (r), \
or check status of all packages at a specific time (s)")

# takes a time input and prints the status of all packages at a specific time
if(yesOrNot == "s"):

    ttC = input("Enter time to check (HH:mm AM/PM): ")

    hrsToCheck, minAndMeridToCheck = ttC.split(':')
    minToCheck, meridToCheck = minAndMeridToCheck.split(' ')

    truck1 = Truck(t1r1PkgList)
    truck2 = Truck(t2r1PkgList)

    truck1.truckRoute("8:00 AM")
    truck2.truckRoute("9:05 AM") # start time is 9:05 AM because of delay

    # The wrong delivery address for package #9, Third District Juvenile Court, 
    # will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
    if(int(hrsToCheck) >= 10) and (int(minToCheck) >= 20):
        key9 = 9
        hashVal = hashing_func(key9)
        packages_hash_table[hashVal].pkgAddress, \
            packages_hash_table[hashVal].pkgCity,\
            packages_hash_table[hashVal].pkgZip = \
                '410 S State St', 'Salt Lake City', '84111'

    truck1.loadTruck(t1r2PkgList)
    t1SecondLoadTime = truck1.currentTime
    truck1.truckRoute(truck1.currentTime)

    delay = "Delayed"

    #complexity: O(n)
    for pkg in packages_hash_table:
        if pkg is None:
            continue
        else:

            hrDelivered, minAndMeridDelivered = pkg.timeDelivered.split(':')
            minDelivered, meridDelivered = minAndMeridDelivered.split(' ')

            hrLeftHub, minAndMeridLeftHub = pkg.timeLeftHub.split(':')
            minLeftHub, meridLeftHub = minAndMeridLeftHub.split(' ')


            if int(hrsToCheck) > int(hrDelivered):
                pkg.pkgStatus = 'delivered'

            elif int(hrsToCheck) == int(hrDelivered):
                if int(minToCheck) >= int(minDelivered):
                    pkg.pkgStatus = 'delivered'
                elif int(hrsToCheck) < int(hrLeftHub):  
                    if int(minToCheck) < int(minLeftHub):
                        pkg.pkgStatus = 'AT HUB'
                else:
                    pkg.pkgStatus = 'in route'
            
            elif int(hrsToCheck) < int(hrDelivered):
                if int(hrsToCheck) < int(hrLeftHub):
                    pkg.pkgStatus = 'AT HUB'
                elif int(hrsToCheck) == int(hrLeftHub):
                    if int(minToCheck) > int(minLeftHub):
                        pkg.pkgStatus = 'in route'
                    else:
                        pkg.pkgStatus = 'AT HUB'
                elif int(hrsToCheck) > int(hrLeftHub):
                    pkg.pkgStatus = 'AT HUB'

        if int(hrsToCheck) < 9 and delay in pkg.pkgNote:
            pkg.pkgStatus = "Delayed in flight - not yet at HUB"
        elif int(hrsToCheck) == 9 and delay in pkg.pkgNote:
            if int(minToCheck) < 5:
                pkg.pkgStatus = "Delayed in flight - note yet at HUB"




    # Demostrate that all packages have been delivered,
    # their required delivery time,
    # as well as what time they were actually delivered at
    # complexity: O(n)
    for pk in packages_hash_table:
        if pk is None:
            continue
        else:
            print(pk.pkgID + " - " + pk.pkgAddress + ", " + pk.pkgState + \
                " " + pk.pkgZip + " | weight: " + pk.pkgValue + " | note: " + pk.pkgNote + \
                " | required delivery time: " + pk.pkgTime + \
                " actual delivery time: " + pk.timeDelivered + " | delivery status " + \
                pk.pkgStatus)
            
#regular program
elif(yesOrNot == "r"):
    truck1 = Truck(t1r1PkgList)
    truck2 = Truck(t2r1PkgList)

    # complexity: O(n^2)
    truck1.truckRoute("08:00 AM")

    # complexity: O(n^2)    
    truck2.truckRoute("09:05 AM") # start time is 9:05 AM because of delay

    # The wrong delivery address for package #9, Third District Juvenile Court, 
    # will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
    key9 = 9
    hashVal = hashing_func(key9)
    packages_hash_table[hashVal].pkgAddress, \
        packages_hash_table[hashVal].pkgCity,\
        packages_hash_table[hashVal].pkgZip = \
            '410 S State St', 'Salt Lake City', '84111'

    truck1.loadTruck(t1r2PkgList)
    # complexity: O(n^2)
    truck1.truckRoute(truck1.currentTime)

    # compare times delivered to times supposed to be delivered
    # if all packages delivered on time -> print "all packages delivered on time"
    # else: -> print "package(s) x was not delivered on time"



    print("t1 distance: " + str(truck1.distanceDriven))
    print("t2 distance: " + str(truck2.distanceDriven))
    print("total distance traveled: " + str(truck1.distanceDriven + truck2.distanceDriven))
    onTime()


else:
    print("incorrect letter entered, rerun program")


