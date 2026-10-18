import os
from typing import Optional, Mapping

from tests.clients.base import BaseHttpClient


class ToDoListClient(BaseHttpClient):
    """Готовый клиент: base_url из аргумента или окружения (удобно для локального uvicorn/docker)."""

    def __init__(
        self,
        base_url: str | None = None,
        *,
        api_prefix: str = "",
        timeout: float = 30.0,
        default_headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        raw = (base_url or os.environ.get("E2E_BASE_URL", "http://127.0.0.1:8000")).rstrip("/")
        prefix = api_prefix.strip().strip("/")
        self._base_url = f"{raw}/{prefix}" if prefix else raw
        super().__init__(timeout=timeout, default_headers=default_headers)

    @property
    def base_url(self) -> str:
        return self._base_url