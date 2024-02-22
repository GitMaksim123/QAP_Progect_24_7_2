import os
from dotenv import load_dotenv


load_dotenv()


valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

invalid_email = os.getenv('invalid_email')
invalid_password = os.getenv('invalid_password')

name_set = os.getenv('name_set')
animal_type_set = os.getenv('animal_type_set')
age_set = os.getenv('age_set')