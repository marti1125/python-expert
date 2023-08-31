import asyncio
from typing import AsyncGenerator
from random import randint
from req_http import http_get

# the highest pokemon id
MAX_POKEMON = 898


async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])


async def next_pokemon(total: int) -> AsyncGenerator[str, None]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name


async def main() -> None:
    
    async for name in next_pokemon(10):
        print(name)
    
    names = [name async for name in next_pokemon(10)]
    print(names)


if __name__ == "__main__":
    asyncio.run(main())