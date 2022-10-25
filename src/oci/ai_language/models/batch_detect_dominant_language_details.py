# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BatchDetectDominantLanguageDetails(object):
    """
    The documents details for language detect call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BatchDetectDominantLanguageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this BatchDetectDominantLanguageDetails.
        :type compartment_id: str

        :param documents:
            The value to assign to the documents property of this BatchDetectDominantLanguageDetails.
        :type documents: list[oci.ai_language.models.DominantLanguageDocument]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'documents': 'list[DominantLanguageDocument]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'documents': 'documents'
        }

        self._compartment_id = None
        self._documents = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this BatchDetectDominantLanguageDetails.
        The `OCID`__ of the compartment that calls the API, inference will be served from pre trained model

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this BatchDetectDominantLanguageDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BatchDetectDominantLanguageDetails.
        The `OCID`__ of the compartment that calls the API, inference will be served from pre trained model

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this BatchDetectDominantLanguageDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def documents(self):
        """
        **[Required]** Gets the documents of this BatchDetectDominantLanguageDetails.
        List of Documents for detect language.


        :return: The documents of this BatchDetectDominantLanguageDetails.
        :rtype: list[oci.ai_language.models.DominantLanguageDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """
        Sets the documents of this BatchDetectDominantLanguageDetails.
        List of Documents for detect language.


        :param documents: The documents of this BatchDetectDominantLanguageDetails.
        :type: list[oci.ai_language.models.DominantLanguageDocument]
        """
        self._documents = documents

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
