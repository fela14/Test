def pytest_addoption(parser):
    parser.addoption(
        "--myopt", 
        action="store_true", 
        help="some boolean option")
    parser.addoption(
        "--foo", 
        action="store", 
        default="bar", 
        help="foo: bar or baz")
    parser.addoption(
        "--mychoice",
        action="store_false",
        help="my boolean choice")
    parser.addoption(
        "--city",
        action="store",
        default="southy",
        help="city: southy or whatever")