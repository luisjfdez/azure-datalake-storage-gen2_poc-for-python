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


class Filesystem(Model):
    """Filesystem.

    :param name:
    :type name: str
    :param last_modified:
    :type last_modified: str
    :param e_tag:
    :type e_tag: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, last_modified: str=None, e_tag: str=None, **kwargs) -> None:
        super(Filesystem, self).__init__(**kwargs)
        self.name = name
        self.last_modified = last_modified
        self.e_tag = e_tag
