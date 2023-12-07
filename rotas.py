from fastapi import APIRouter, status, Depends, Request
#from classes import Presidente, item, gabinete, User, salvar, consultar, ver, html
import classes


from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="templates")

rotas = APIRouter()


@rotas.get('/teste/{num}', response_class=HTMLResponse)
def testes(request : Request, num : int):
    if num == 0:
        return templates.TemplateResponse('main.html', {"request": request, "mensagem": 'funcionaaaa'})
