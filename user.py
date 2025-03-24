
_id_count = 0

class User:


  def __init__(self, user_name: str, user_email: str):
    """
    Constructor for the User class.

    Args:
      user_id (int): The unique identifier of the user.
      user_name (str): The name of the user.
      user_email (str): The email address of the user.
    """
    global _id_count

    _id_count = _id_count + 1
    self._id = _id_count  # We use an underscore to indicate it's an internal variable
    self.name = user_name
    self.email = user_email

  @property
  def id(self) -> str:
    """
    Getter for the id property. It is read-only.
    """
    return self._id

  def to_json(self):
    """
    Returns a dictionary representation of the User object.
    """
    return {
      'id': self.id,
      'name': self.name,
      'email': self.email
    }

  @staticmethod
  def validate_user_data(data: dict) -> bool:
    """
    Validates if a dictionary contains only the 'email' and 'name' properties.

    Args:
      data (dict): The dictionary to validate.

    Returns:
      bool: True if the dictionary contains only 'email' and 'name', False otherwise.
    """
    if len(data) == 2 and 'email' in data and 'name' in data:
      return True
    else:
      return False
