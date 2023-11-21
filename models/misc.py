from os import getenv

from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


classes = {
    'User': User,
    'City': City,
    'Place': Place,
    'Review': Review,
    'State': State,
    'Amenity': Amenity
}

db = getenv("HBNB_MYSQL_DB")
host = getenv("HBNB_MYSQL_HOST")
user = getenv("HBNB_MYSQL_USER")
pwd = getenv("HBNB_MYSQL_PWD")
ENV = getenv("HBNB_ENV")