from abc import ABC, abstractmethod


# command base class
class Command(ABC):
    """命令接口声明了执行命令的方法。"""

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# receiver
class TextEditor:
    """
    接收者类执行与操作相关的实际业务逻辑。
    """

    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text
        print(f"Text now: '{self.text}'")

    def delete_last(self, length):
        self.text = self.text[:-length]
        print(f"Text now: '{self.text}'")


# concrete command
class WriteCommand(Command):

    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text
        self.removed_length = len(text)

    def execute(self):
        self.editor.write(self.text)

    def undo(self):
        self.editor.delete_last(self.removed_length)


# Invoker
class CommandInvoker:
    """
    发送者负责启动命令。发送者不需要知道如何执行或撤销操作。
    """

    def __init__(self):
        self.history = []

    def store_and_execute(self, command: Command):
        self.history.append(command)
        command.execute()

    def undo_last(self):
        if self.history:
            command = self.history.pop()
            command.undo()


if __name__ == "__main__":
    editor = TextEditor()
    invoker = CommandInvoker()

    invoker.store_and_execute(WriteCommand(editor, "hello,"))
    invoker.store_and_execute(WriteCommand(editor, "world!"))

    invoker.undo_last()

    invoker.undo_last()
