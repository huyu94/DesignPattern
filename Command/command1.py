from abc import ABC, abstractmethod

class Command(ABC):

    def __init__(self, app, editor):
        self.app = app
        self.editor = editor


    def save_backup(self):
        self.backup = self.editor.text

    def undo(self):
        self.editor.text = self.backup

    @abstractmethod
    def execute(self):
        pass


class copyCommand(Command):
    def execute(self):
        self.app.clipboard = self.editor.get_selection()
        return False

class CutCommand(Command):
    def execute(self):
        self.save_backup()
        self.app.clipboard = self.editor.get_selection()
        self.editor.delete_selection()
        return True

class PasteCommand(Command):
    def execute(self):
        self.save_backup()
        self.editor.replace_selection(self.app.clipboard)
        return True

class UndoCommand(Command):
    def execute(self):
        self.app.undo()
        return False

class CommandHistory:
    def __init__(self):
        self.history = []

    def push(self, command):
        self.history.append(command)

    def pop(self):
        if self.history:
            return self.history.pop()
        else:
            return None


def Editor:
    def __init__(self):
        self.text = ""

    def get_selection(self):
        return "Selected Text"

    def delete_selection(self):
        pass

    def replace_selection(self, text):
        self.text = text


class Application:
    def __init__(self):
        self.clipboard = ""
        self.editor = []
        self.active_editor = Editor()
        self.history = CommandHistory()


    def create_ui(self):
        pass # 这里假设我们有某种UI，实际中应连接到UI事件

    def execute_command(self, command):
        if command.execute():
            self.history.push(command)

    def undo(self):
        command =self.history.pop()
        if command is not None:
            command.undo()

