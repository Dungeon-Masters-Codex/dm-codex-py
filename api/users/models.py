from pydantic import BaseModel, Field

class User(BaseModel):
    # TODO: when more relevant expand to using Field for email/password
    username: str # TODO: install python-email-validator to get the EmailStr type and later validation (will be presented as email to user in FE)
    display_name: str | None = Field(
        default=None, title="The display name chosen by the user", 
        max_length=50,
        examples=["Elrich of the Emerald Enclave"]
    )

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class UserInDB(User):
    hashed_password: str

# TODO: review fastapi docs that this is a sensible pattern when more time
class UserInput(User):
    """ Extends User with input specific schema. """
    password: str