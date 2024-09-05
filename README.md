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
GET /movies/?search=Psycho
```

Example Response:

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 500,
      "name": "Psycho",
      "director": "Alfred Hitchcock",
      "imdb_score": 8.7,
      "imdb_popularity": 87.0,
      "genres": [
        {
          "id": 10,
          "name": "Horror"
        },
        {
          "id": 11,
          "name": " Mystery"
        },
        {
          "id": 12,
          "name": " Thriller"
        }
      ]
    }
  ]
}
```

2. Retrieve a Movie

URL: `/movies/<pk>/`

Method: GET

Description: Retrieve detailed information about a specific movie.

Example Request:

```
GET /movies/500/
```

Example Response:

```json
{
  "id": 500,
  "name": "Psycho",
  "director": "Alfred Hitchcock",
  "imdb_score": 8.7,
  "imdb_popularity": 87.0,
  "genres": [
    {
      "id": 10,
      "name": "Horror"
    },
    {
      "id": 11,
      "name": " Mystery"
    },
    {
      "id": 12,
      "name": " Thriller"
    }
  ]
}
```

3. Create a Movie

URL: `/movies/`

Method: POST

Description: Create a new movie. Requires admin privileges.

Request Body:

```json
{
  "name": "Psycho-2",
  "director": "Alfred Hitchcock",
  "imdb_score": 8.7,
  "imdb_popularity": 87.0,
  "genre_ids": [10, 11]
}
```

Example Response:

```json
{
  "message": "Movie added successfully",
  "movie_id": "12"
}
```

4. Update a Movie

URL: `/movies/<pk>/`

Method: PUT

Description: Update an existing movie. Requires admin privileges.

Request Body:

```json
{
  "name": "Psycho-2s",
  "director": "Alfred Hitchcock",
  "imdb_score": 8.7,
  "imdb_popularity": 87.0,
  "genre_ids": [10, 11]
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

```json
{
  "detail": "Given token not valid for any token type",
  "code": "token_not_valid",
  "messages": [
    {
      "token_class": "AccessToken",
      "token_type": "access",
      "message": "Token is invalid or expired"
    }
  ]
}
```

```json
{
  "name": ["movie with this name already exists."]
}
```
