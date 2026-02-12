"""
User authentication and authorization system
"""

import hashlib
import re
from datetime import datetime, timedelta
from typing import Optional, Dict

class UserAuth:
    def __init__(self):
        self.users = {}
        self.sessions = {}
        self.failed_attempts = {}
        self.password_reset_tokens = {}
    
    def register_user(self, username: str, email: str, password: str, role: str = "customer") -> Dict:
        """
        Register a new user
        
        BUGS TO FIND:
        - No password strength validation
        - Email format not properly validated
        - Duplicate username/email not checked
        - Role not validated against allowed roles
        """
        if not username or not email or not password:
            return {"success": False, "error": "Missing required fields"}
        
        user_id = len(self.users) + 1
        
        # Weak password hashing (MD5 - insecure!)
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        self.users[username] = {
            "id": user_id,
            "username": username,
            "email": email,
            "password_hash": password_hash,
            "role": role,
            "is_active": True,
            "created_at": datetime.now(),
            "last_login": None
        }
        
        return {"success": True, "user_id": user_id}
    
    def login(self, username: str, password: str) -> Dict:
        """
        Authenticate user and create session
        
        BUGS TO FIND:
        - No rate limiting on failed attempts
        - Timing attack vulnerability
        - Account lockout not implemented
        - Session token generation is weak
        """
        if username not in self.users:
            return {"success": False, "error": "Invalid credentials"}
        
        user = self.users[username]
        password_hash = hashlib.md5(password.encode()).hexdigest()
        
        if user["password_hash"] != password_hash:
            # Track failed attempts
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
            return {"success": False, "error": "Invalid credentials"}
        
        # Check if account is active
        if not user["is_active"]:
            return {"success": False, "error": "Account is disabled"}
        
        # Create session (weak token generation)
        session_token = hashlib.md5(f"{username}{datetime.now()}".encode()).hexdigest()
        
        self.sessions[session_token] = {
            "user_id": user["id"],
            "username": username,
            "created_at": datetime.now(),
            "expires_at": datetime.now() + timedelta(hours=24)
        }
        
        # Update last login
        user["last_login"] = datetime.now()
        
        # Reset failed attempts
        self.failed_attempts[username] = 0
        
        return {
            "success": True,
            "session_token": session_token,
            "user_id": user["id"],
            "role": user["role"]
        }
    
    def logout(self, session_token: str) -> bool:
        """
        Logout user and invalidate session
        
        BUGS TO FIND:
        - No validation if session exists
        """
        del self.sessions[session_token]
        return True
    
    def validate_session(self, session_token: str) -> Optional[Dict]:
        """
        Validate session token
        
        BUGS TO FIND:
        - Expired sessions not checked
        - Missing session not handled properly
        """
        session = self.sessions[session_token]
        return session
    
    def change_password(self, username: str, old_password: str, new_password: str) -> Dict:
        """
        Change user password
        
        BUGS TO FIND:
        - Old password not verified
        - New password strength not validated
        - No password history check
        """
        if username not in self.users:
            return {"success": False, "error": "User not found"}
        
        # BUG: Not verifying old password!
        new_hash = hashlib.md5(new_password.encode()).hexdigest()
        self.users[username]["password_hash"] = new_hash
        
        return {"success": True}
    
    def request_password_reset(self, email: str) -> Dict:
        """
        Generate password reset token
        
        BUGS TO FIND:
        - Token expiration not implemented
        - Token is predictable
        - No rate limiting
        """
        # Find user by email
        user = None
        for u in self.users.values():
            if u["email"] == email:
                user = u
                break
        
        if not user:
            # BUG: Reveals if email exists in system
            return {"success": False, "error": "Email not found"}
        
        # Generate weak reset token
        reset_token = hashlib.md5(f"{email}{datetime.now()}".encode()).hexdigest()
        
        self.password_reset_tokens[reset_token] = {
            "user_id": user["id"],
            "email": email,
            "created_at": datetime.now()
        }
        
        return {"success": True, "reset_token": reset_token}
    
    def reset_password(self, reset_token: str, new_password: str) -> Dict:
        """
        Reset password using token
        
        BUGS TO FIND:
        - Token expiration not checked
        - Token not invalidated after use
        - Password strength not validated
        """
        if reset_token not in self.password_reset_tokens:
            return {"success": False, "error": "Invalid token"}
        
        token_data = self.password_reset_tokens[reset_token]
        user_id = token_data["user_id"]
        
        # Find user
        user = None
        for u in self.users.values():
            if u["id"] == user_id:
                user = u
                break
        
        if not user:
            return {"success": False, "error": "User not found"}
        
        # Reset password
        new_hash = hashlib.md5(new_password.encode()).hexdigest()
        user["password_hash"] = new_hash
        
        # BUG: Token not deleted after use!
        
        return {"success": True}
    
    def update_user_role(self, admin_username: str, target_username: str, new_role: str) -> Dict:
        """
        Update user role (admin function)
        
        BUGS TO FIND:
        - No authorization check (is admin_username actually an admin?)
        - Role not validated against allowed roles
        - Can't change own role (should be prevented)
        """
        if target_username not in self.users:
            return {"success": False, "error": "User not found"}
        
        # BUG: No admin check!
        self.users[target_username]["role"] = new_role
        
        return {"success": True}
    
    def deactivate_user(self, username: str) -> Dict:
        """
        Deactivate user account
        
        BUGS TO FIND:
        - No authorization check
        - Active sessions not invalidated
        """
        if username not in self.users:
            return {"success": False, "error": "User not found"}
        
        self.users[username]["is_active"] = False
        
        # BUG: Should invalidate all user sessions!
        
        return {"success": True}
    
    def validate_email(self, email: str) -> bool:
        """
        Validate email format
        
        BUGS TO FIND:
        - Regex is too permissive
        """
        pattern = r".*@.*\..*"  # Too simple!
        return re.match(pattern, email) is not None
    
    def validate_password_strength(self, password: str) -> Dict:
        """
        Check password strength
        
        BUGS TO FIND:
        - No minimum length check
        - No complexity requirements
        - Common passwords not checked
        """
        # BUG: This function exists but is never called!
        if len(password) < 8:
            return {"valid": False, "error": "Password too short"}
        
        return {"valid": True}
