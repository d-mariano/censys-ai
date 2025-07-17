import json
import os

from fastapi.openapi.utils import get_openapi
from censys_ai.api.app import app

destination = os.path.join(
    os.path.dirname(__file__),
    '../src/censys_ai/api/censys-ai-openapi.json'
)

with open(destination, 'w') as f:
    json.dump(get_openapi(
        title=app.title,
        version=app.version,
        openapi_version="3.1.0",
        description=app.description,
        routes=app.routes,
    ), f)
