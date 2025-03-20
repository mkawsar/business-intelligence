from datetime import datetime, timezone
from beanie import Document
from pydantic import Field, BaseModel
from typing import List

class User(Document):
    name: str
    email: str
    username: str
    password: str
    roles: List[str] = []
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    