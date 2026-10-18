from abc import ABC, abstractmethod
from typing import Optional, Mapping, Self, Any

import httpx
from httpx import Response


class BaseHttpClient(ABC):
    """Абстрактная обёртка над httpx для e2e против поднятого сервиса. Подклассы задают base_url."""
    __client_token_data = None
    def __init__(
        self,
        *,
        timeout: float = 30.0,
        default_headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        self._client = httpx.Client(
            base_url=self._httpx_base_url(),
            timeout=timeout,
            headers=dict(default_headers or {}),
        )

    @property
    @abstractmethod
    def base_url(self) -> str:
        """Корень API без завершающего слэша, например http://127.0.0.1:8000."""

    def _httpx_base_url(self) -> str:
        return self.base_url.rstrip("/") + "/"

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()

    def get(self, path: str, *, headers: Optional[Mapping[str, str]] = None, **kwargs: Any) -> Response:
        return self._client.get(path, headers=self._merge_headers(headers), **kwargs)

    def post(self, path: str, *, headers: Optional[Mapping[str, str]] = None, **kwargs: Any) -> Response:
        return self._client.post(path, headers=self._merge_headers(headers), **kwargs)

    def put(self, path: str, *, headers: Optional[Mapping[str, str]] = None, **kwargs: Any) -> Response:
        return self._client.put(path, headers=self._merge_headers(headers), **kwargs)

    def patch(self, path: str, *, headers: Optional[Mapping[str, str]] = None, **kwargs: Any) -> Response:
        return self._client.patch(path, headers=self._merge_headers(headers), **kwargs)

    def delete(self, path: str, *, headers: Optional[Mapping[str, str]] = None, **kwargs: Any) -> Response:
        return self._client.delete(path, headers=self._merge_headers(headers), **kwargs)

    def _merge_headers(self, extra: Optional[Mapping[str, str]]) -> Optional[dict[str, str]]:
        if not extra:
            return None
        merged = dict(self._client.headers)
        merged.update(extra)
        return merged

    def get_token(self):
        data = {
            "grant_type": "password",
            "username": "user@example.com",
            "password": "string",
        }
        res =self._client.post(url="/auth/token", data=data)
        self.__client_token_data = res.json()
        self._client.headers.update(
            httpx.Headers(
                {
                    "Authorization": f"Bearer {self.__client_token_data['access_token']}",
                    "accept": "application/json"
                },
            ),
        )