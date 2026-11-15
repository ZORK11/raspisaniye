from fastapi import FastAPI, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from utils import *

app = FastAPI()
templates = Jinja2Templates('templates')
app.mount('/static', StaticFiles(directory="static"), name="static")

UPLOAD_DIR = 'uploads'

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse(name = 'index.html', request=request)

@app.post('/check')
async def check(file: UploadFile,request: Request):
    content = await file.read()

    destination = f'{UPLOAD_DIR}/{file.filename}'

    with open(destination, "wb") as dest_file:
        dest_file.write(content)

    parsed_file = parse_room_csv(destination)
    conflicts = find_room_conflict(parsed_file)
    return templates.TemplateResponse(request=request, name='result.html', context={'conflicts': conflicts})

@app.get('/sample.csv')
def sample():
    file_path = 'lessons.csv'
    return FileResponse(
        path=file_path,
        filename="sample.csv",  # Имя файла при скачивании
        media_type="multipart/form-data"  # MIME-тип
    )
