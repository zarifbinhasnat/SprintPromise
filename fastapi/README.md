# FastAPI Track

Mini-projects organized by concept. Each folder is a standalone runnable app.

## Structure

```
fastapi/
├── 01_hello_world/         Setup + GET routes
├── 02_path_query_params/   Path & query parameters
├── 03_request_body/        POST with Pydantic models
├── 04_put_delete/          Full CRUD
├── 05_status_codes/        Swagger UI deep-dive, response status codes
├── 06_error_handling/      HTTPException, custom errors
├── 07_response_models/     Output schemas
├── 08_middleware/          CORS, logging middleware
├── 09_dependencies/        Dependency injection
├── 10_week2_review/        CRUD + status codes + error handling + dependencies, reviewed
├── 11_custom_exception_handlers/  @app.exception_handler, consistent error envelopes
├── 12_lifespan_events/     @asynccontextmanager startup/shutdown hooks
├── 13_cors_middleware/     CORSMiddleware, allowed origins, preflight requests
├── 14_request_logging/     Middleware logging method, path, status, duration
├── 16_class_based_middleware/  BaseHTTPMiddleware subclass, add_middleware()
├── 17_middleware_ordering_gzip/  Stacking middleware, onion-model ordering, GZipMiddleware
├── 18_lifespan_resource_pool/   Lifespan-managed connection pool via Depends()
└── ...
```

## How to Run Any Project

```bash
cd fastapi/01_hello_world
pip install fastapi uvicorn
uvicorn main:app --reload
# Open http://localhost:8000/docs
```

## Docs

- FastAPI: https://fastapi.tiangolo.com
- Pydantic: https://docs.pydantic.dev
