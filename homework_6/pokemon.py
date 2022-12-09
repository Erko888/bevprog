import urllib.request
from urllib.request import Request, urlopen
import json

def main():

    name = input("Add meg a Pokemon nevét: ")
    response = Request(f"https://pokeapi.co/api/v2/pokemon/{name}/", headers={"User-Agent": "Mozilla/5.0"})
    raw = urlopen(response).read()
    txt = raw.decode('utf-8')
    data = json.loads(txt)

    name = data["name"]
    health = data["stats"][0]["base_stat"]
    attack = data["stats"][1]["base_stat"]
    defense = data["stats"][2]["base_stat"]
    height = data["height"]
    print(f"Name: {name}")
    print(f"attack: {attack}")
    print(f"defense: {defense}")
    print(f"height: {height}")
    print(f"Health: {health}")


if __name__ == "__main__":
    main()