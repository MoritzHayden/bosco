from typing import Union, TYPE_CHECKING
import emoji
from util.constants import CUSTOM_EMOJIS, DEFAULT_EMOJI

if TYPE_CHECKING:
    from model.deepdives import Anomaly, MissionType, Warning

def get_emoji(model: Union["MissionType", "Warning", "Anomaly", None]) -> Union[str, None]:
    return DEFAULT_EMOJI if model is None else CUSTOM_EMOJIS.get(model.value, DEFAULT_EMOJI)
