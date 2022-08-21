# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/darkosupport & t.me/Lyoc0de

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from ProjectPyrodark import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bots
from ProjectPyrodark.helpers.misc import git, heroku

MSG_ON = """
😈 **Gojo-UserBot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecek Bot**
━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("Lunatic0de")
            await bot.join_chat("SharingUserbot")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("ProjectPyrodark").info("Starting Gojo-UserBot")
    LOGGER("ProjectPyrodark").info(f"Total Clients = {len(bots)} Users")
    install()
    git()
    heroku()
    LOGGER("ProjectPyrodark").info(f"Gojo-UserBot v{BOT_VER} [😈 BERHASIL DIAKTIFKAN! 😈]")
    LOOP.run_until_complete(main())
