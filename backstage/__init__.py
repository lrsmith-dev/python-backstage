import os
import yaml

class Backstage:

    def __init__(self, kind, metadata, apiVersion=None ):

        # Check for mandatory, for all entities, in metadata
        if "name" not in metadata:
            raise ValueError("name not defined in metadata")

        self.__metadata = metadata
        self.__apiVersion = 'backstage.io/v1alpha1' if apiVersion is None else apiVersion
        self.__kind = kind

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

        return (f'apiVersion: {self.apiversion}\n'
                f'kind: {self.kind}\n' + 
                yaml.dump(tmp) 
                )

