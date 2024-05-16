# models/base_model.py

# Import the variable 'storage' from file_storage.py
# from models.engine.file_storage import FileStorage
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        If kwargs is not emptym, recreate the instance from a
        dictionary representation.
        otherwise, create a new instance."""

        if kwargs: # If kwargs is not empty
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    # Convert created_at and updated_at to datetime objects
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    # Set each attribute according to the key-value pairs
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # Add a call  to new() method on storage for new instances
            self._import_storage().new(self) 
    
    def __str__(self):
        """
        Return a string represantation of the BaseModel instance

        Returns:
            str: String representation of the BaseModel instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        # print(string_rep)
        # return string_rep

    def save(self):
        """
        Update the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        self._import_storage().save()

    def to_dict(self):
        """
        Return a dictionary containing all key/value pairs of
        __dict__ of the instance

        Returns:
            dict: Dictionary representation ot the instance.
        """
        dict_object = self.__dict__.copy()
        dict_object["__class__"] = self.__class__.__name__
        dict_object["created_at"] = self.created_at.isoformat()
        dict_object["updated_at"] = self.updated_at.isoformat()
        return dict_object


    def _import_storage(self):
        " Imports storage when required "
        from models import storage
        return storage
