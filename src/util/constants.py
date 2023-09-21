BOSCO_WEBSITE_TEXT: str = 'Website'
BOSCO_WEBSITE_URL: str = 'https://boscobot.dev/'
BOSCO_INVITE_TEXT: str = 'Invite to Server'
BOSCO_INVITE_URL: str = 'https://discord.com/api/oauth2/authorize' \
                        '?client_id=1097476432579539026&permissions=2147485696&scope=bot'
ERROR_RESPONSE_TEXT: str = 'Oops, something went wrong! Please try again later.'
DRG_API_BASE_URL: str = 'https://drgapi.com'
DRG_API_VERSION: str = '/v1'
DRG_API_DEEPDIVES_ENDPOINT: str = '/deepdives'
DRG_API_SALUTES_ENDPOINT: str = '/salutes'
DRG_API_TRIVIA_ENDPOINT: str = '/trivia'
DRG_API_TIMEOUT_SECONDS: int = 3
CUSTOM_EMOJIS: dict[str] = {
    # Mission types
    'Mining Expedition': '<:mining:1147866170767196270>',
    'Egg Hunt': '<:egg:1147866162890285118>',
    'On-Site Refining': '<:refining:1147866175485780060>',
    'Salvage Operation': '<:salvage:1147866180426682418>',
    'Point Extraction': '<:point:1147866173422194769>',
    'Escort Duty': ' <:escort:1147866168586141717>',
    'Elimination': '<:elimination:1147866166061174914>',
    'Black Box': '<:blackbox:1147866161208373399>',
    'Industrial Sabotage': '<:sabotage:1147866177964609557>',

    # Warnings
    'Cave Leech Cluster': '<:leech:1147874362960138362>',
    'Elite Threat': '<:elite:1147874358375747725>',
    'Exploder Infestation': '<:exploder:1147874360808460448>',
    'Haunted Cave': '<:haunted:1147874362028986389>',
    'Lethal Enemies': '<:lethal:1147874365669658624>',
    'Low Oxygen': '<:oxygen:1147874369561952327>',
    'Mactera Plague': '<:mactera:1147874367116685373>',
    'Parasites': '<:parasites:1147874370862198814>',
    'Regenerative Bugs': '<:regenerative:1147874372451848202>',
    'Rival Presence': '<:rival:1147874374993580184>',
    'Shield Disruption': '<:shield:1147874376537100391>',
    'Swarmageddon': '<:swarmageddon:1147874410934571018>',

    # Anomalies
    'Critical Weakness': '<:crticial:1147881857879396423>',
    'Double XP': '<:double:1147881859993325579>',
    'Gold Rush': '<:gold:1147881862182739980>',
    'Golden Bugs': '<:bugs:1147881856142938162>',
    'Low Gravity': '<:gravity:1147881863793344542> ',
    'Mineral Mania': '<:mineral:1147881864992923749>',
    'Rich Atmosphere': '<:rich:1147881867744395314>',
    'Volatile Guts': '<:volatile:1147881869438890114>'
}
