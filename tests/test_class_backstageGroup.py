import backstage
import pytest


def test_backstageGroupClass_requiredFields_noChildren(capsys):
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team")
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: Group
metadata:
  name: o11y
spec:
  children: []
  type: team

"""
    assert obj.type == "team"
    assert obj.children == []
    assert captured.out == expected

def test_backstageGroupClass_requiredFields_withChildren(capsys):
    logging = backstage.BackstageGroup(name="team-logging",
                                   type="team")
    metrics = backstage.BackstageGroup(name="team-metrics",
                                   type="team")
    traces = backstage.BackstageGroup(name="team-traces",
                                   type="team")
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   children= [ logging, metrics, traces])
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: Group
metadata:
  name: o11y
spec:
  children:
  - team-logging
  - team-metrics
  - team-traces
  type: team

"""
    assert captured.out == expected
    assert obj.type == "team"
    # Refactor to verify names or new test to verify name?
    assert obj.children == [ logging, metrics, traces ]

def test_backstageGroupClass_withParent(capsys):
    parent = backstage.BackstageGroup(name="engineering",
                                   type="team" )
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   parent = parent )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: Group
metadata:
  name: o11y
spec:
  children: []
  parent: engineering
  type: team

"""
    assert captured.out == expected
    assert obj.parent.name == "engineering"

def test_backstageGroupClass_withMembers(capsys):
    john = backstage.BackstageUser(name="John Doe")
    jane = backstage.BackstageUser(name="Jane Doe")
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   members = [ john, jane] )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: Group
metadata:
  name: o11y
spec:
  children: []
  members:
  - John Doe
  - Jane Doe
  type: team

"""
    assert obj.members == [ john, jane ]
    assert captured.out == expected

def test_backstageGroupClass_withdisplayName(capsys):
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   displayName = "The Observability Team" )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: Group
metadata:
  name: o11y
spec:
  children: []
  profile:
    displayName: The Observability Team
  type: team

"""
    assert obj.displayName == "The Observability Team"
    assert captured.out == expected

def test_backstageGroupClass_withEmail(capsys):
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   email = "o11y@big.brother" )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: Group
metadata:
  name: o11y
spec:
  children: []
  profile:
    email: o11y@big.brother
  type: team

"""
    assert obj.email == "o11y@big.brother"
    assert captured.out == expected

def test_backstageGroupClass(capsys):
    parent = backstage.BackstageGroup(name="engineering",
                                   type="team" )
    logging = backstage.BackstageGroup(name="team-logging",
                                   type="team")
    metrics = backstage.BackstageGroup(name="team-metrics",
                                   type="team")
    traces = backstage.BackstageGroup(name="team-traces",
                                   type="team")
    john = backstage.BackstageUser(name="John Doe")
    jane = backstage.BackstageUser(name="Jane Doe")
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   members = [ john, jane],
                                   parent = parent,
                                   displayName = "The Observability Team",
                                   children= [logging, metrics,traces],
                                   email = "o11y@big.brother" )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: Group
metadata:
  name: o11y
spec:
  children:
  - team-logging
  - team-metrics
  - team-traces
  members:
  - John Doe
  - Jane Doe
  parent: engineering
  profile:
    displayName: The Observability Team
    email: o11y@big.brother
  type: team

"""
    assert captured.out == expected