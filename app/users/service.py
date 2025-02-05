from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schemas import UserCreate
from app.db.models import User

class UserService:
    
    async def get_all_users(self, session: AsyncSession):
        query = select(User)

        result = await session.execute(query)    

        return result.scalars().all()

    async def get_user(self,user_id: str, session: AsyncSession):
        query = select(User).where(User.id == user_id)

        result = await session.execute(query)

        return result.scalar()
    

    async def create_user(self, user_data: UserCreate, session: AsyncSession):
        user_data = user_data.model_dump()

        new_user = User(**user_data)
        
        session.add(new_user)

        await session.commit()

        await session.refresh(new_user)

        return new_user
    

    async def delete_user(self, user_id: str, session: AsyncSession):
        user = await self.get_user(user_id, session)

        if user is not None:
            await session.delete(user)

            await session.commit()

            return {}

        else:
            return None
        
    