BOSCO_WEBSITE_TEXT: str = 'Website'
BOSCO_WEBSITE_URL: str = 'https://boscobot.dev/'
BOSCO_INVITE_TEXT: str = 'Invite to Server'
BOSCO_INVITE_URL: str = 'https://discord.com/api/oauth2/authorize' \
                        '?client_id=1097476432579539026&permissions=2147747840&scope=bot'
ERROR_RESPONSE_TEXT: str = 'Oops, something went wrong! Please try again later.'
DRG_API_BASE_URL: str = 'https://drgapi.com'
DRG_API_VERSION: str = '/v1'
DRG_API_DEEPDIVES_ENDPOINT: str = '/deepdives'
DRG_API_SALUTES_ENDPOINT: str = '/salutes'
DRG_API_TRIVIA_ENDPOINT: str = '/trivia'
DRG_API_TIMEOUT_SECONDS: int = 3
DEFAULT_EMOJI = ':black_medium_square:'
DEEP_DIVE_IMAGE_URL = 'https://i.imgur.com/S8duBIv.png'
CUSTOM_EMOJIS: dict[str, str] = {
    # Mission types
    'Mining Expedition': '<:mining:1155632856845000805>',
    'Egg Hunt': '<:egghunt:1155632746237001791>',
    'On-Site Refining': '<:refining:1155665375447494717>',
    'Salvage Operation': '<:salvage:1155665418053230642>',
    'Point Extraction': '<:point:1155665373140619334>',
    'Escort Duty': ' <:escort:1155632782110892082>',
    'Elimination': '<:elimination:1155632779250380951>',
    'Black Box': '<:blackbox:1155632740855722076>',
    'Industrial Sabotage': '<:sabotage:1155665416803319818>',

    # Warnings
    'Cave Leech Cluster': '<:leech:1155632822791438346>',
    'Elite Threat': '<:elite:1155632780311547904>',
    'Exploder Infestation': '<:exploder:1155632783079776256>',
    'Haunted Cave': '<:haunted:1155632821302480896>',
    'Lethal Enemies': '<:lethal:1155632824527884390>',
    'Low Oxygen': '<:oxygen:1155632858283643000>',
    'Mactera Plague': '<:mactera:1155632826696335400>',
    'Parasites': '<:parasites:1155632859500003349>',
    'Regenerative Bugs': '<:regenerative:1155665376626090075>',
    'Rival Presence': '<:rival:1155665379763421254>',
    'Shield Disruption': '<:shielddisruption:1155665420846649364>',
    'Swarmageddon': '<:swarmageddon:1155665421941354496>',

    # Anomalies
    'Critical Weakness': '<:critical:1155632743401660497>',
    'Double XP': '<:double:1155632743959503001>',
    'Gold Rush': '<:gold:1155632784086405150>',
    'Golden Bugs': '<:bugs:1155632742021726349>',
    'Low Gravity': '<:gravity:1155632820375527515>',
    'Mineral Mania': '<:mineral:1155632855913861253>',
    'Rich Atmosphere': '<:rich:1155665377976647810>',
    'Volatile Guts': '<:volatile:1155665423535198318>'
}
