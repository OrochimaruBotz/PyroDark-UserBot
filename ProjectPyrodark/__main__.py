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

from config import BOT_VER, CMD_HANDLER
from ProjectPyrodark import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bots
from ProjectPyrodark.helpers.misc import heroku
from ProjectPyrodark.modules import ALL_MODULES

MSG_ON = """
😈 **PyroDark-UserBot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecek Bot**
━━
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"ProjectPyrodark.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("lyoc0de")
            await bot.join_chat("darkosupport")
            await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            LOGGER("ProjectPyrodark").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("ProjectPyrodark").info(
        f"PyroDark-UserBot v{BOT_VER} [😈 BERHASIL DIAKTIFKAN! 😈]"
    )
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("ProjectPyrodark").info("Starting PyroDark-UserBot")
    install()
    heroku()
    LOOP.run_until_complete(main())
