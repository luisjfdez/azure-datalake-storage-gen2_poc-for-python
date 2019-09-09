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
from msrest.exceptions import HttpOperationError


class DataLakeStorageError(Model):
    """DataLakeStorageError.

    :param error: The service error response object.
    :type error: ~azure.mgmt.media.models.DataLakeStorageErrorError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'DataLakeStorageErrorError'},
    }

    def __init__(self, **kwargs):
        super(DataLakeStorageError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class DataLakeStorageErrorException(HttpOperationError):
    """Server responsed with exception of type: 'DataLakeStorageError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(DataLakeStorageErrorException, self).__init__(deserialize, response, 'DataLakeStorageError', *args)
