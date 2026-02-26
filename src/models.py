from utils import id_mapping

class LineItem:
    def __init__(self, name: str, quantity: int, unit: str) -> None:
        assert isinstance(name, str)
        assert isinstance(quantity, int)
        assert isinstance(unit, str)
        
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.product_id = None
        self.set_product_id()

    def get_name(self) -> str:
        return self.name
    
    def set_name(self, new_name: str) -> None:
        assert isinstance(new_name, str)
        self.name = new_name
        self.set_product_id()
    
    def get_quantity(self) -> int:
        return self.quantity
    
    def set_quantity(self, new_quantity: int) -> None:
        assert isinstance(new_quantity, int)
        self.quantity = new_quantity

    def get_unit(self) -> str:
        return self.unit

    def set_unit(self, new_unit: str) -> None:
        assert isinstance(new_unit, str)
        self.unit = new_unit

    def get_product_id(self) -> int | None:
        return self.product_id

    def set_product_id(self) -> None:
        product_id = id_mapping.get(self.name, 0)
        
        if product_id == 0:
            raise ValueError(f"Product '{self.name}' not found in the database.")
        else:
            self.product_id = product_id