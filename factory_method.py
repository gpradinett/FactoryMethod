from __future__ import annotations
from abc import ABC, abstractmethod
import logging


class Creator(ABC):
    
    @abstractmethod
    def factory_method(self):
        pass
    
    """
    Manejo de Errores
    """
    def some_operation(self) -> str:
        try:
            product = self.factory_method()
            logging.info(f"[LOG] Creado: {product.operation()}")
            print(" logs para registrar la creación de productos.", logging.info)    
            result = f"[Creator] la misma clase creater  funciona con {product.operation()}"
            return result
        except Exception as e:
            return f"[Error] No se pudo crear el producto: {e}"

"""
 Fábrica Abstracta
"""

class AbstractFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Product:
        pass

class VehicleFactory(AbstractFactory):
    def create_vehicle(self, type_: str) -> Product:
        if type_ == "bici":
            return BiciProduct()
        elif type_ == "moto":
            return MotoProduct()
        else:
            raise ValueError(f"Tipo de vehículo no soportado: {type_}")

"""
"""

class ProductRegistry:
    _creators = {}

    @classmethod
    def register_creator(cls, name: str, creator: Creator):
        cls._creators[name] = creator

    @classmethod
    def get_creator(cls, name: str) -> Creator:
        return cls._creators.get(name, None)


"""
"""

class BiciCreator(Creator):
    
    def __init__(self, color: str = "rojo", caracteristica: str = "pedal") -> None:
        self.color = color
        self.caracteristica = caracteristica
    
    def factory_method(self) -> Product:
        return BiciProduct(self.color, self.caracteristica)

class MotoCreator(Creator):
    def factory_method(self):
        return MotoProduct()
        
class AutoCreator(Creator):
    def factory_method(self):
        return AutoProduct()


"""
"""

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass
    
    @abstractmethod
    def to_dic(self) -> dict:
        pass
    
    """
    Serialización de Productos
    """
    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> Product:
        pass

class BiciProduct(Product):
    
    def __init__(self, color: str, caracteristica: str) -> None:
        self.color = color
        self.caracteristica = caracteristica
        self._validate()
    
    def _validate(self) -> None:
        if not self.caracteristica or not self.color:
            raise ValueError("La bicicleta debe tener características válidas")
    
    def operation(self) -> str:
        return "{Bici Creada}"
    
    def get_features(self) -> str:
        return f"Características: {self.caracteristica}, Color: {self.color}"
    
    def to_dic(self) -> dict:
        return {"type": "bici", "color": self.color, "caracteristica": self.caracteristica}

    def from_dict(cls, data: dict) -> Product:
        return cls(color=data["color"], caracteristica=data["caracteristica"])

class MotoProduct(Product):
    def __init__(self, color="Negro", caracteristica="100cc"):
        if not caracteristica.endswith("cc"):
            raise ValueError("La potencia debe especificarse en 'cc'")
        self.color = "Negro"
        self.caracteristica = "Motor"
        
    
    def operation(self) -> str:
        return "{Moto Creada}"
    """
    def get_features(self) -> str:
        return f"Color: {self.color}, Potencia: {self.potencia}"
    """
    def get_features(self) -> str:
        return f"Características: {self.caracteristica}, Color: {self.color}"

    def to_dic(self) -> dict:
        return {"type": "bici", "color": self.color, "caracteristica": self.caracteristica}

    def from_dict(cls, data: dict) -> Product:
        return cls(color=data["color"], caracteristica=data["caracteristica"])


class AutoProduct(Product):
    def __init__(self) -> None:
        self.carateristacas = "Motor Avanzdo"
        self.color = "Azul"
        
    def  operation(self) -> str:
        return "{Auto creado}"
    
    def get_features(self) -> str:
        return f"Caracteristicas: {self.carateristacas}, Color: {self.color}"

    def to_dic(self) -> dict:
        return {"type": "bici", "color": self.color, "caracteristica": self.caracteristica}

    def from_dict(cls, data: dict) -> Product:
        return cls(color=data["color"], caracteristica=data["caracteristica"])


"""
"""

def list_products(creators: list[Creator]) -> None:
    print("Catálogo de productos disponibles:")
    for creator in creators:
        product = creator.factory_method()
        print(f"- {product.operation()} con {product.get_features()}")


def order(creator: Creator) -> None:
    product = creator.factory_method()
    
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}\n"
          f"Detalles del producto: {product.get_features()}", end="")
    print("-" * 50)



if __name__ == "__main__":
    creators = [BiciCreator(), MotoCreator(), AutoCreator()]
    list_products(creators)
    
    print("App: Lanzado con el BiciCreator.")
    #order(BiciCreator())
    order(BiciCreator(color="kaka", caracteristica="electrónica"))
    print("\n")
    """
    print("App: Lanzado con el MotoCreator.")
    order(MotoCreator())
    print("\n")
    
    print("App: Lanzado con el AutoCreator.")
    order(AutoCreator())
    """
    ProductRegistry.register_creator("bici", BiciCreator())
    print("1: ",ProductRegistry)
    ProductRegistry.register_creator("moto", MotoCreator())
    print("2: ",ProductRegistry)
    ProductRegistry.register_creator("auto", AutoCreator())
    print("3: ",ProductRegistry)
    
    # Selección en tiempo de ejecución
    selected_creator = ProductRegistry.get_creator("moto")
    if selected_creator:
        order(selected_creator)
