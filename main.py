import asyncio
from src import Security


async def main():
    """Main execution"""
    security = {}
    security.operation = Security()

    # Run various security methods asynchronously
    asyncio.run(security.operation.handle_toggle_button_interaction())


if __name__ == "__main__":
    asyncio.run(main())
