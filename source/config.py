from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 5916492495
bot_user = "UUCC20bot"
api_id = 22230207
api_hash = "efee56194c10eb0d29b3f4fc136e7446"
session = "BAC6EYmlEIrstCaD2dlMq2-8GzgP2V1kZIBP0rVJiArbzymq5PFE8OhbNOVJmLOZQwuKe_918SgdRb2RwlBUAHG9ZHAUHI7ou2ipW86ktEIuczxpYmU81p1Lath67qYYuHbCONTCB7pp3lSM63eD71XwRLewA_f33MhyswjWJvIAD7zGcLFiOm5TCsA77dWbCG4IJLhFPiosXccvkhmI3z33D1zj8oGIsHS3I6i6sNRcRoaHcYqCTywdtUu8H2gpI2Y5yXPm-1_Z6IrzapVBIEIDhtyszxcy597pfv61tz3Z7xpn-VA8TKobKitfYZ8yVNSDAfHEufExcSEwx2BVtoFkAAAAAWCmgs8A"
token = "6135895794:AAHqX_yA5_V11Wp3cU4Mi4UaiwxGqTY5UDk"
sudo_command = [5656828413, 5916492495]
pm = "-1001804255843"
mention = "-1001804255843"
plugins = dict(root="plugins")
app = Client("user:Amrsabrrybot",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("Amrsabrrybot",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
