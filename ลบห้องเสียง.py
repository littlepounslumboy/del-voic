import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# ================= INIT =================
load_dotenv()
TOKEN = os.getenv("USER_TOKEN")

GUILD_ID = 1420368738686861337      # ใส่ Server ID ของคุณ
CATEGORY_ID = 1421226069167706142   # ใส่ Category ID ที่ต้องการลบห้อง

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True  # ถ้าต้องการลบ voice channels
client = discord.Client(intents=intents)  # discord.py-self จะใช้ Client ปกติ

# ================= EVENT =================
@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user} (id={client.user.id})")

    guild = client.get_guild(GUILD_ID)
    if not guild:
        print("❌ ไม่พบ guild")
        await client.close()
        return

    category = discord.utils.get(guild.categories, id=CATEGORY_ID)
    if not category:
        print("❌ ไม่พบ category")
        await client.close()
        return

    # ================= ลบห้องทั้งหมดใน category =================
    deleted = 0
    for ch in category.voice_channels:
        try:
            await ch.delete(reason="ลบห้องในหมวดหมู่เพื่อสร้างใหม่")
            print(f"ลบห้อง: {ch.name} (id={ch.id})")
            deleted += 1
        except Exception as e:
            print(f"❌ ล้มเหลวลบ {ch.name}: {e}")

    print(f"เสร็จแล้ว — ลบ {deleted} ห้องทั้งหมดใน category '{category.name}'")
    await client.close()

# ================= RUN =================
client.run(TOKEN, bot=False)  # ต้องใส่ bot=False สำหรับ user token
