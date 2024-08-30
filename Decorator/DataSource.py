from abc import ABC, abstractmethod


# 定义数据源接口
class DataSource(ABC):

    @abstractmethod
    def write_data(self,data):
        pass

    @abstractmethod
    def read_data(self):
        pass

