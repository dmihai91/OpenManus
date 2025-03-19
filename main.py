import asyncio

from app.api.api import API
from app.logger import logger


async def main():
    try:
        api = API()
        api.run()
    except Exception as e:
        logger.error(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
