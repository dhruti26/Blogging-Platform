from fastapi import FastAPI 
from routes.entry import entry_root
from routes.blog import node
app = FastAPI()

app.include_router(entry_root)
app.include_router(node)