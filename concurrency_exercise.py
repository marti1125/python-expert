import asyncio
import requests


async def fetch_data(url: str) -> str:
    await asyncio.sleep(2)
    print(f"Data from {url}")
    return requests.get(url=url).url


async def main() -> None:
    urls = [
        "https://www.arjancodes.com",
        "https://www.google.com",
        "https://www.python.org",
    ]
    data = await asyncio.gather(*[fetch_data(url=url) for url in urls])
    print(f"Result: {data}")


if __name__ == "__main__":
    asyncio.run(main())