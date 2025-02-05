import pytest
from app.books.service import BookService
from app.books.schemas import Book, BookCreate



@pytest.mark.asyncio
async def test_get_all_books(async_client, mocker):

    books = [
        Book(id=1, title="Mock Book 1", description="Description 1", owner_id=1),
        Book(id=2, title="Mock Book 2", description="Description 2", owner_id=2),
    ]

    mock = mocker.patch.object(
        BookService, "get_all_books", return_value=books
    )

    # Make the request to the mocked endpoint
    response = await async_client.get("/books/all")

    # Assertions
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "Mock Book 1", "description": "Description 1", "owner_id": 1},
        {"id": 2, "title": "Mock Book 2", "description": "Description 2", "owner_id": 2},
    ]
    mock.assert_called_once()
    
@pytest.mark.asyncio
async def test_create_book(async_client, mocker):

    book = Book(id=1, title="New Book", description="A great book", owner_id=1)

    mock = mocker.patch.object(
        BookService, "create_book", return_value=book
    )

    book_data = BookCreate(title="New Book", description="A great book")

    response = await async_client.post("/books/new", json=book_data.model_dump(), params={"user_id": 1})

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "New Book",
        "description": "A great book",
        "owner_id": 1,
    }

    mock.assert_called_once()
    
@pytest.mark.asyncio
async def test_delete_book(async_client, mocker):
    
    mock = mocker.patch.object(
        BookService, "delete_book", return_value={}
    )

    response = await async_client.delete("/books/delete/1")

    assert response.status_code == 200
    assert response.json() == {}

    mock.assert_called_once_with(1, mocker.ANY)