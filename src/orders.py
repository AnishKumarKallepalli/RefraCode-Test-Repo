"""
Order processing and management system
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
from enum import Enum

class OrderStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"

class OrderProcessor:
    def __init__(self):
        self.orders = {}
        self.order_counter = 0
    
    def create_order(
        self,
        user_id: int,
        items: List[Dict],
        shipping_address: Dict,
        payment_method: str,
        total_amount: float
    ) -> Dict:
        """
        Create a new order
        
        BUGS TO FIND:
        - Empty items list not validated
        - Negative total amount not validated
        - Shipping address fields not validated
        - Payment method not validated
        - User ID not validated
        """
        self.order_counter += 1
        order_id = f"ORD-{self.order_counter:06d}"
        
        order = {
            "id": order_id,
            "user_id": user_id,
            "items": items,
            "shipping_address": shipping_address,
            "payment_method": payment_method,
            "total_amount": total_amount,
            "status": OrderStatus.PENDING.value,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
            "estimated_delivery": datetime.now() + timedelta(days=7)
        }
        
        self.orders[order_id] = order
        
        return {"success": True, "order_id": order_id}
    
    def update_order_status(self, order_id: str, new_status: str) -> Dict:
        """
        Update order status
        
        BUGS TO FIND:
        - Order existence not checked
        - Status transition validation missing (can go from shipped to pending)
        - Invalid status values not validated
        - Notification not sent
        """
        self.orders[order_id]["status"] = new_status
        self.orders[order_id]["updated_at"] = datetime.now()
        
        return {"success": True, "new_status": new_status}
    
    def cancel_order(self, order_id: str, reason: str = "") -> Dict:
        """
        Cancel an order
        
        BUGS TO FIND:
        - Can cancel already shipped orders
        - Refund not processed
        - Inventory not returned
        - Order existence not checked
        """
        order = self.orders[order_id]
        
        # BUG: No status check!
        order["status"] = OrderStatus.CANCELLED.value
        order["cancellation_reason"] = reason
        order["cancelled_at"] = datetime.now()
        
        # BUG: Inventory not returned!
        # BUG: Payment not refunded!
        
        return {"success": True}
    
    def get_order(self, order_id: str) -> Optional[Dict]:
        """
        Get order details
        
        BUGS TO FIND:
        - Order existence not checked (KeyError)
        """
        return self.orders[order_id]
    
    def get_user_orders(self, user_id: int) -> List[Dict]:
        """
        Get all orders for a user
        
        BUGS TO FIND:
        - No pagination (can return huge list)
        - No sorting options
        """
        user_orders = [
            order for order in self.orders.values()
            if order["user_id"] == user_id
        ]
        
        return user_orders
    
    def add_tracking_info(
        self,
        order_id: str,
        carrier: str,
        tracking_number: str
    ) -> Dict:
        """
        Add shipping tracking information
        
        BUGS TO FIND:
        - Order existence not checked
        - Order status not validated (should be shipped)
        - Tracking number format not validated
        - Carrier not validated
        """
        self.orders[order_id]["tracking"] = {
            "carrier": carrier,
            "tracking_number": tracking_number,
            "added_at": datetime.now()
        }
        
        return {"success": True}
    
    def calculate_refund_amount(self, order_id: str) -> Dict:
        """
        Calculate refund amount for order
        
        BUGS TO FIND:
        - Order existence not checked
        - Partial refunds not supported
        - Shipping cost refund policy not clear
        - Time-based refund rules not implemented
        """
        order = self.orders[order_id]
        
        # BUG: Always refunds full amount regardless of order age or status
        refund_amount = order["total_amount"]
        
        return {
            "order_id": order_id,
            "refund_amount": refund_amount,
            "original_amount": order["total_amount"]
        }
    
    def process_return(
        self,
        order_id: str,
        items_to_return: List[str],
        reason: str
    ) -> Dict:
        """
        Process order return
        
        BUGS TO FIND:
        - Order existence not checked
        - Return window not validated (can return after 1 year)
        - Items existence in order not validated
        - Partial returns not properly handled
        - Refund not processed
        """
        order = self.orders[order_id]
        
        return_id = f"RET-{order_id}"
        
        return_record = {
            "return_id": return_id,
            "order_id": order_id,
            "items": items_to_return,
            "reason": reason,
            "status": "pending",
            "created_at": datetime.now()
        }
        
        # BUG: Refund not processed!
        # BUG: Inventory not updated!
        
        return {"success": True, "return_id": return_id}
    
    def get_orders_by_status(self, status: str) -> List[Dict]:
        """
        Get all orders with specific status
        
        BUGS TO FIND:
        - Status value not validated
        - No pagination
        - Case sensitivity issues
        """
        filtered_orders = [
            order for order in self.orders.values()
            if order["status"] == status
        ]
        
        return filtered_orders
    
    def update_shipping_address(
        self,
        order_id: str,
        new_address: Dict
    ) -> Dict:
        """
        Update shipping address for order
        
        BUGS TO FIND:
        - Can update address after order is shipped
        - Order existence not checked
        - Address validation missing
        - No notification sent
        """
        self.orders[order_id]["shipping_address"] = new_address
        self.orders[order_id]["updated_at"] = datetime.now()
        
        return {"success": True}
