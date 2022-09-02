import asyncio
from src import Security


async def main():
    """Main execution"""
    security = Security()

    # Run various security methods asynchronously
    await asyncio.gather(security.handle_toggle_button_interaction())


if __name__ == "__main__":
    asyncio.run(main())
