# Псевдокод
from abc import ABC, abstractmethod

# интерфейс компонента
class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self): # показывает подсказку
        pass

class Component(ComponentWithContextualHelp):

    container = None
    tooltip_text: str | None = None

    def __init__(self, tooltip_text=None):
        self.tooltip_text = tooltip_text # Сохраняет текст

    def show_help(self):

        # если есть подсказка
        if self.tooltip_text is not None:
            print("Показать подсказку:", self.tooltip_text)

        # иначе передаем запрос контейнеру
        elif self.container:
            self.container.show_help()


# контейнер
class Container(Component):
    children = []
    def add(self, child: Component):
        # добавляем дочерний элемент
        self.children.append(child)
        child.container = self

# кнопка
class Button(Component):
    pass

class Panel(Container):
    modal_help_text: str | None = None
    def __init__(self, modal_help_text=None): # показывает модальное окно или передает дальше
        self.modal_help_text = modal_help_text

    def show_help(self):
        if self.modal_help_text is not None:
            print("Показать модальное окно:", self.modal_help_text)
        else:
            Container.show_help(self)

class Dialog(Container):
    wiki_page_url: str | None = None
    def __init__(self, wiki_page_url=None): #сохраняет ссылку
        self.wiki_page_url = wiki_page_url
    def show_help(self):
        if self.wiki_page_url is not None:
            print("Открыть wiki:", self.wiki_page_url) # открывает ссылку
        else:
            Container.show_help(self)

dialog = Dialog("Budget Reports")
dialog.wiki_page_url = "http://..."
panel = Panel("This panel does...")
ok = Button("This is an OK button that...")
cancel = Button("This is a Cancel button that...")

panel.add(ok)
panel.add(cancel)
dialog.add(panel)

print("Кнопка OK (есть подсказка):")
ok.show_help()

print("\nКнопка Cancel (есть подсказка):")
cancel.show_help()

print("\nНовая кнопка без подсказки:")
new_btn = Button()
panel.add(new_btn)
new_btn.show_help()