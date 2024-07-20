import backstage
import pytest

metadata = {
    "name" : "o11y",
}

#    with pytest.raises(Exception) as ValueError:
def test_backstgeClass():
    with pytest.raises(ValueError,match="name not defined in metadata"):
        obj = backstage.Backstage(kind="group",
                                  metadata={})

def test_backstageClass_requiredFields():
    obj = backstage.Backstage(kind="group",
                              metadata=metadata)
    print(obj.name)
    assert obj.name == "o11y"
    assert obj.kind == "group"
    assert obj.apiversion == "backstage.io/v1alpha1"

def test_print_backstageClass(capsys):
    print(backstage.Backstage(kind="group",
                              metadata=metadata,
                              ))

    captured = capsys.readouterr()
    expected = r"""apiVersion: backstage.io/v1alpha1
kind: group
metadata:
  name: o11y

"""
    assert captured.out == expected