from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def createTitle(self, title_text, font_size, font_family, alignment):
        pass
    @abstractmethod    
    def createContent(self, title_text, font_size, font_family, alignment):
        pass
    @abstractmethod     
    def createFooter(self, title_text, font_size, font_family, alignment):
        pass
    @abstractmethod
    def save(self):
        pass