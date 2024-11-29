# Factory Pattern Implementation

This repository contains a Python implementation of the Factory Method design pattern, demonstrating its use with products like bicycles, motorcycles, and cars. Additionally, the repository includes unit tests to validate the functionality of the factory method and its derived classes.

## Features

### Core Features:
- **Factory Method Pattern**: Abstract class `Creator` that defines the interface for creating products, and concrete implementations for `BiciCreator`, `MotoCreator`, and `AutoCreator`.
- **Product Classes**: `BiciProduct`, `MotoProduct`, and `AutoProduct` represent different types of vehicles.
- **Abstract Factory**: `VehicleFactory` allows the creation of products dynamically based on a type string.
- **Product Registry**: Dynamically register and retrieve creators at runtime.
- **Serialization**: Includes methods to serialize and deserialize product data.
- **Error Handling**: Comprehensive error handling for invalid product creation.

### Additional Components:
- **Logging**: Tracks the creation and features of products.
- **Unit Testing**: Ensures reliability of the factory method implementation using Python's `unittest` module.

## Usage

### Prerequisites
- Python 3.8+

### Installation
Clone the repository and navigate to its directory:
```bash
git clone [<repository-url>](https://github.com/gpradinett/FactoryMethod.git)
cd FactoryMethod
```

### Running the Application
Execute the main script to see the factory method in action:
```bash
python factory_method.py
```

### Example Output
```plaintext
Catálogo de productos disponibles:
- {Bici Creada} con Características: pedal, Color: rojo
- {Moto Creada} con Características: Motor, Color: Negro
- {Auto creado} con Caracteristicas: Motor Avanzdo, Color: Azul
App: Lanzado con el BiciCreator.
Client: I'm not aware of the creator's class, but it still works.
[LOG] Creado: {Bici Creada}
Detalles del producto: Características: electrónica, Color: kaka
--------------------------------------------------
```

### Unit Tests
Run the tests to verify functionality:
```bash
python -m unittest test_factory_method.py
```

### Example Test Output
```plaintext
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## File Structure

```
.
├── factory_method.py       # Implementation of the Factory Method pattern
├── test_factory_method.py  # Unit tests for the Factory Method implementation
```

## Documentation

### Classes and Methods

#### Creator
Abstract base class that defines the interface for creating products.
- `factory_method()`: Abstract method for creating products.
- `some_operation()`: Demonstrates logging and error handling during product creation.

#### Concrete Creators
- `BiciCreator`: Creates instances of `BiciProduct`.
- `MotoCreator`: Creates instances of `MotoProduct`.
- `AutoCreator`: Creates instances of `AutoProduct`.

#### Product
Abstract base class for all products.
- `operation()`: Abstract method to define product-specific behavior.
- `to_dict()`: Serializes product attributes into a dictionary.
- `from_dict(cls, data)`: Deserializes product attributes from a dictionary.

#### Concrete Products
- `BiciProduct`: Represents a bicycle.
- `MotoProduct`: Represents a motorcycle.
- `AutoProduct`: Represents a car.

#### ProductRegistry
Provides a runtime registry to dynamically register and retrieve product creators.
- `register_creator(name, creator)`: Registers a creator under a given name.
- `get_creator(name)`: Retrieves a registered creator by name.

#### VehicleFactory
An abstract factory that dynamically creates products based on a type string.

### Tests
- `TestFactoryMethod`: Unit tests for `BiciCreator`, `MotoCreator`, and invalid product creation.

## License
This project is licensed under the MIT License.

## Author
Created by gpradinett.
