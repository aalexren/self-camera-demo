import aiohttp

from app.config import get_settings


ZITADEL_DOMAIN = get_settings().CLIENT_ISSUER
CLIENT_ID = get_settings().CLIENT_ID
CLIENT_SECRET = get_settings().CLIENT_SECRET

async def validate_pat(pat):
    url = f"{ZITADEL_DOMAIN}/oauth/v2/introspect"
    data = {"token": pat, "token_type_hint": "access_token", "scope": "openid"}
    auth = aiohttp.BasicAuth(CLIENT_ID, CLIENT_SECRET)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, auth=auth) as resp:
            resp.raise_for_status()
            return await resp.json()