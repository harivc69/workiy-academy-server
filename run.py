import uvicorn

if __name__ == "__main__":
    import os
    env = os.getenv("APP_ENV", "dev")
    app_path = "app.main:app"

    uvicorn.run(app_path, host="127.0.0.1", port=8000, reload=True)
