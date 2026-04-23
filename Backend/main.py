from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
from extractor import extract_topics
from hierarchy import build_hierarchy
from utils import read_file
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API working"}

@app.post("/process")
async def process(file: UploadFile = File(...)):
    content = await file.read()

    # convert bytes → text
    text = content.decode("utf-8")

    topics = extract_topics(text)
    hierarchy = build_hierarchy(topics)

    return {"gis": hierarchy}