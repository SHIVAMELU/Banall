import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from .config import Config
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot = Client(":memory:", api_id=Config.TELEGRAM_APP_ID, api_hash=Config.TELEGRAM_APP_HASH, bot_token=Config.TELEGRAM_TOKEN)

async def ban_all_members(chat_id: int):
    async for i in bot.iter_chat_members(chat_id):
        try:
            await bot.ban_chat_member(chat_id=chat_id, user_id=i.user.id)
            print("kicked {} from {}".format(i.user.id, chat_id))
        except Exception as e:
            print("failed to kick {} from {}: {}".format(i.user.id, chat_id, e))
    print("process completed")

async def unban_user(chat_id: int, user_id: int):
    try:
        await bot.unban_chat_member(chat_id=chat_id, user_id=user_id)
        print("unbanned {} from {}".format(user_id, chat_id))
    except Exception as e:
        print("failed to unban {} from {}: {}".format(user_id, chat_id, e))

@bot.on_message(filters.command(["banall", "fuckall", "tmkc", "tatakai", "rumbling", "chudaistart"]))
async def ban_all_command(bot: Client, message: Message):
    # The ban_all_command code from the previous solution remains unchanged.

@bot.on_message(filters.command(["unban"]))
async def unban_command(bot: Client, message: Message):
    if message.chat.type in ("supergroup", "channel"):
        # Extract the group ID and user ID from the command
        command_parts = message.text.split()
        if len(command_parts) == 3:
            group_id = command_parts[1]
            user_id = command_parts[2]
            if group_id.startswith('-100') and group_id[4:].isdigit() and user_id.isdigit():
                try:
                    group_id = int(group_id)
                    user_id = int(user_id)
                    await unban_user(group_id, user_id)
                    await message.reply_text(f"Successfully unbanned user {user_id} in group {group_id}.")
                except Exception as e:
                    await message.reply_text(f"Failed to unban user {user_id} in group {group_id}: {e}")
            else:
                await message.reply_text("Please provide valid group ID (should start with -100) and user ID.")
        else:
            await message.reply_text("Please provide a valid group ID and user ID after the command.")
    else:
        await message.reply_text("This command can only be used in supergroups or channels.")

@bot.on_message(filters.command("start") & filters.private)
async def hello(bot: Client, message: Message):
    await message.reply_text("Hello, This Is a Banall Bot, I can Ban and Unban Members Within seconds!\n\n Simply give me Ban rights in the targeted group and give the command /banall, or you can use alternative commands like /tmkc, /tatakai, /rumbling, /chudaistart, fuckall\n\nTo unban, use the command /unban (group_id) (user_id)")
