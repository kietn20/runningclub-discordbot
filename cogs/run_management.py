from discord.ext import commands
from database import get_db_connection

class RunManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='announce')
    async def announce_run(self, ctx, date: str, time: str):
        """Announce an upcoming run."""
        announcement = f"🏃‍♂️ Upcoming Run 🏃‍♀️\nDate: {date}\nTime: {time}"
        await ctx.send(announcement)
        
    @commands.command(name='log')
    async def log_run(self, ctx, date: str, distance: float, time: str, calories: int, 
                      total_calories: int, time_start: str, time_end: str, 
                      average_pace: str, first_mile_time: str):
        """Log a completed run."""
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO runs (date, distance, time, calories, total_calories, 
                              time_start, time_end, average_pace, first_mile_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (date, distance, time, calories, total_calories, time_start, time_end, 
              average_pace, first_mile_time))
        conn.commit()
        conn.close()
        await ctx.send("Run logged successfully!")
    
def setup(bot):
    bot.add_cog(RunManagement(bot))