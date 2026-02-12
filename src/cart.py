"""
Shopping cart and checkout system
"""

from typing import Dict, List, Optional
from datetime import datetime

class ShoppingCart:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.items = {}
        self.discount_codes = []
        self.shipping_address = None
        self.created_at = datetime.now()
    
    def add_item(
        self, 
        product_id: str, 
        quantity: int, 
        price: float,
        product_name: str = ""
    ) -> Dict:
        """
        Add item to cart
        
        BUGS TO FIND:
        - Negative quantity not handled
        - Zero quantity not handled
        - Negative price not validated
        - No inventory check
        - No maximum quantity limit
        """
        if product_id in self.items:
            self.items[product_id]["quantity"] += quantity
        else:
            self.items[product_id] = {
                "product_id": product_id,
                "product_name": product_name,
                "quantity": quantity,
                "price": price,
                "added_at": datetime.now()
            }
        
        return {"success": True, "item_count": len(self.items)}
    
    def remove_item(self, product_id: str) -> Dict:
        """
        Remove item from cart
        
        BUGS TO FIND:
        - No check if product exists
        - KeyError not handled
        """
        del self.items[product_id]
        return {"success": True}
    
    def update_quantity(self, product_id: str, new_quantity: int) -> Dict:
        """
        Update item quantity
        
        BUGS TO FIND:
        - Can set quantity to 0 or negative
        - Product existence not checked
        - No inventory validation
        """
        self.items[product_id]["quantity"] = new_quantity
        return {"success": True}
    
    def apply_discount_code(self, code: str, discount_percent: float) -> Dict:
        """
        Apply discount code to cart
        
        BUGS TO FIND:
        - Same discount can be applied multiple times
        - No expiration date check
        - Discount percent not validated (can be > 100)
        - No minimum purchase requirement
        """
        self.discount_codes.append({
            "code": code,
            "percent": discount_percent,
            "applied_at": datetime.now()
        })
        
        return {"success": True, "discount_applied": discount_percent}
    
    def calculate_subtotal(self) -> float:
        """
        Calculate cart subtotal before discounts
        
        BUGS TO FIND:
        - Empty cart not handled
        - Overflow not handled for large quantities
        """
        subtotal = sum(
            item["quantity"] * item["price"]
            for item in self.items.values()
        )
        return subtotal
    
    def calculate_discount(self) -> float:
        """
        Calculate total discount amount
        
        BUGS TO FIND:
        - Multiple discounts can stack (might be intentional or bug)
        - Discount can exceed subtotal
        """
        subtotal = self.calculate_subtotal()
        total_discount = 0
        
        for discount in self.discount_codes:
            discount_amount = subtotal * (discount["percent"] / 100)
            total_discount += discount_amount
        
        return total_discount
    
    def calculate_total(self, shipping_cost: float = 0.0, tax_rate: float = 0.0) -> Dict:
        """
        Calculate final cart total
        
        BUGS TO FIND:
        - Negative shipping cost not validated
        - Negative tax rate not validated
        - Total can be negative if discount > subtotal
        - Rounding issues not handled
        """
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        
        # BUG: Can go negative!
        amount_after_discount = subtotal - discount
        
        tax = amount_after_discount * (tax_rate / 100)
        total = amount_after_discount + tax + shipping_cost
        
        return {
            "subtotal": subtotal,
            "discount": discount,
            "tax": tax,
            "shipping": shipping_cost,
            "total": total
        }
    
    def set_shipping_address(self, address: Dict) -> Dict:
        """
        Set shipping address
        
        BUGS TO FIND:
        - No validation of address fields
        - Required fields not checked
        - Country/state validation missing
        """
        self.shipping_address = address
        return {"success": True}
    
    def checkout(self, payment_method: str) -> Dict:
        """
        Process checkout
        
        BUGS TO FIND:
        - Empty cart not checked
        - Shipping address not validated
        - Payment method not validated
        - Inventory not reserved/deducted
        - Cart not cleared after successful checkout
        - No order confirmation
        """
        total_info = self.calculate_total()
        
        order_id = f"ORD-{self.user_id}-{len(self.items)}"
        
        order = {
            "order_id": order_id,
            "user_id": self.user_id,
            "items": self.items.copy(),
            "total": total_info["total"],
            "shipping_address": self.shipping_address,
            "payment_method": payment_method,
            "status": "confirmed",
            "created_at": datetime.now()
        }
        
        # BUG: Cart not cleared!
        # BUG: Inventory not updated!
        
        return {
            "success": True,
            "order_id": order_id,
            "total": total_info["total"]
        }
    
    def clear_cart(self) -> Dict:
        """
        Clear all items from cart
        
        BUGS TO FIND:
        - Discount codes not cleared
        - Shipping address not cleared
        """
        self.items = {}
        # BUG: discount_codes and shipping_address not cleared!
        return {"success": True}
    
    def get_item_count(self) -> int:
        """
        Get total number of items in cart
        
        BUGS TO FIND:
        - Returns number of unique products, not total quantity
        """
        # BUG: Should return sum of quantities!
        return len(self.items)
    
    def validate_cart(self) -> Dict:
        """
        Validate cart before checkout
        
        BUGS TO FIND:
        - Incomplete validation
        - No inventory check
        - No price validation
        """
        if not self.items:
            return {"valid": False, "error": "Cart is empty"}
        
        if not self.shipping_address:
            return {"valid": False, "error": "Shipping address required"}
        
        # BUG: Should check inventory, validate prices, etc.
        
        return {"valid": True}
