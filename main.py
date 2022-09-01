from src import Security
import asyncio


async def main():
    """Main execution"""
    SECURITY_CLASS = Security()

    # Run various security methods asynchronously
    asyncio.run(SECURITY_CLASS.handle_button())


if __name__ == "__main__":
    asyncio.run(main())
