import praw
from deep_dive_type import DeepDiveType
from deep_dive import DeepDive


def get_deep_dive_details(reddit_client_id: str, reddit_client_secret: str, deep_dive_type: DeepDiveType):
    try:
        print('INFO: Getting deep dive details')
        reddit = praw.Reddit(
            client_id=reddit_client_id,
            client_secret=reddit_client_secret,
            user_agent="discord:dev.boscobot",
            check_for_async=False
        )
        submission = reddit.subreddit("DeepRockGalactic").sticky()
        date = parse_date(str(submission.title))
        url = str(submission.url)
        text = str(submission.selftext)
        deep_dives = parse_details(text, date, url)
        print('SUCCESS: Got deep dive details')
        return deep_dives
    except Exception as e:
        print(f'FAILURE: Failed to get deep dive details exception={str(e)}')
        return None


def parse_date(title: str):
    date = title.split(" - ")[1].split(" ")
    return f'{date[1]} {date[0]}, {date[2]}'


def parse_details(text: str, date: str, url: str):
    deep_dives = []
    lines = text.split('\n')

    # Deep Dive
    dd_about = lines[4].replace("*", "").split(" | ")
    dd = DeepDive(DeepDiveType.DEEP_DIVE, dd_about[1], dd_about[2], date, url)
    dd_stages = [lines[8].split("|"), lines[9].split("|"), lines[10].split("|")]
    for dd_stage in dd_stages:
        dd.add_stage(dd_stage[1], dd_stage[2], dd_stage[3], dd_stage[4], dd_stage[5])
    deep_dives.append(dd)

    # Elite Deep Dive
    edd_about = lines[12].replace("*", "").split(" | ")
    edd = DeepDive(DeepDiveType.ELITE_DEEP_DIVE, edd_about[1], edd_about[2], date, url)
    edd_stages = [lines[16].split("|"), lines[17].split("|"), lines[18].split("|")]
    for edd_stage in edd_stages:
        edd.add_stage(edd_stage[1], edd_stage[2], edd_stage[3], edd_stage[4], edd_stage[5])
    deep_dives.append(edd)

    return deep_dives
