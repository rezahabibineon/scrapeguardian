from fastapi import APIRouter, Query
from apps.controllers.NewsController import NewsController


router = APIRouter()

@router.get("/scrape_news")
async def scrape_news():
    total, data =  NewsController.scrape_news()
    return {
        "total": total,
        "data": data,
    }

@router.get("/get_news")
async def get_news():
    total, data =  NewsController.get_news()
    return {
        "total": total,
        "data": data,
    }

@router.get("/get_news_by_word")
async def get_news_by_word(qword: str = Query(..., example="Tackle Economic")):
    total, data =  NewsController.get_news_by_word(qword)
    return {
        "total": total,
        "data": data,
    }

@router.get("/get_news_by_title")
async def get_news_by_title(qtitle: str = Query(..., 
            example="Pressure Grows On Uk To Beef Up Measures To Tackle Economic")):
    
    data = NewsController.get_news_by_title(title=qtitle)
    return {
        "data": data,
    }

@router.get("/get_news_by_link")
async def get_news_by_link(qlink: str = Query(..., 
            example="https://www.theguardian.com/law/2022/jan/25/pressure-grows-on-uk-to-beef-up-measures-to-tackle-economic")):
    
    data, msg = NewsController.get_news_by_link(link=qlink)
    return {
        "msg": msg,
        "data": data,
    }  