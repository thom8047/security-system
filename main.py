import asyncio
from src import Security


async def main():
    """Main execution"""
    security = Security()

    async def multiple_writing(i):
        """testing method
        Args:
            i (int): number
        """
        await asyncio.sleep(5)
        security.write_output_to_lcd(f"Awaited 5 seconds {i}")
        await multiple_writing(i + 1)

    # Run various security methods asynchronously
    await asyncio.gather(
        security.handle_toggle_button_interaction(),
        multiple_writing(0),
    )


if __name__ == "__main__":
    asyncio.run(main())
