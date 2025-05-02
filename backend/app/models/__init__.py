# Explicitly export CryptoPrice for clarity and avoid circular import issues
from app.models.crypto_price import CryptoPrice

__all__ = ["CryptoPrice"]