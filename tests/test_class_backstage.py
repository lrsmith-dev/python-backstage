import backstage
import pytest

metadata = {
    "name" : "o11y",
}


def test_backstageClass_requiredFields():
    obj = backstage.Backstage(kind="group",
                              name="o11y")
    assert obj.name == "o11y"
    assert obj.kind == "group"
    assert obj.apiversion == "backstage.io/v1alpha1"

def test_print_backstageClass(capsys):
    print(backstage.Backstage(kind="group",
                              name="o11y",
                              ))

    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: group
metadata:
  name: o11y

"""
    assert captured.out == expected