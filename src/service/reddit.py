import praw
from model.drg import Anomaly, Biome, DeepDive, DeepDiveStage, DeepDiveType, Warning
from util.string import to_screaming_snake_case, to_title_case


class RedditService:
    def __init__(self, client_id: str, client_secret: str, user_agent: str, check_for_async: bool):
        self.client_id: str = client_id
        self.client_secret: str = client_secret
        self.user_agent: str = user_agent
        self.check_for_async: bool = check_for_async

    def get_weekly_deep_dives(self) -> list[DeepDive]:
        try:
            print('INFO: Getting deep dive details')
            reddit = praw.Reddit(
                client_id=self.client_id,
                client_secret=self.client_secret,
                user_agent=self.user_agent,
                check_for_async=self.check_for_async
            )
            threads = reddit.subreddit("DeepRockGalactic").search(query="Weekly Deep Dives Thread",
                                                                  sort="hot",
                                                                  time_filter="week")
            top_thread = next(threads)
            deep_dives = self.__parse_details(url=str(top_thread.url),
                                              title=str(top_thread.title),
                                              text=str(top_thread.selftext))
            print('SUCCESS: Got weekly deep dives')
            return deep_dives
        except Exception as e:
            print(f'FAILURE: Failed to get weekly deep dives exception={str(e)}')
            return None

    def __parse_details(self, url: str, title: str, text: str) -> list[DeepDive]:
        date = self.__parse_date(title)
        lines = text.split('\n')
        return [
            self.__parse_deep_dive_details(DeepDiveType.DEEP_DIVE, lines, date, url),
            self.__parse_deep_dive_details(DeepDiveType.ELITE_DEEP_DIVE, lines, date, url)
        ]

    def __parse_date(self, title: str) -> str:
        date_arr = title.split(" - ")[1].split(" ")
        date = f'{date_arr[1]} {date_arr[0]}, {date_arr[2]}'
        return date

    def __parse_deep_dive_details(self,
                                  dive_type: DeepDiveType,
                                  lines: list[str],
                                  date: str,
                                  url: str) -> DeepDive:
        index = 4 if dive_type == DeepDiveType.DEEP_DIVE else 12
        about = lines[index].replace("*", "").split(" | ")
        raw_stages = [lines[index+4].split("|"),
                      lines[index+5].split("|"),
                      lines[index+6].split("|")]
        stages: list[DeepDiveStage] = []

        for raw_stage in raw_stages:
            stages.append(DeepDiveStage(stage=int(raw_stage[1]),
                                        primary=raw_stage[2],
                                        secondary=raw_stage[3],
                                        anomaly=Anomaly[to_screaming_snake_case(raw_stage[4])],
                                        warning=Warning[to_screaming_snake_case(raw_stage[5])]))

        return DeepDive(type=dive_type,
                        name=to_title_case(about[1]),
                        biome=Biome[to_screaming_snake_case(about[2])],
                        date=date,
                        url=url,
                        stages=stages)
