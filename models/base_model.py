#!/usr/bin/python3                                          """defines all common attributes/methods for other classes"""
from uuid import uuid4
import datetime
                                                            
class BaseModel:
    """a class that defines all common attributes/methods for other classes"""
    def __init__(self, id, created_at, updated_at):                 """a constructor to initialize this class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """string representation of class"""                        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the updated_at with cirrent time"""
        self.updated_at = datetime.now()

    def __dict__(self):
        """creates a dictionary in json format"""
        return {
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
            }
