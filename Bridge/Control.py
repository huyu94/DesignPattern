class RemoteControl:
    def __init__(self, device):
        self._device = device

    def togglePower(self):
        if self._device.isEnabled():
            self._device.disable()
        else:
            self._device.enable()

    def volumeDown(self):
        self._device.setVolume(self._device.getVolume() - 10)
    def volumeUp(self):
        self._device.setVolume(self._device.getVolume() + 10)
    def channelDown(self):
        self._device.setChannel(self._device.getChannel() - 1)
    def channelUp(self):
        self._device.setChannel(self._device.getChannel() + 1)

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self._device.setVolume(0)



