from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Lead(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    phone: str = Field(..., description="Phone number")
    city: Optional[str] = Field(None, description="City in Pakistan")
    message: Optional[str] = Field(None, description="Optional message from user")

# Collection name will be "lead" (lowercase of class name)
