# Movie API Documentation

# Movie API Documentation

This is the API documentation for the Movie application. The API allows users to retrieve, create, update, and delete movie information.

## Authentication

The API uses JWT (JSON Web Token) for authentication. You need to include a valid token in the `Authorization` header of your requests.

### Example

```http
Authorization: Bearer <your_token>
```

1. List Movies

URL: `/movies/`

Method: GET

Description: Retrieve a list of movies with optional search and genre filters.

Query Parameters:

- `search` (optional): Search term to filter movies by name.
- `genre` (optional): Genre to filter movies by genre name.
- `page` (optional): Page number for pagination.
- `page_size` (optional): Number of movies per page.

Example Request:

```
GET /movies/?search=Inception&genre=Action&page=1&page_size=10
```

Example Response:

```json
{
  "count": 100,
  "next": "http://example.com/movies/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Inception",
      "genres": ["Action", "Sci-Fi"],
      "release_date": "2010-07-16"
    },
    {
      "id": 2,
      "name": "The Dark Knight",
      "genres": ["Action", "Crime"],
      "release_date": "2008-07-18"
    }
    // More movie objects...
  ]
}
```

2. Retrieve a Movie

URL: `/movies/<pk>/`

Method: GET

Description: Retrieve detailed information about a specific movie.

Example Request:

```
GET /movies/1/
```

Example Response:

```json
{
  "id": 1,
  "name": "Inception",
  "genres": ["Action", "Sci-Fi"],
  "release_date": "2010-07-16"
}
```

3. Create a Movie

URL: `/movies/`

Method: POST

Description: Create a new movie. Requires admin privileges.

Request Body:

```json
{
  "name": "Inception",
  "genres": ["Action", "Sci-Fi"],
  "release_date": "2010-07-16"
}
```

Example Response:

```json
{
  "message": "Movie added successfully",
  "movie_id": 1
}
```

4. Update a Movie

URL: `/movies/<pk>/`

Method: PUT

Description: Update an existing movie. Requires admin privileges.

Request Body:

```json
{
  "name": "Inception",
  "genres": ["Action", "Sci-Fi"],
  "release_date": "2010-07-16"
}
```

Example Response:

```json
{
  "message": "Movie updated successfully"
}
```

5. Delete a Movie

URL: `/movies/<pk>/`

Method: DELETE

Description: Delete an existing movie. Requires admin privileges.

Example Response:

```json
{
  "message": "Movie deleted successfully"
}
```

Example Error Response:

```json
{
  "detail": "Authentication credentials were not provided."
}
```
