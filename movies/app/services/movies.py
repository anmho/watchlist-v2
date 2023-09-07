import httpx
from fastapi import HTTPException, status
from app.config import Config
from app.utils.logger import LoggerFactory
import logging
import backoff


class MovieService:
    TMDB_API_KEY = Config.TMDB_API_KEY
    client = httpx.AsyncClient(
        base_url="https://api.themoviedb.org/3/",
        params={
            "api_key": TMDB_API_KEY
        }
    )

    # logger = LoggerFactory.create("MovieService")
    logger = logging.getLogger("MovieService")
    httpx_logger = logging.getLogger("httpx")
    httpx_logger.setLevel(logging.DEBUG)


    @classmethod
    @backoff.on_exception(backoff.expo, HTTPException, max_tries=3)
    async def get_movie_by_id(cls, movie_id: str):
        cls.logger.debug("✅✅✅" + cls.TMDB_API_KEY)

        try:
            r = await cls.client.get(f"/movie/{movie_id}")
            
            if 500 <= r.status_code <= 600:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            r.raise_for_status()
            return r.json()

        except httpx.HTTPError as e:
            cls.logger.error(e)
            raise
    
    @classmethod
    async def search_movies(cls, query: str):
        r = await cls.client.get("/search/movie", params={
            "query": query
        })
        return r.json()



        






    

