from abc import ABC, abstractmethod


# 定义数据源接口
class DataSource(ABC):

    @abstractmethod
    def write_data(self,data):
        pass

    @abstractmethod
    def read_data(self):
        pass


# 实现具体数据源
class FileDataSource(DataSource):
    def __init__(self, filename):
        self._filename = filename

    def write_data(self,data):
        with open(self._filename,'w') as f:
            f.write(data)

    def read_data(self):
        with open(self._filename,'r') as f:
            return f.read()
