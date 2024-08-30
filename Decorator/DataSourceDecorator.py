from DataSource import DataSource
# 定义装饰基类
class DataSourceDecorator(DataSource):

    def __init__(self, source):
        self._wrappee = source

    def write_data(self, data):
        self._wrappee.write_data(data)

    def read_data(self):
        return self._wrappee.read_data()

# 实现具体压缩装饰
class CompressionDecorator(DataSourceDecorator):

    def write_data(self, data):
        # 添加压缩逻辑
        compressed_data = self._compress(data)
        self._wrappee.write_data(compressed_data)

    def read_data(self):
        compressed_data = self._wrappee.read_data()
        return self._decompress(compressed_data)

    def _compress(self, data):
        # 实现压缩逻辑
        return data

    def _decompress(self, compressed_data):
        # 实现解压逻辑
        return compressed_data

# 实现具体加密装饰

class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data):
        encrypted_data = self._encrypt(data)
        self._wrappee.write_data(encrypted_data)

    def read_data(self):
        encrypted_data = self._wrappee.read_data()
        return self._decrypt(encrypted_data)

    def _encrypt(self, data):
        # 实现加密逻辑
        return data

    def _decrypt(self, data):
        # 实现解密逻辑
        return data