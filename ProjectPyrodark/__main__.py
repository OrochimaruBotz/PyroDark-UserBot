# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/darkosupport & t.me/lyoc0de

import importlib

from pyrogram import idle
from uvloop import install

from config import *
from ProjectPyrodark import BOTLOG_CHATID, LOGGER, LOOP, bots
from ProjectPyrodark.helpers.misc import git, heroku

MSG_ON = """
😈 **PyroDark-UserBot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk mengecek Bot**
━━
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("lyoc0de")
            await bot.join_chat("darkosupport")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
        except Exception as a:
            LOGGER("main").warning(a)
    await idle()


if __name__ == "__main__":
    LOGGER("ProjectPyrodark").info("Starting PYRODARK-USERBOT")
    LOGGER("ProjectPyrodark").info(f"Total Clients = {len(bots)} Users")
    install()
    git()
    heroku()
    LOGGER("ProjectPyrodark").info(
        f"PyroDark-UserBot v{BOT_VER} [😈 BERHASIL DIAKTIFKAN! 😈]"
    )
    LOOP.run_until_complete(main())
