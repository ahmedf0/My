from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "24776367")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "ce1018f501c41724b883bf706165a0e9")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "6180610264:AAGZdr4iRAiW5XIgev8WpbgWEUBfCk3BMnE")
SESSION_NAME = getenv("SESSION_NAME", "BQBvuRFaNBC7HZsGabz2oX-jgcrx9um-_pG7eak31xWIkLGNFGCOCrFEWr68kO9nC5z-kKAbXW_rrIKE0HvwK6z04wNnRIzEaRrTcc2WX8GD3MVcrwD3WuSG6ztLIbVvCHLkmyfAqiPwUbXKgf789J6N0VRjVpKY06u5unXBD0V1GjPb-S6q372ETzf5yhb-PbrOuyrsGqBWeouS_qcl5T39H6I5UFUMJWsfTHKU8JcqsaMYPBcTgmWmIn_yZN4WwiA0uMFJYMxbHHV7g8h87ERfWRkNTwPezkQYv3bFokq_gs9bRhlYZrOpx6p-28eBcZv8AqA3Qz8PcLSmDfL-qDJTAAAAAXAFlSsA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "k5kil") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "ahmed") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "FDFDRFE4BOT") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "k5kil") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "k5kil") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://storefireff:JxoeJzWtMHksqt1g@cluster0.60lxfsh.mongodb.net/?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1486460019").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1486460019").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
