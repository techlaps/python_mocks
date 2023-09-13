import requests


def len_joke():
    joke = get_joke()

    print()
    print("The joke from get_joke(): ", joke)
    print()

    return len(joke)


def get_joke():
    url = "https://api.chucknorris.io/jokes/random"

    print()
    print(type(requests.exceptions.Timeout))
    print()

    try:
        response = requests.get(url, timeout=30)
    except requests.exceptions.Timeout:
        return "No jokes"

    except requests.exceptions.ConnectionError:
        pass

    else:
        if response.status_code == 200:
            joke = response.json()['value']
        else:
            joke = "No jokes"

    return joke


if __name__ == "__main__":
    print(get_joke())
