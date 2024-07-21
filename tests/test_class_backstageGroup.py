import backstage
import pytest


def test_backstageGroupClass_requiredFields_noChildren(capsys):
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team")
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: group
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
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   children= ['team-logging','team-metrics','team-traces'])
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: group
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
    assert obj.children == [ 'team-logging', 'team-metrics', 'team-traces' ]

def test_backstageGroupClass_withParent(capsys):
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   parent = "engineering" )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: group
metadata:
  name: o11y
spec:
  children: []
  parent: engineering
  type: team

"""
    assert captured.out == expected
    assert obj.parent == "engineering"

def test_backstageGroupClass_withMembers(capsys):
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   members = [ 'John Doe', 'Jane Doe'] )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: group
metadata:
  name: o11y
spec:
  children: []
  members:
  - John Doe
  - Jane Doe
  type: team

"""
    assert obj.members == [ 'John Doe', 'Jane Doe']
    assert captured.out == expected



def test_backstageGroupClass_withDisplayname(capsys):
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   displayname = "The Observability Team" )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: group
metadata:
  name: o11y
spec:
  children: []
  profile:
    displayName: The Observability Team
  type: team

"""
    assert obj.displayname == "The Observability Team"
    assert captured.out == expected

def test_backstageGroupClass_withEmail(capsys):
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   email = "o11y@big.brother" )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: group
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
    obj = backstage.BackstageGroup(name="o11y",
                                   type="team",
                                   members = [ 'John Doe', 'Jane Doe'],
                                   parent = "engineering",
                                   displayname = "The Observability Team",
                                   children= ['team-logging','team-metrics','team-traces'],
                                   email = "o11y@big.brother" )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: group
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