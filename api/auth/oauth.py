from fastapi.security import OAuth2PasswordBearer

from constants.api import API_PREFIX, AUTH_PREFIX

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{API_PREFIX}{AUTH_PREFIX}/token")
