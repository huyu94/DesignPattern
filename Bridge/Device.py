from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def isEnabled(self) -> bool:
        pass
    @abstractmethod
    def enable(self):
        pass
    @abstractmethod
    def disable(self):
        pass
    @abstractmethod
    def getVolume(self):
        pass
    @abstractmethod
    def setVolume(self, volume):
        pass
    @abstractmethod
    def getChannel(self):
        pass
    @abstractmethod
    def setChannel(self, channel):
        pass


class Tv(Device):
    def __init__(self):
        self.volume = 0
        self.channel = 0
        self.enabled = False
    def isEnabled(self):
        return self.enabled
    def enable(self):
        self.enabled = True
    def disable(self):
        self.enabled = False
    def getVolume(self):
        return self.volume
    def setVolume(self, volume):
        self.volume = volume
    def getChannel(self):
        return self.channel
    def setChannel(self, channel):
        self.channel = channel

class Radio(Device):
    def __init__(self):
        self.volume = 0
        self.channel = 0
        self.enabled = False
    def isEnabled(self):
        return self.enabled
    def enable(self):
        self.enabled = True
    def disable(self):
        self.enabled = False
    def getVolume(self):
        return self.volume
    def setVolume(self, volume):
        self.volume = volume
    def getChannel(self):
        return self.channel
    def setChannel(self, channel):
        self.channel = channel

