from fastapi import APIRouter, Depends, status
from app.books.service import BookService
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import get_session
from app.books.schemas import BookCreate

books_router = APIRouter(prefix="/books", tags=["books"])

book_service = BookService()

@books_router.get("/all")
async def all_books(session: AsyncSession = Depends(get_session)):
    return await book_service.get_all_books(session) 


@books_router.get("/{book_id}")
async def get_book(book_id: int, session: AsyncSession = Depends(get_session)):
    return await book_service.get_book(book_id, session)

@books_router.get("/by_user/{user_id}")
async def get_user_books(user_id: int, session: AsyncSession = Depends(get_session)):
    return await book_service.get_user_books(user_id, session)


@books_router.post("/new")
async def create_book(book_data: BookCreate, user_id: int, session: AsyncSession = Depends(get_session)):
    return await book_service.create_book(book_data, user_id, session)

@books_router.delete("/delete/{book_id}")
async def delete_book(book_id: int, session: AsyncSession = Depends(get_session)):
    return await book_service.delete_book(book_id, session)