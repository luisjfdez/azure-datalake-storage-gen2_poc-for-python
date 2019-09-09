# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Path(Model):
    """Path.

    :param name:
    :type name: str
    :param is_directory:  Default value: False .
    :type is_directory: bool
    :param last_modified:
    :type last_modified: str
    :param e_tag:
    :type e_tag: str
    :param content_length:
    :type content_length: long
    :param owner:
    :type owner: str
    :param group:
    :type group: str
    :param permissions:
    :type permissions: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_directory': {'key': 'isDirectory', 'type': 'bool'},
        'last_modified': {'key': 'lastModified', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'content_length': {'key': 'contentLength', 'type': 'long'},
        'owner': {'key': 'owner', 'type': 'str'},
        'group': {'key': 'group', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Path, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.is_directory = kwargs.get('is_directory', False)
        self.last_modified = kwargs.get('last_modified', None)
        self.e_tag = kwargs.get('e_tag', None)
        self.content_length = kwargs.get('content_length', None)
        self.owner = kwargs.get('owner', None)
        self.group = kwargs.get('group', None)
        self.permissions = kwargs.get('permissions', None)