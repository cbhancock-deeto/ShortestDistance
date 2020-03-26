# Cody Hancock | Student ID: #001087330

class Package:
    def __init__(self,pkgID, pkgAddress, pkgCity, pkgState, pkgZip, pkgTime, pkgValue, pkgNote):
        self.pkgID = pkgID
        self.pkgAddress = pkgAddress
        self.pkgCity = pkgCity
        self.pkgState = pkgState
        self.pkgZip = pkgZip
        self.pkgTime = pkgTime
        self.pkgValue = pkgValue
        self.pkgNote = pkgNote
        self.pkgStatus = "At hub"
        self.timeDelivered = "n/a"
        self.timeLeftHub = "n/a"

    @property
    def timeLeftHub(self):
        return self.__timeLeftHub
    @timeLeftHub.setter
    def timeLeftHub(self,timeLeftHub):
        self.__timeLeftHub = timeLeftHub

    @property
    def timeDelivered(self):
        return self.__timeDelivered
    @timeDelivered.setter
    def timeDelivered(self,deliveryTime):
        self.__timeDelivered = deliveryTime

    @property
    def pkgStatus(self):
        return self.__pkgStatus
    @pkgStatus.setter
    def pkgStatus(self,status):
        self.__pkgStatus = status

    @property
    def pkgID(self):
        return self.__pkgID
    @pkgID.setter
    def pkgID(self,pkgID):
        self.__pkgID = pkgID

    @property
    def pkgAddress(self):
        return self.__pkgAddress
    @pkgAddress.setter
    def pkgAddress(self, pkgAddress):
        self.__pkgAddress = pkgAddress
    

    @property
    def pkgCity(self):
        return self.__pkgCity
    @pkgCity.setter
    def pkgCity(self, pkgCity):
        self.__pkgCity = pkgCity


    @property
    def pkgState(self):
        return self.__pkgState
    @pkgState.setter
    def pkgState(self, pkgState):
        self.__pkgState = pkgState
    

    @property
    def pkgZip(self):
        return self.__pkgZip
    @pkgZip.setter
    def pkgZip(self, pkgZip):
        self.__pkgZip = pkgZip


    @property
    def pkgTime(self):
        return self.__pkgTime
    @pkgTime.setter
    def pkgTime(self, pkgTime):
        self.__pkgTime = pkgTime


    @property
    def pkgValue(self):
        return self.__pkgValue
    @pkgValue.setter
    def pkgValue(self,pkgValue):
        self.__pkgValue = pkgValue
    
    @property
    def pkgNote(self):
        return self.__pkgNote
    @pkgNote.setter
    def pkgNote(self,pkgNote):
        self.__pkgNote = pkgNote


