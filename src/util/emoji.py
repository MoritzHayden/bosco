from typing import Union, TYPE_CHECKING
import emoji
from util.constants import CUSTOM_EMOJIS

if TYPE_CHECKING:
    from model.deepdives import Anomaly, MissionType, Warning

def get_emoji(model: Union["MissionType", "Warning", "Anomaly", None]) -> Union[str, None]:
    DEFAULT_EMOJI = emoji.emojize(':black_medium_square:');
    if(model == None):
        return DEFAULT_EMOJI
    return CUSTOM_EMOJIS.get(model.value, DEFAULT_EMOJI)
