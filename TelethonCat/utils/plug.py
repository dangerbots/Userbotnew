import importlib
import logging
import os
import sys
from pathlib import Path

from catconfig import Config
from telethon.tl.types import InputMessagesFilterDocument
from TelethonCat.clients.client_list import client_id
from TelethonCat.clients.decs import cat_cmd
from TelethonCat.clients.logger import LOGGER as LOGS
from TelethonCat.clients.session import H2, H3, H4, H5, Hell, HellBot
from TelethonCat.utils.cmds import CmdHelp
from TelethonCat.utils.decorators import admin_cmd, command, sudo_cmd
from TelethonCat.utils.extras import delete_hell, edit_or_reply
from TelethonCat.utils.globals import LOAD_PLUG


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import TelethonCat.utils

        path = Path(f"TelethonCat/plugins/{shortname}.py")
        name = "TelethonCat.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("DANGERCAT - Successfully imported " + shortname)
    else:
        import TelethonCat.utils

        path = Path(f"TelethonCat/plugins/{shortname}.py")
        name = "TelethonCat.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Hell
        mod.H1 = Hell
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.Hell = Hell
        mod.HellBot = HellBot
        mod.tbot = HellBot
        mod.tgbot = Hell.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        mod.Config = Config
        mod.borg = Hell
        mod.hellbot = Hell
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_hell = delete_hell
        mod.eod = delete_hell
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.cat_cmd = cat_cmd
        mod.sudo_cmd = sudo_cmd
        sys.modules["userbot.utils"] = TelethonCat
        sys.modules["userbot"] = TelethonCat
        sys.modules["userbot.events"] = TelethonCat
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["TelethonCat.plugins." + shortname] = mod
        LOGS.info("⚡ DANGERCAT ⚡ - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                Hell.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"TelethonCat.plugins.{shortname}"

            for i in reversed(range(len(Hell._event_builders))):
                ev, cb = Hell._event_builders[i]
                if cb.__module__ == name:
                    del Hell._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel != 0:
        LOGS.info("⚡ DANGERCAT ⚡ - PLUGIN CHANNEL DETECTED.")
        LOGS.info("⚡ DANGERCAT ⚡ - Starting to load extra plugins.")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"TelethonCat/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "TelethonCat/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))


# hellbot
