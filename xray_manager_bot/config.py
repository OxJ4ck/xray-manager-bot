import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="xray_manager_bot",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="xray_manager_bot_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from xray_manager_bot.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export xray_manager_bot_KEY=value
export xray_manager_bot_KEY="@int 42"
export xray_manager_bot_KEY="@jinja {{ this.db.uri }}"
export xray_manager_bot_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
xray_manager_bot_ENV=production xray_manager_bot run
```

Read more on https://dynaconf.com
"""
