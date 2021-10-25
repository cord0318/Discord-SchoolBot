BOT_TOKEN = ""
BOT_ID = ""

PREFIX = ["?", f"<@!{BOT_ID}>", f"<@!{BOT_ID}> "]

OWNER_ID = []

EXTENSION_LIST = []

import os
for e in [f for f in os.listdir("src/extensions") if f.endswith('py')]:
    EXTENSION_LIST.append(f'extensions.{e.replace(".py", "")}')