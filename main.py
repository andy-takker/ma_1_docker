from fastapi import FastAPI


def get_application() -> FastAPI:
    """App Factory"""
    application = FastAPI(
        title="Health Check",
        version="0.0.1",
    )

    @application.get("/health/")
    async def get_health():
        return {"status": "OK"}

    return application


app = get_application()
