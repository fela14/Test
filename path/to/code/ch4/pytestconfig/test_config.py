import pytest

def test_option(pytestconfig):
    print('"foo" set to: ', pytestconfig.getoption('foo'))
    print('"myopt" set to: ', pytestconfig.getoption('myopt'))
    print('"mychoice" set to: ', pytestconfig.getoption('mychoice'))
    print('"city" set to: ', pytestconfig.getoption('city'))

@pytest.fixture()
def foo(pytestconfig):
    return pytestconfig.option.foo

@pytest.fixture()
def myopt(pytestconfig):
    return pytestconfig.option.myopt

@pytest.fixture()
def mychoice(pytestconfig):
    return pytestconfig.option.mychoice

@pytest.fixture()
def city(pytestconfig):
    return pytestconfig.option.city

def test_fixtures_for_options_a(foo, myopt):
    print('"foo" set to: ', foo)
    print('"myopt" set to: ', myopt)

def test_fixtures_for_options_b(mychoice, city):  
    print('"mychoice" set to: ', mychoice)
    print('"city" set to: ', city)

#------------------------------------------------------------
# Pytest built-in values
#------------------------------------------------------------

def test_pytestconfig(pytestconfig):
    print('args :', pytestconfig.args)
    print('inifile :', pytestconfig.inifile)
    print('invocation_dir :', pytestconfig.invocation_dir)
    print('rootdir :', pytestconfig.rootdir)
    print('-k EXPRESSION :', pytestconfig.getoption('keyword'))
    print('-v, --verbose :', pytestconfig.getoption('verbose'))
    print('-q, --quiet :', pytestconfig.getoption('quiet'))
    print('-l, --showlocals:', pytestconfig.getoption('showlocals'))
    print('--tb=style :', pytestconfig.getoption('tbstyle'))
