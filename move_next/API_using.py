import requests

def give_name(name):
    base_url = "https://pokeapi.co/api/v2/"

    url = f"{base_url}pokemon/{name}"
    get_data = requests.get(url)


    if get_data.status_code == 200 :
        return requests.get(url).json()

if __name__=="__main__":
    nme = give_name("pikachu")
    print(f"{nme["name"]}")