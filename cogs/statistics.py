from discord.ext import commands
from database import get_db_connection

class Statistics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='recent')
    async def view_recent_runs(self, ctx, limit: int = 5):
        """View recent runs."""
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM runs ORDER BY date DESC LIMIT ?', (limit,))
        runs = cur.fetchall()
        conn.close()
        
        if not runs:
            await ctx.send("No recent runs found.")
            return

        response = "Recent Runs:\n"
        for run in runs:
            response += f"Date: {run['date']}, Distance: {run['distance']}km, Time: {run['time']}\n"
        
        await ctx.send(response)

    @commands.command(name='summary')
    async def monthly_summary(self, ctx, year: int, month: int):
        """Generate a summary of runs for a specific month."""
        # Implementation similar to previous example

def setup(bot):
    bot.add_cog(Statistics(bot))