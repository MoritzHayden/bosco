from typing import Union, TYPE_CHECKING
from util.constants import CUSTOM_EMOJIS, DEFAULT_EMOJI

if TYPE_CHECKING:
    from model.deepdives import Anomaly, MissionType, Warning

def get_emoji(model: Union["MissionType", "Warning", "Anomaly", None]) -> str:
    return DEFAULT_EMOJI if model is None else CUSTOM_EMOJIS.get(model.value, DEFAULT_EMOJI)
