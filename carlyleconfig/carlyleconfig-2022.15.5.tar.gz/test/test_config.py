import os
import sys
import subprocess
import json

import pytest


from carlyleconfig import deriveconfig, derive


@pytest.mark.parametrize(
    "args,env,expected",
    [
        ([], {}, {"debug": False}),
        (["--debug"], {}, {"debug": True}),
        ([], {"TEST_CONFIG_DEBUG": "foo"}, {"debug": True}),
        ([], {"TEST_CONFIG_DEBUG": ""}, {"debug": False}),
        ([], {"TEST_CONFIG_DEBUG": "1"}, {"debug": True}),
        (["--debug"], {"TEST_CONFIG_DEBUG": "1"}, {"debug": True}),
        (["--debug"], {"TEST_CONFIG_DEBUG": ""}, {"debug": True}),
    ],
)
def test_config_program(args, env, expected):
    path = os.path.join(os.path.dirname(__file__), "config.py")
    p = subprocess.run(
        [sys.executable, path] + args,
        env=env,
        encoding="utf-8",
        capture_output=True,
    )
    loaded = json.loads(p.stdout)
    assert loaded == expected


def test_key_program():
    path = os.path.join(os.path.dirname(__file__), "key.py")
    p = subprocess.run(
        [sys.executable, path],
        env={},
        encoding="utf-8",
        capture_output=True,
    )
    loaded = p.stdout.strip().split("\n")
    assert loaded == [
        "['foo', 'baz']",
        "['foo', 'bar']",
        "['bar', 'baz']",
    ]


def test_repr():
    @deriveconfig
    class Config:
        foo: str = derive.field().from_constant("foo")
        bar: str = derive.field().from_constant("bar")

    config = Config()
    value = str(config)
    assert value == "{'bar': 'bar', 'foo': 'foo'}"


def test_sensitive_field():
    @deriveconfig
    class Config:
        secret: str = derive.field(sensitive=True).from_constant("secret")

    config = Config()
    value = str(config)
    assert value == "{'secret': '*****'}"
