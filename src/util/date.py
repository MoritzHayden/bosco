from datetime import datetime


def get_ordinal_suffix(day: int) -> str:
    if 11 <= (day % 100) <= 13:
        return 'th'

    return ['th', 'st', 'nd', 'rd', 'th'][min(day % 10, 4)]


def prettify_datetime(iso_datetime: str) -> str:
    parsed_time = datetime.strptime(iso_datetime, "%Y-%m-%dT%H:%M:%SZ")
    month = parsed_time.strftime("%B")
    day = parsed_time.day
    day_suffix = get_ordinal_suffix(day)
    year = parsed_time.year
    formatted_day = str(day) if day >= 10 else str(day).lstrip("0")
    return f'{month} {formatted_day}{day_suffix}, {year}'
