import pytest
from sqlalchemy import select
from app.users.schemas import UserCreate
from app.db.models import User



@pytest.mark.asyncio
async def test_create_user(async_client, db_session):
    user_data = UserCreate(name="John Doe", email="johndoe@example.com")
    
    response = await async_client.post("/users/new", json=user_data.model_dump())
    assert response.status_code == 201
    
    user_id = response.json()["id"]
    result = await db_session.execute(select(User).where(User.id == user_id))
    user = result.scalar()
    assert user.email == "johndoe@example.com"
    
@pytest.mark.asyncio
async def test_delete_user(async_client, db_session):
    
    user = User(name="Jane Doe", email="janedoe@example.com")
    db_session.add(user)
    await db_session.commit()
    
    response = await async_client.delete(f"/users/delete/{user.id}")
    assert response.status_code == 200
    
    result = await db_session.execute(select(User).where(User.id == user.id))
    assert result.scalar() is None
  