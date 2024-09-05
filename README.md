# Movie API Documentation

This is the API documentation for the Movie application.

## Features

- List all movies with pagination
- Search movies by name and genre
- Sort movies by rating and creation date
- Add, update, and delete movies (admin only)

## Authentication

The API uses JWT (JSON Web Token) for authentication. You need to include a valid token in the `Authorization` header of your requests.

### Example

```http
Authorization: Bearer <your_token>
```

## User Registration

URL: `user/register/`

Method: POST

Description: Register a new user.

Request Body:

```json
{
  "username": "test",
  "email": "test@gmail.com",
  "password": "test@123",
  "is_admin": true
}
```

Example Response:

```json
{
  "message": "User registered successfully"
}
```

## User Login

URL: `user/login/`

Method: POST

Description: Log in an existing user, USE FOLLOWING CREDENTIALS TO LOGIN.

Request Body:

```json
{
  "username": "avi@gmail.com",
  "password": "avi@123"
}
```

Example Response:

````json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTY0MDM4MywiaWF0IjoxNzI1NTUzOTgzLCJqdGkiOiJmODIxMDdhMmQwMzE0YmI4ODBkYmE3MjA5NDFlNTU2NiIsInVzZXJfaWQiOjN9.Yn9JtT-2LVUh-Z3BthH157pQYRp4UrDwAm_oQAq9L-k",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NTU0MjgzLCJpYXQiOjE3MjU1NTM5ODMsImp0aSI6ImMzNjVhN2M0YzBhMzRiNGFiZGI2NTljODBmYmUzYTNkIiwidXNlcl9pZCI6M30.ViFZasi8B6UG13syvKYxT0yhO1N2wL15Upudb5o8xgc"
}
```


NOTE : use access token for authorization as a bearer token


1. List Movies

URL: `/movies/`

Method: GET

Description: Retrieve a list of movies with optional search and genre filters.

Query Parameters:

- `search` (optional): Search term to filter movies by name.
- `genre` (optional): Genre to filter movies by genre name.
- `page` (optional): Page number for pagination.
- `sort` (optional): Sort page based on rating or score
- `page_size` (optional): Number of movies per page.

Example Request for search movies:

````

GET /movies/?search=Psycho

````

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
````

Example Request for sorting movies based on rating :

```
GET /movies/?sort_by=imdb_score&order=asc
```

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "Inception",
      "director": "Christopher Nolan",
      "imdb_score": 8.8,
      "imdb_popularity": 90.0,
      "genres": [
        {
          "id": 1,
          "name": "Action"
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
