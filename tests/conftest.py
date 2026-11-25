import warnings
import pytest

# Suppress the Starlette deprecation warning about httpx
warnings.filterwarnings(
    "ignore",
    message="Using `httpx` with `starlette.testclient` is deprecated",
    category=DeprecationWarning
)
