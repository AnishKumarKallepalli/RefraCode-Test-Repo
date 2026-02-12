"""
Inventory management system
"""

from typing import Dict, List, Optional
from datetime import datetime

class Inventory:
    def __init__(self):
        self.products = {}
        self.reservations = {}
        self.low_stock_threshold = 10
    
    def add_product(
        self,
        product_id: str,
        name: str,
        quantity: int,
        price: float,
        category: str = "general"
    ) -> Dict:
        """
        Add new product to inventory
        
        BUGS TO FIND:
        - Negative quantity not validated
        - Negative price not validated
        - Duplicate product_id not checked
        - Name can be empty
        """
        self.products[product_id] = {
            "id": product_id,
            "name": name,
            "quantity": quantity,
            "price": price,
            "category": category,
            "reserved": 0,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        return {"success": True, "product_id": product_id}
    
    def update_stock(self, product_id: str, quantity_change: int) -> Dict:
        """
        Update product stock quantity
        
        BUGS TO FIND:
        - Product existence not checked
        - Can make stock negative
        - Reserved stock not considered
        """
        self.products[product_id]["quantity"] += quantity_change
        self.products[product_id]["updated_at"] = datetime.now()
        
        return {"success": True, "new_quantity": self.products[product_id]["quantity"]}
    
    def check_availability(self, product_id: str, requested_qty: int) -> Dict:
        """
        Check if product is available in requested quantity
        
        BUGS TO FIND:
        - Product existence not checked
        - Reserved stock not considered
        - Negative quantity not handled
        """
        product = self.products[product_id]
        available = product["quantity"] >= requested_qty
        
        return {
            "available": available,
            "in_stock": product["quantity"],
            "requested": requested_qty
        }
    
    def reserve_stock(self, product_id: str, quantity: int, order_id: str) -> Dict:
        """
        Reserve stock for an order
        
        BUGS TO FIND:
        - Availability not checked before reserving
        - Can reserve more than available
        - Stock can go negative
        - Reservation can be made multiple times for same order
        """
        if product_id not in self.products:
            return {"success": False, "error": "Product not found"}
        
        # BUG: Not checking if enough stock available!
        self.products[product_id]["quantity"] -= quantity
        self.products[product_id]["reserved"] += quantity
        
        reservation_id = f"RES-{order_id}-{product_id}"
        self.reservations[reservation_id] = {
            "product_id": product_id,
            "quantity": quantity,
            "order_id": order_id,
            "created_at": datetime.now()
        }
        
        return {"success": True, "reservation_id": reservation_id}
    
    def release_reservation(self, reservation_id: str) -> Dict:
        """
        Release a stock reservation
        
        BUGS TO FIND:
        - Reservation existence not checked
        - Stock not returned to available
        """
        reservation = self.reservations[reservation_id]
        product_id = reservation["product_id"]
        quantity = reservation["quantity"]
        
        # BUG: Not returning stock to available!
        self.products[product_id]["reserved"] -= quantity
        
        del self.reservations[reservation_id]
        
        return {"success": True}
    
    def update_price(self, product_id: str, new_price: float) -> Dict:
        """
        Update product price
        
        BUGS TO FIND:
        - Product existence not checked
        - Negative price not validated
        - No price history tracking
        """
        self.products[product_id]["price"] = new_price
        self.products[product_id]["updated_at"] = datetime.now()
        
        return {"success": True, "new_price": new_price}
    
    def get_low_stock_products(self) -> List[Dict]:
        """
        Get list of products with low stock
        
        BUGS TO FIND:
        - Reserved stock not considered in calculation
        - Threshold is hardcoded
        """
        low_stock = []
        
        for product in self.products.values():
            if product["quantity"] < self.low_stock_threshold:
                low_stock.append({
                    "product_id": product["id"],
                    "name": product["name"],
                    "quantity": product["quantity"]
                })
        
        return low_stock
    
    def bulk_update_prices(self, price_changes: Dict[str, float]) -> Dict:
        """
        Update multiple product prices at once
        
        BUGS TO FIND:
        - Product existence not checked for each
        - Negative prices not validated
        - Partial failure not handled (some succeed, some fail)
        """
        updated = []
        
        for product_id, new_price in price_changes.items():
            # BUG: No validation!
            self.products[product_id]["price"] = new_price
            updated.append(product_id)
        
        return {"success": True, "updated_count": len(updated)}
    
    def transfer_stock(
        self,
        from_product_id: str,
        to_product_id: str,
        quantity: int
    ) -> Dict:
        """
        Transfer stock between products (for variants, etc.)
        
        BUGS TO FIND:
        - Product existence not checked
        - Negative quantity not validated
        - Can transfer more than available
        - Source stock can go negative
        """
        self.products[from_product_id]["quantity"] -= quantity
        self.products[to_product_id]["quantity"] += quantity
        
        return {"success": True}
