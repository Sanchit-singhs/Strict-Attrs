# Strict Dataclass Utilities

This repository contains custom utilities for enhancing the functionality of Python's `dataclass` with strict type validation. The utilities provided here help in ensuring that data assigned to class attributes adheres strictly to the specified types.

## `strict_dataclass` Decorator

The `strict_dataclass` decorator combines the features of the `dataclass` and adds strict type validation. It is used to enforce the following:

- **Dataclass Functionality**: Adds the standard `dataclass` functionality to the decorated class.
- **Strict Type Validation**: Validates that the assigned values to class attributes match the specified types.

### Usage

```python
from strict_dataclass_utils import strict_dataclass

@strict_dataclass
class Example:
    name: str
    age: int
    data: dict
```

In the example above, the `Example` class will have the benefits of a regular `dataclass` and will perform strict type validation during initialization.

## `strict_attrs` Decorator

Similar to `strict_dataclass`, the `strict_attrs` decorator combines the features of the `attrs` library with strict type validation. It enforces the following:

- **Attrs Functionality**: Adds the functionality provided by the `attrs` library to the decorated class.
- **Strict Type Validation**: Validates that the assigned values to class attributes match the specified types.

### Usage

```python
from strict_dataclass_utils import strict_attrs

@strict_attrs
class Example:
    name: str
    age: int
    data: dict
```

In this example, the `Example` class benefits from both `attrs` and strict type validation.

## How it works

The decorators utilize type hints and annotations to perform type validation during object initialization. The validation ensures that the assigned values are instances of the specified types. If a type mismatch is detected, a `TypeError` is raised.

Feel free to explore and integrate these utilities into your projects for enhanced type safety with dataclasses and attrs.
