from Factories.AbstractFactory import AbstractFactory

class File:
    def __init__(self, factory: AbstractFactory, title="Title", content="Paragraph1", footer="Footer", title_options=None, content_options=None, footer_options=None):
        self.factory = factory
        self.title = title
        self.content = content
        self.footer = footer
        self.title_options = title_options or {}
        self.content_options = content_options or {}
        self.footer_options = footer_options or {}

    def generate(self) -> None:
        self.factory.createTitle(self.title, **self.title_options)
        self.factory.createContent(self.content, **self.content_options)
        self.factory.createFooter(self.footer, **self.footer_options)

        self.factory.save()