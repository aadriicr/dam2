"""

La abstracción consiste en captar las características y funcionalidades que un objeto
desempeña y estos son representados en clases por medio de atributos y métodos de dicha clase.



"""
from abc import ABC, abstractmethod


class Persona(ABC):

    @abstractmethod
    def setName(self, name):
        self.setName = name

    @abstractmethod
    def getName(self):
        return self.name

    def andar(self):
        print("Estoy andando")