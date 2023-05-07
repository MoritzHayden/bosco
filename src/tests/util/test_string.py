from util.string import to_screaming_snake_case, to_title_case


class TestString:
    def test_to_screaming_snake_case(self):
        assert to_screaming_snake_case("hello world") == "HELLO_WORLD"
        assert to_screaming_snake_case(" Hello World") == "HELLO_WORLD"
        assert to_screaming_snake_case("hello_world") == "HELLO_WORLD"
        assert to_screaming_snake_case("hello      world    ") == "HELLO_WORLD"
        assert to_screaming_snake_case("") == ""

    def test_to_title_case(self):
        assert to_title_case("hello_world") == "Hello World"
        assert to_title_case("Hello_World") == "Hello World"
        assert to_title_case("HELLO_WORLD") == "Hello World"
        assert to_title_case(" hello_world  ") == "Hello World"
        assert to_title_case("") == ""
