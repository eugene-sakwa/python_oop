# python_oop
Tutorial to learn a OOP and how to implement it using Python.
# 🧠 Python OOP Practice Project

This is a simple Python project built as a learning exercise to understand and apply core concepts of Object-Oriented Programming (OOP), including encapsulation, inheritance, class/instance attributes, and data validation.

## 📦 Project Structure

```bash
.
├── item.py         # Defines the Item class
├── phone.py        # Defines the Phone class, which inherits from Item
├── main.py         # Script to run and test the classes
├── items.csv       # CSV file used for class instantiation
├── helper.py       # (Optional) Helper functions (if any used later)
└── README.md       # This file
```

## 🧱 Concepts Demonstrated

### ✅ Encapsulation
- Attributes like `__name` and `__price` are made private.
- Property decorators are used to define controlled access via getters and setters.

### ✅ Inheritance
- The `Phone` class extends the `Item` class, inheriting common behavior and adding `broken_phones` attribute.

### ✅ Class and Instance Attributes
- Class-level `pay_rate` is shared across instances unless overridden.
- All created instances are tracked in `Item.all`.

### ✅ Data Validation
- Assertions are used to ensure that `price`, `quantity`, and `broken_phones` are non-negative.
- Setter methods raise exceptions if invalid data is provided.

## 🧪 Example Usage

```python
from item import Item

item1 = Item("MyItem", 750)
item1.apply_increament(0.2)

print(item1.price)  # Expected to show incremented price
```

```python
from phone import Phone

phone1 = Phone("iPhone", 999, 5, 1)
print(phone1)
```

## 🛉 Notes

- `__pycache__/` is ignored using `.gitignore` for a clean repository.
- This code is for educational purposes and may not handle all edge cases in production.

