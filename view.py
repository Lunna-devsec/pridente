from fastapi import APIRouter, status, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


from caminhos import caminhos, mercado


templates = Jinja2Templates(directory="templates")
html = APIRouter()


@html.get('/teste/{num}', response_class=HTMLResponse)
def testes(request : Request, num : int):
    if num == 0:
        return templates.TemplateResponse('main.html', {"request": request, "mensagem": 'funcionaaaa'})

@html.get('/', response_class=HTMLResponse)
async def home(request : Request):

        # Exemplo de dados em Python
    cards_data = [
        {"img_src": "imagem1.jpg", "texto1": "Texto do Card 1", "texto2": "Outro texto 1", "texto3": "Mais texto 1"},
        {"img_src": "imagem2.jpg", "texto1": "Texto do Card 2", "texto2": "Outro texto 2", "texto3": "Mais texto 2"},
        {"img_src": "imagem1.jpg", "texto1": "Texto do Card 1", "texto2": "Outro texto 1", "texto3": "Mais texto 1"}
        
        # ... mais dados
    ]
    return templates.TemplateResponse('home.html', {"request": request, "cards_data": cards_data, 'rendimento': 2000, "mercado": caminhos["mercado"]})

@html.get('/mercado', response_class=HTMLResponse)
async def mercado(request):
    return templates.TemplateResponse('mercado.html', {"request": request})