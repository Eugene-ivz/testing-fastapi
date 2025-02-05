from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schemas import BookCreate
from app.db.models import Book


class BookService:
    async def get_all_books(self, session: AsyncSession):
        query = select(Book)

        result = await session.execute(query)

        return result.scalars().all()


    async def get_user_books(self, user_id: int, session: AsyncSession):
        query = (
            select(Book)
            .where(Book.owner_id == user_id))
        print(query)
        result = await session.execute(query)
        return result.scalars().all()


    async def get_book(self, book_id: int, session: AsyncSession):
        query = select(Book).where(Book.id == book_id)

        result = await session.execute(query)

        book = result.scalar_one_or_none()

        return book


    async def create_book(self, book_data: BookCreate, user_id: str, session: AsyncSession):
        book_data = book_data.model_dump()

        new_book = Book(**book_data)
        
        new_book.owner_id = user_id

        session.add(new_book)

        await session.commit()

        await session.refresh(new_book)

        return new_book



    async def delete_book(self, book_uid: str, session: AsyncSession):
        book = await self.get_book(book_uid, session)

        if book is not None:
            await session.delete(book)

            await session.commit()

            return {}

        else:
            return None
