from catconfig import Config, db_config, os_config
from TelethonCat import HEROKU_APP, StartTime
from TelethonCat.clients.client_list import (client_id, clients_list,
                                             get_user_id)
from TelethonCat.clients.decs import dcat_cmd, dcat_handler
from TelethonCat.clients.instaAPI import InstaGram
from TelethonCat.clients.logger import LOGGER
from TelethonCat.clients.session import (H2, H3, H4, H5, Hell, HellBot,
                                         validate_session)
from TelethonCat.DB import gvar_sql
from TelethonCat.helpers.anime import *
from TelethonCat.helpers.classes import *
from TelethonCat.helpers.convert import *
from TelethonCat.helpers.exceptions import *
from TelethonCat.helpers.formats import *
from TelethonCat.helpers.gdriver import *
from TelethonCat.helpers.google import *
from TelethonCat.helpers.ig_helper import *
from TelethonCat.helpers.image import *
from TelethonCat.helpers.int_str import *
from TelethonCat.helpers.mediatype import *
from TelethonCat.helpers.mmf import *
from TelethonCat.helpers.movies import *
from TelethonCat.helpers.pasters import *
from TelethonCat.helpers.pranks import *
from TelethonCat.helpers.progress import *
from TelethonCat.helpers.runner import *
from TelethonCat.helpers.tools import *
from TelethonCat.helpers.tweets import *
from TelethonCat.helpers.users import *
from TelethonCat.helpers.vids import *
from TelethonCat.helpers.yt_helper import *
from TelethonCat.strings import *
from TelethonCat.utils.cmds import *
from TelethonCat.utils.decorators import *
from TelethonCat.utils.errors import *
from TelethonCat.utils.extras import *
from TelethonCat.utils.funcs import *
from TelethonCat.utils.globals import *
from TelethonCat.utils.plug import *
from TelethonCat.utils.startup import *
from TelethonCat.version import __dcatver__, __telever__

cjb = "./catconfig/resources/pics/cjb.jpg"
cat_logo = "./catconfig/resources/pics/dcatlogo.jpg"
restlo = "./catconfig/resources/pics/rest.jpeg"
shhh = "./catconfig/resources/pics/chup_madarchod.jpeg"
shuru = "./catconfig/resources/pics/shuru.jpg"
spotify_logo = "./catconfig/resources/pics/spotify.jpg"


cat_emoji = Config.EMOJI_IN_HELP
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hellbot_version = __dcatver__
telethon_version = __telever__
abuse_m = "Enabled" if str(Config.ABUSE).lower() in enabled_list else "Disabled"
is_sudo = "True" if gvar_sql.gvarstat("SUDO_USERS") else "False"

my_channel = Config.MY_CHANNEL or "danger_bots"
my_group = Config.MY_GROUP or "dangerbots"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/danger_bots"
grp_link = "https://t.me/dangerbots"
dangercat_channel = f"[𝘿𝘼𝙉𝙂𝙀𝙍 𝘾𝘼𝙏]({chnl_link})"
dangercat_grp = f"[𝘿𝘼𝙉𝙂𝙀𝙍 𝘾𝘼𝙏 Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {count} : To get group members
  {first} : To use user first name
  {fullname} : To use user full name
  {last} : To use user last name
  {mention} :  To mention the user
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
  {title} : To get chat name in message
  {userid} : To use userid
  {username} : To use user username
"""

# TelethonCat
