"""
Payment processing system with Stripe integration
"""

from typing import Dict, Optional
from datetime import datetime

class PaymentProcessor:
    def __init__(self, merchant_id: str, api_key: str):
        self.merchant_id = merchant_id
        self.api_key = api_key
        self.transaction_fee_percent = 2.9
        self.fixed_fee = 0.30
        self.transactions = {}
    
    def process_payment(
        self, 
        amount: float, 
        currency: str = "USD",
        customer_id: Optional[str] = None,
        payment_method: str = "card"
    ) -> Dict:
        """
        Process a payment transaction
        
        BUGS TO FIND:
        - No validation for negative amounts
        - No validation for zero amount
        - Currency not validated against supported currencies
        - Customer ID not validated
        - Payment method not validated
        - No fraud detection
        """
        # Calculate fees
        fee = (amount * self.transaction_fee_percent / 100) + self.fixed_fee
        net_amount = amount - fee
        
        transaction_id = f"TXN-{len(self.transactions) + 1}"
        
        transaction = {
            "id": transaction_id,
            "amount": amount,
            "currency": currency,
            "fee": fee,
            "net_amount": net_amount,
            "customer_id": customer_id,
            "payment_method": payment_method,
            "status": "completed",
            "created_at": datetime.now()
        }
        
        self.transactions[transaction_id] = transaction
        
        return {
            "success": True,
            "transaction_id": transaction_id,
            "amount": amount,
            "fee": fee,
            "net_amount": net_amount
        }
    
    def refund_payment(self, transaction_id: str, amount: Optional[float] = None) -> Dict:
        """
        Refund a payment (full or partial)
        
        BUGS TO FIND:
        - Transaction ID not validated
        - Refund amount can exceed original payment
        - Can refund already refunded transaction
        - Negative refund amount not checked
        - Refund fee calculation incorrect
        """
        if transaction_id not in self.transactions:
            return {"success": False, "error": "Transaction not found"}
        
        transaction = self.transactions[transaction_id]
        
        # BUG: Can refund multiple times!
        if transaction["status"] == "refunded":
            return {"success": False, "error": "Already refunded"}
        
        # Determine refund amount
        refund_amount = amount if amount is not None else transaction["amount"]
        
        # BUG: Not checking if refund_amount > original amount!
        
        # Calculate refund fee (1%)
        refund_fee = refund_amount * 0.01
        final_refund = refund_amount - refund_fee
        
        transaction["status"] = "refunded"
        transaction["refund_amount"] = refund_amount
        transaction["refund_fee"] = refund_fee
        transaction["refunded_at"] = datetime.now()
        
        return {
            "success": True,
            "transaction_id": transaction_id,
            "refund_amount": final_refund,
            "refund_fee": refund_fee
        }
    
    def apply_discount(self, amount: float, discount_percent: float) -> float:
        """
        Apply discount to amount
        
        BUGS TO FIND:
        - Discount percent can be > 100
        - Discount percent can be negative
        - Result can be negative
        """
        discount = amount * (discount_percent / 100)
        final_amount = amount - discount
        
        return final_amount
    
    def calculate_installments(
        self, 
        total_amount: float, 
        num_installments: int,
        interest_rate: float = 0.0
    ) -> Dict:
        """
        Calculate installment payment plan
        
        BUGS TO FIND:
        - Division by zero if num_installments = 0
        - Negative installments not handled
        - Rounding errors not handled
        - Interest rate can be negative
        """
        # BUG: No validation!
        installment_amount = total_amount / num_installments
        
        # Apply interest
        if interest_rate > 0:
            total_with_interest = total_amount * (1 + interest_rate / 100)
            installment_amount = total_with_interest / num_installments
        
        return {
            "total_amount": total_amount,
            "num_installments": num_installments,
            "installment_amount": installment_amount,
            "interest_rate": interest_rate
        }
    
    def process_recurring_payment(
        self,
        customer_id: str,
        amount: float,
        frequency: str = "monthly"
    ) -> Dict:
        """
        Setup recurring payment
        
        BUGS TO FIND:
        - Frequency not validated
        - Amount not validated
        - Customer ID not validated
        - No end date option
        """
        subscription_id = f"SUB-{len(self.transactions) + 1}"
        
        subscription = {
            "id": subscription_id,
            "customer_id": customer_id,
            "amount": amount,
            "frequency": frequency,
            "status": "active",
            "created_at": datetime.now(),
            "next_billing_date": datetime.now()
        }
        
        return {
            "success": True,
            "subscription_id": subscription_id,
            "amount": amount,
            "frequency": frequency
        }
    
    def verify_payment_method(self, payment_method_id: str) -> Dict:
        """
        Verify payment method is valid
        
        BUGS TO FIND:
        - Always returns success (no actual verification)
        - Payment method ID format not validated
        """
        # BUG: No actual verification!
        return {"valid": True, "payment_method_id": payment_method_id}
    
    def calculate_tax(self, amount: float, tax_rate: float, country: str = "US") -> Dict:
        """
        Calculate tax for transaction
        
        BUGS TO FIND:
        - Tax rate not validated (can be negative or > 100)
        - Country-specific rules not implemented
        - Amount not validated
        """
        tax_amount = amount * (tax_rate / 100)
        total_with_tax = amount + tax_amount
        
        return {
            "subtotal": amount,
            "tax_rate": tax_rate,
            "tax_amount": tax_amount,
            "total": total_with_tax,
            "country": country
        }
