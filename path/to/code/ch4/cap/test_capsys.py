from sys import stderr
import sys

def greeting(name):
    print('Hello, {}'.format(name))

def test_greeting(capsys):
    greeting('world')
    out, err = capsys.readouterr()
    assert out == "Hello, world\n"
    assert err == ""

    greeting('sweets')
    greeting('honey')
    out, err = capsys.readouterr()
    assert out == "Hello, sweets\nHello, honey\n"
    assert err == ""

def yikes(problem):
    print('YIKES! {}'.format(problem), file=sys.stderr)

def test_yikes(capsys):
    yikes("no problem")
    out, err = capsys.readouterr()
    assert out == ""                     # nothing printed to stdout
    assert "no problem" in err           # stderr contains the message

def test_capsys_disabled(capsys):
    with capsys.disabled():
        print('\nalways print this')   # this bypasses capture, always on console
    print('normal print, usually captured')  # this gets captured by pytest

    out, err = capsys.readouterr()   
    assert 'normal print, usually captured' in out
    assert err == ""  # nothing went to stderr
