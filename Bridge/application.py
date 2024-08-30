from Device import Tv, Radio
from Control import RemoteControl,AdvancedRemoteControl


tv = Tv()
remote = RemoteControl(tv)
remote.togglePower()

radio = Radio()
remote = AdvancedRemoteControl(radio)
