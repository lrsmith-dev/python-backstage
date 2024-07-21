import backstage
import pytest


def test_backstageUser_requiredFields_noMemberOf(capsys):

    obj = backstage.BackstageUser(name="zaphod")
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: User
metadata:
  name: zaphod
spec:
  memberOf: []

"""
    assert obj.kind == "User"
    assert obj.name == "zaphod"
    assert obj.memberOf == []
    assert captured.out == expected

def test_backstageUser_requiredFields_withMemberOf(capsys):

    obj = backstage.BackstageUser(name="zaphod",
                                  memberOf = [ 'Heart of Gold' ],
                                  )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: User
metadata:
  name: zaphod
spec:
  memberOf:
  - Heart of Gold

"""
    assert obj.kind == "User"
    assert obj.name == "zaphod"
    assert obj.memberOf == ['Heart of Gold']
    assert captured.out == expected

def test_backstageUser_displayName(capsys):

    obj = backstage.BackstageUser(name="zaphod",
                                  displayName = "Zaphod Beeblebrox"
                                  )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: User
metadata:
  name: zaphod
spec:
  memberOf: []
  profile:
    displayName: Zaphod Beeblebrox

"""
    assert obj.kind == "User"
    assert obj.name == "zaphod"
    assert obj.memberOf == []
    assert captured.out == expected

def test_backstageUser_withEmail(capsys):
    obj = backstage.BackstageUser(name="zaphod",
                                  email = "zaphod@end.universe" )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: User
metadata:
  name: zaphod
spec:
  memberOf: []
  profile:
    email: zaphod@end.universe

"""
    assert obj.email == "zaphod@end.universe"
    assert captured.out == expected

def test_backstageUser(capsys):
    obj = backstage.BackstageUser(name="zaphod",
                                  displayName = "Zaphod Beeblebrox",
                                  memberOf = [ 'Heart of Gold' ],
                                  email = "zaphod@end.universe" )
    print(obj)
    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: User
metadata:
  name: zaphod
spec:
  memberOf:
  - Heart of Gold
  profile:
    displayName: Zaphod Beeblebrox
    email: zaphod@end.universe

"""
    assert obj.email == "zaphod@end.universe"
    assert captured.out == expected