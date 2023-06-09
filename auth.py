from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import JWTError, jwe
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from config import settings
import json

SECRET_KEY: str = settings.jwt_secret

key_scheme = HTTPBearer(description="Json Web Token with Encrypted", scheme_name="Token")


def hkdf_key(key_material: str) -> bytes:
    salt = b""
    info = b"NextAuth.js Generated Encryption Key"

    hkdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=salt, info=info)
    derived_key = hkdf.derive(key_material.encode("utf-8"))
    return derived_key


# JWEをデコードする関数
def decode_jwe(token: str) -> str:
    secret = hkdf_key(key_material=SECRET_KEY)
    payload = jwe.decrypt(jwe_str=token.encode(), key=secret)
    return payload.decode()


async def get_current_user(token: str = Depends(key_scheme)) -> dict:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = json.loads(decode_jwe(str(token.credentials)))
        email: str = payload.get("email")
        if (not "higashifukuoka.net" in email or email == "hfhs.digitalp@gmail.com"):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to access.",
                headers={"WWW-Authenticate": "Bearer"},
            )
        else:
            return payload
    except JWTError:
        raise credentials_exception