import os
import yaml

class Backstage:

    def __init__(self, kind, name, apiVersion=None ):


        self.__apiVersion = 'backstage.io/v1alpha1' if apiVersion is None else apiVersion
        self.__kind = kind

        self.__metadata = {}
        self.__metadata['name'] = name

    @property 
    def apiversion(self): 
        return self.__apiVersion

    @property 
    def kind(self): 
        return self.__kind

    @property 
    def name(self): 
        return self.__metadata['name']

    def __str__(self):
        tmp = {}
        tmp['metadata'] = self.__metadata

        if hasattr(self,"spec"):
            tmp['spec'] = self.spec

        return (f'apiVersion: {self.apiversion}\n'
                f'kind: {self.kind}\n' + 
                yaml.dump(tmp) 
                )

# https://backstage.io/docs/features/software-catalog/descriptor-format#kind-user
class BackstageUser(Backstage):
    def __init__(self,
                 name,
                 apiversion = None,
                 displayName=None,  # Optional field
                 email=None,        # Optional field
                 memberOf = [],
                 ):

        self.__spec = {}
        self.__spec['memberOf'] = memberOf

        if displayName is not None:
            if 'profile' not in self.__spec:
                self.__spec['profile'] = {}
            self.__spec['profile']['displayName'] = displayName

        if email is not None:
            if 'profile' not in self.__spec:
                self.__spec['profile'] = {}
            self.__spec['profile']['email'] = email

        super().__init__(name=name,
                         kind="User")
    
    @property
    def memberOf(self):
        return self.__spec['memberOf']

    @property
    def displayName(self): 
        return self.__spec['profile']['displayName']

    @property
    def email(self): 
        return self.__spec['profile']['email']

    @property
    def spec(self): 
        return self.__spec
    
# https://backstage.io/docs/features/software-catalog/descriptor-format#kind-group
class BackstageGroup(Backstage):
    def __init__(self,
                 name,
                 type,
                 parent=None,       # Optional field
                 apiversion=None,
                 children=[],
                 displayName=None,  # Optional field
                 email=None,        # Optional field
                 members=[],        # Optional field
    ):

        self.__spec             = {}
        self.__spec['type']     = type
        self.__spec['children'] = children

        if parent is not None:
            self.__spec['parent']  = parent

        if members != []:
            self.__spec['members'] = members

        if displayName is not None:
            if 'profile' not in self.__spec:
                self.__spec['profile'] = {}
            self.__spec['profile']['displayName'] = displayName

        if email is not None:
            if 'profile' not in self.__spec:
                self.__spec['profile'] = {}
            self.__spec['profile']['email'] = email


        super().__init__(name=name,
                         kind="Group")

    @property
    def type(self): 
        return self.__spec['type']

    @property
    def children(self): 
        return self.__spec['children']

    @property
    def displayName(self): 
        return self.__spec['profile']['displayName']

    @property
    def email(self): 
        return self.__spec['profile']['email']

    @property
    def members(self): 
        return self.__spec['members']

    @property
    def parent(self): 
        return self.__spec['parent']

    @property
    def spec(self): 
        return self.__spec
