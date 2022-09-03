import asyncio
import datetime
from src import Security


async def main():
    """Main execution"""
    security = Security()

    async def multiple_writing(i):
        """testing method
        Args:
            i (int): number
        """
        await asyncio.sleep(30)
        [hour, minute, suffix] = [
            datetime.datetime.now().hour,
            "{:02d}".format(datetime.datetime.now().minute),
            "PM" if datetime.datetime.now().hour > 11 else "AM",
        ]
        security.clear_lcd_display()
        security.write_output_to_lcd(
            f"Date: {datetime.date.today()}Time: {12 if hour == 0 else hour - 12 if hour > 12 else hour}:{minute} {suffix}"
        )
        await multiple_writing(i + 1)

    # Run various security methods asynchronously
    await asyncio.gather(
        multiple_writing(0),
    )


if __name__ == "__main__":
    asyncio.run(main())
