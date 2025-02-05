from fastapi import APIRouter, Depends, status
from app.users.service import UserService
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import get_session
from app.users.schemas import UserCreate

users_router = APIRouter(prefix="/users", tags=["users"])

user_service = UserService()

@users_router.get("/all")
async def all_users(session: AsyncSession = Depends(get_session)):
    return await user_service.get_all_users(session)


@users_router.get("/{user_id}")
async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    return await user_service.get_user(user_id, session)


@users_router.post("/new", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate, session: AsyncSession = Depends(get_session)):
    return await user_service.create_user(user_data, session)

@users_router.delete("/delete/{user_id}")
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    return await user_service.delete_user(user_id, session)