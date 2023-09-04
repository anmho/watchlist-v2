import httpx
import asyncio


from app.app import create_app


app = create_app()



# async def get_movie(url):
#     async with httpx.AsyncClient() as client:
#         r = await client.get(url)
#         return r.json()
    

# async  def main():
#     TMDB_API_KEY = "8784d04e148ccc0bdc003b1dc79e5483"

#     url = f"https://api.themoviedb.org/3/movie/157336?api_key={TMDB_API_KEY}"

#     # Synchronous
#     r = httpx.get(url)
#     print(r.json())

#     # Asynchronous
#     movie = await get_movie(url)
#     print(movie)
    

# if __name__ == "__main__":
#     asyncio.run(main())


# import requests

# url = "https://api.themoviedb.org/3/search/movie?query=furious&include_adult=false&language=en-US&page=1&api_key=8784d04e148ccc0bdc003b1dc79e5483"

# headers = {
#     "accept": "application/json",
# }

# response = requests.get(url, headers=headers)

# print(response.text)