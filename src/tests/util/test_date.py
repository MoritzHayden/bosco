from util.date import get_ordinal_suffix, prettify_datetime


class TestString:
    def test_get_ordinal_suffix(self):
        assert get_ordinal_suffix(1) == "st"
        assert get_ordinal_suffix(2) == "nd"
        assert get_ordinal_suffix(3) == "rd"
        assert get_ordinal_suffix(4) == "th"
        assert get_ordinal_suffix(5) == "th"
        assert get_ordinal_suffix(10) == "th"
        assert get_ordinal_suffix(11) == "th"
        assert get_ordinal_suffix(12) == "th"
        assert get_ordinal_suffix(13) == "th"
        assert get_ordinal_suffix(14) == "th"
        assert get_ordinal_suffix(15) == "th"
        assert get_ordinal_suffix(20) == "th"
        assert get_ordinal_suffix(21) == "st"
        assert get_ordinal_suffix(22) == "nd"
        assert get_ordinal_suffix(23) == "rd"
        assert get_ordinal_suffix(24) == "th"
        assert get_ordinal_suffix(25) == "th"
        assert get_ordinal_suffix(30) == "th"
        assert get_ordinal_suffix(31) == "st"

    def test_prettify_datetime(self):
        assert prettify_datetime("2023-12-31T23:59:59Z") == "December 31st, 2023"
        assert prettify_datetime("2023-05-18T11:00:00Z") == "May 18th, 2023"
        assert prettify_datetime("2023-05-22T18:45:00Z") == "May 22nd, 2023"
        assert prettify_datetime("2023-05-11T12:30:00Z") == "May 11th, 2023"
        assert prettify_datetime("2023-05-01T09:15:00Z") == "May 1st, 2023"
        assert prettify_datetime("2022-10-15T20:20:20Z") == "October 15th, 2022"
        assert prettify_datetime("2022-02-28T00:00:00Z") == "February 28th, 2022"
        assert prettify_datetime("2022-01-05T08:00:00Z") == "January 5th, 2022"

