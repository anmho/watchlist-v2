from fastapi import APIRouter, Query, HTTPException, status
from app.services.movies import MovieService


movies = APIRouter(
    prefix="/movies", 
    tags=["movies"], 
    dependencies=[]
)


"""
Resources Managed: Movies, Movie Ratings


Goals: Pagination, Caching, Rate Limiting, Authorization
GraphQL
"""


@movies.get("/{movie_id}")
async def get_movie(movie_id: str):
    movies = await MovieService.get_movie_by_id(movie_id)
    return movies

@movies.get("")
async def search_movies(query: str):
    return await MovieService.search_movies(query)
