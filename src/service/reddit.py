import praw
from model.drg import DeepDive, DeepDiveType


class RedditService:
    def __init__(self, client_id: str, client_secret: str, user_agent: str, check_for_async: bool):
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self.user_agent: str = user_agent
        self.check_for_async: bool = check_for_async

    def get_weekly_deep_dives(self):
        try:
            print('INFO: Getting deep dive details')
            reddit = praw.Reddit(
                client_id=self.client_id,
                client_secret=self.client_secret,
                user_agent=self.user_agent,
                check_for_async=False
            )
            submission = next(reddit.subreddit("DeepRockGalactic").search(query="Weekly Deep Dives Thread",
                                                                          sort="hot",
                                                                          time_filter="week"))
            deep_dives = self.__parse_details(url=str(submission.url),
                                              title=str(submission.title),
                                              text=str(submission.selftext))
            print('SUCCESS: Got weekly deep dives')
            return deep_dives
        except Exception as e:
            print(f'FAILURE: Failed to get weekly deep dives exception={str(e)}')
            return None

    # TODO: Update this
    def __parse_details(url: str, title: str, text: str) -> list[DeepDive]:
        deep_dives: list[DeepDive] = []
        lines = text.split('\n')
        
        # Date (ex: September 26th, 2019)
        date_arr = title.split(" - ")[1].split(" ")
        date = f'{date_arr[1]} {date_arr[0]}, {date_arr[2]}'

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
