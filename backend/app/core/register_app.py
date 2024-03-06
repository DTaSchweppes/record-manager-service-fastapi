from fastapi import FastAPI
from backend.app.api.routers import v1
from backend.app.core.conf import settings


def register_app():
    # FastAPI
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOCS_URL,
        openapi_url=settings.OPENAPI_URL
    )

    register_router(app)
    return app


def register_router(app: FastAPI):
    """
    :param app: FastAPI
    :return:
    """
    app.include_router(v1)