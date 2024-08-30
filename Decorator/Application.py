from DataSource import FileDataSource
from DataSourceDecorator import CompressionDecorator,EncryptionDecorator
# 简单示例类
class Application:

    def dumb_usage_example(self):
        source = FileDataSource("somefile.dat")
        source.write_data("salaryRecords")

        source = CompressionDecorator(source)
        source.write_data("salaryRecords")

        source = EncryptionDecorator(source)
        source.write_data("salaryRecords")

# 工资管理器类
class SalaryManager:

    def __init__(self, source):
        self._source = source

    def load(self):
        return self._source.read_data()

    def save(self, salary_records):
        self._source.write_data(salary_records)


# 应用配置类
class ApplicationConfigurator:

    def configuration_example(self, enabled_encryption, enabled_compression):
        source = FileDataSource("salary.dat")

        if enabled_encryption:
            source = EncryptionDecorator(source)

        if enabled_compression:
            source = CompressionDecorator(source)

        logger = SalaryManager(source)
        salary = logger.load()
        return salary