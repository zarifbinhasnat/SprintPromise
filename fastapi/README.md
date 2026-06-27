# FastAPI Track

Mini-projects organized by concept. Each folder is a standalone runnable app.

## Structure

```
fastapi/
├── 01_hello_world/         Setup + GET routes
├── 02_path_query_params/   Path & query parameters
├── 03_request_body/        POST with Pydantic models
├── 04_put_delete/          Full CRUD
├── 05_response_models/     Output schemas
├── 06_error_handling/      HTTPException, custom errors
├── 07_middleware/          CORS, logging middleware
├── 08_dependencies/        Dependency injection
├── 09_auth_jwt/            JWT auth flow
├── 10_sqlalchemy/          SQLite + ORM
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
