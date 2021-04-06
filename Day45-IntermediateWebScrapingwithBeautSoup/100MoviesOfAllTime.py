from bs4 import BeautifulSoup
import lxml
import requests
import json

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
data = json.loads(soup.select_one("#__NEXT_DATA__").contents[0])

# print(json.dumps(data,indent=4))

def find_titles(data):
    if isinstance(data,dict):
        for k,v in data.items():
            if k.startswith("ImageMeta:"):
                yield v["titleText"]
            else:
                yield from find_titles(v)
    elif isinstance(data,list):
        for i in data:
            yield from find_titles(i)


movie_titles = []
# appending the movie to movies variable
for a in find_titles(data):
    movie_titles.append(a)
    # print(a)

# quick ascending order
movies = movie_titles[::-1]

# for n in range(len(movies) - 1, -1,-1):
#     print(movies[n])

# now writing the movies list to a text file
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")