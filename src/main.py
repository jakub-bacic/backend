import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.app:create_app", factory=True, reload=True)
