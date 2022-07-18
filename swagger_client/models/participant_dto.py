# coding: utf-8

"""
    Student-Management-System-API

    The Student-Management-System-API. <a href='http://147.172.178.30:8080/stmgmt/api-json'>JSON</a>  # noqa: E501

    OpenAPI spec version: 2.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ParticipantDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_id': 'str',
        'username': 'str',
        'display_name': 'str',
        'matr_nr': 'float',
        'email': 'str',
        'role': 'str',
        'group_id': 'str',
        'group': 'GroupDto'
    }

    attribute_map = {
        'user_id': 'userId',
        'username': 'username',
        'display_name': 'displayName',
        'matr_nr': 'matrNr',
        'email': 'email',
        'role': 'role',
        'group_id': 'groupId',
        'group': 'group'
    }

    def __init__(self, user_id=None, username=None, display_name=None, matr_nr=None, email=None, role=None, group_id=None, group=None):  # noqa: E501
        """ParticipantDto - a model defined in Swagger"""  # noqa: E501
        self._user_id = None
        self._username = None
        self._display_name = None
        self._matr_nr = None
        self._email = None
        self._role = None
        self._group_id = None
        self._group = None
        self.discriminator = None
        self.user_id = user_id
        self.username = username
        self.display_name = display_name
        if matr_nr is not None:
            self.matr_nr = matr_nr
        if email is not None:
            self.email = email
        self.role = role
        if group_id is not None:
            self.group_id = group_id
        if group is not None:
            self.group = group

    @property
    def user_id(self):
        """Gets the user_id of this ParticipantDto.  # noqa: E501


        :return: The user_id of this ParticipantDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ParticipantDto.


        :param user_id: The user_id of this ParticipantDto.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def username(self):
        """Gets the username of this ParticipantDto.  # noqa: E501


        :return: The username of this ParticipantDto.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ParticipantDto.


        :param username: The username of this ParticipantDto.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def display_name(self):
        """Gets the display_name of this ParticipantDto.  # noqa: E501


        :return: The display_name of this ParticipantDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ParticipantDto.


        :param display_name: The display_name of this ParticipantDto.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def matr_nr(self):
        """Gets the matr_nr of this ParticipantDto.  # noqa: E501


        :return: The matr_nr of this ParticipantDto.  # noqa: E501
        :rtype: float
        """
        return self._matr_nr

    @matr_nr.setter
    def matr_nr(self, matr_nr):
        """Sets the matr_nr of this ParticipantDto.


        :param matr_nr: The matr_nr of this ParticipantDto.  # noqa: E501
        :type: float
        """

        self._matr_nr = matr_nr

    @property
    def email(self):
        """Gets the email of this ParticipantDto.  # noqa: E501


        :return: The email of this ParticipantDto.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ParticipantDto.


        :param email: The email of this ParticipantDto.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def role(self):
        """Gets the role of this ParticipantDto.  # noqa: E501


        :return: The role of this ParticipantDto.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ParticipantDto.


        :param role: The role of this ParticipantDto.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["LECTURER", "TUTOR", "STUDENT"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def group_id(self):
        """Gets the group_id of this ParticipantDto.  # noqa: E501


        :return: The group_id of this ParticipantDto.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ParticipantDto.


        :param group_id: The group_id of this ParticipantDto.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def group(self):
        """Gets the group of this ParticipantDto.  # noqa: E501


        :return: The group of this ParticipantDto.  # noqa: E501
        :rtype: GroupDto
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ParticipantDto.


        :param group: The group of this ParticipantDto.  # noqa: E501
        :type: GroupDto
        """

        self._group = group

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ParticipantDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ParticipantDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
