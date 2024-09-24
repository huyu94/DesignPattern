class ComponentWithContextualHelp:
    """处理者接口声明了一个创建处理者链的方法。还声明了一个执行请求的方法。"""
    def show_help(self):
        raise NotImplementedError()


class Component(ComponentWithContextualHelp):
    """简单组件的基础类。"""
    def __init__(self):
        self.tooltip_text = None
        self.container = None

    def show_help(self):
        """
        如果组件设定了帮助文字，那它将会显示提示信息。如果组件没有帮助文字
        且其容器存在，那它会将调用传递给容器。
        """
        if self.tooltip_text is not None:
            # 显示提示信息
            print(self.tooltip_text)
        elif self.container is not None:
            self.container.show_help()


class Container(Component):
    """
    容器可以将简单组件和其他容器作为其子项目。链关系将在这里建立。该类将从
    其父类处继承 showHelp（显示帮助）的行为。
    """

    def __init__(self):
        super().__init__()
        self.children = []

    def add(self, child):
        self.children.append(child)
        child.container = self


class Button(Component):
    """原始组件应该能够使用帮助操作的默认实现……"""

    def __init__(self, x, y, width, height, text):
        super().__init__()


class Panel(Container):
    def __init__(self,x,y,width, height):
        super().__init__()
        self.modal_help_text = None

    def show_help(self):
        if self.modal_help_text is not None:
            # 显示包含帮助文字的模态窗口。
            print(self.modal_help_text)
        else:
            super().show_help()

class Dialog(Container):
    """……同上……"""

    def __init__(self, title):
        super().__init__()
        self.wiki_page_url = None

    def show_help(self):
        if self.wiki_page_url is not None:
            # 打开百科帮助页面。
            print(f"打开维基百科页面：{self.wiki_page_url}")
        else:
            super().show_help()


class Application:
    """客户端代码。"""

    def create_ui(self):
        """每个程序都能以不同方式对链进行配置。"""
        dialog = Dialog("预算报告")
        # dialog.wiki_page_url = "http://..."
        panel = Panel(0, 0, 400, 800)
        panel.modal_help_text = "本面板用于..."
        ok = Button(250, 760, 50, 20, "确认")
        ok.tooltip_text = "这是一个确认按钮..."
        cancel = Button(320, 760, 50, 20, "取消")
        # ……
        panel.add(ok)
        panel.add(cancel)
        dialog.add(panel)

        return panel

    def on_f1_key_press(self):
        """想象这里会发生什么。"""
        component = self.get_component_at_mouse_coords()
        component.show_help()

    def get_component_at_mouse_coords(self):
        #  获取鼠标位置的组件逻辑
        #  这里只是一个示例，你需要根据实际情况实现
        return self.create_ui()


if __name__ == "__main__":
    app = Application()
    # app.create_ui()
    app.on_f1_key_press()