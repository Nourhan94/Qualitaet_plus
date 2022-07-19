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

class AssignmentDto(object):
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
        'id': 'str',
        'name': 'str',
        'state': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'type': 'str',
        'collaboration': 'str',
        'points': 'float',
        'bonus_points': 'float',
        'comment': 'str',
        'configs': 'list[SubmissionConfigDto]',
        'links': 'list[LinkDto]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'type': 'type',
        'collaboration': 'collaboration',
        'points': 'points',
        'bonus_points': 'bonusPoints',
        'comment': 'comment',
        'configs': 'configs',
        'links': 'links'
    }

    def __init__(self, id=None, name=None, state=None, start_date=None, end_date=None, type=None, collaboration=None, points=None, bonus_points=None, comment=None, configs=None, links=None):  # noqa: E501
        """AssignmentDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._state = None
        self._start_date = None
        self._end_date = None
        self._type = None
        self._collaboration = None
        self._points = None
        self._bonus_points = None
        self._comment = None
        self._configs = None
        self._links = None
        self.discriminator = None
        self.id = id
        self.name = name
        self.state = state
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        self.type = type
        self.collaboration = collaboration
        self.points = points
        if bonus_points is not None:
            self.bonus_points = bonus_points
        if comment is not None:
            self.comment = comment
        if configs is not None:
            self.configs = configs
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this AssignmentDto.  # noqa: E501

        Unique identifier of this assignment.  # noqa: E501

        :return: The id of this AssignmentDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssignmentDto.

        Unique identifier of this assignment.  # noqa: E501

        :param id: The id of this AssignmentDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this AssignmentDto.  # noqa: E501

        The title of this assignment.  # noqa: E501

        :return: The name of this AssignmentDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssignmentDto.

        The title of this assignment.  # noqa: E501

        :param name: The name of this AssignmentDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def state(self):
        """Gets the state of this AssignmentDto.  # noqa: E501

        Determines, wether students can submit, assessments should be published, etc.  # noqa: E501

        :return: The state of this AssignmentDto.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AssignmentDto.

        Determines, wether students can submit, assessments should be published, etc.  # noqa: E501

        :param state: The state of this AssignmentDto.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["INVISIBLE", "CLOSED", "IN_PROGRESS", "IN_REVIEW", "EVALUATED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def start_date(self):
        """Gets the start_date of this AssignmentDto.  # noqa: E501

        Date at which this assignment should enter the IN_PROGRESS-state to allow submissions.  # noqa: E501

        :return: The start_date of this AssignmentDto.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this AssignmentDto.

        Date at which this assignment should enter the IN_PROGRESS-state to allow submissions.  # noqa: E501

        :param start_date: The start_date of this AssignmentDto.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this AssignmentDto.  # noqa: E501

        Date at which this assignment should enter the IN_REVIEW-state to disable submissions.  # noqa: E501

        :return: The end_date of this AssignmentDto.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this AssignmentDto.

        Date at which this assignment should enter the IN_REVIEW-state to disable submissions.  # noqa: E501

        :param end_date: The end_date of this AssignmentDto.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def type(self):
        """Gets the type of this AssignmentDto.  # noqa: E501

        The type of assignment, i.e homework or project.  # noqa: E501

        :return: The type of this AssignmentDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AssignmentDto.

        The type of assignment, i.e homework or project.  # noqa: E501

        :param type: The type of this AssignmentDto.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["HOMEWORK", "TESTAT", "SEMINAR", "PROJECT", "OTHER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def collaboration(self):
        """Gets the collaboration of this AssignmentDto.  # noqa: E501

        Determines, wether students can submit their solutions in groups, alone or both.  # noqa: E501

        :return: The collaboration of this AssignmentDto.  # noqa: E501
        :rtype: str
        """
        return self._collaboration

    @collaboration.setter
    def collaboration(self, collaboration):
        """Sets the collaboration of this AssignmentDto.

        Determines, wether students can submit their solutions in groups, alone or both.  # noqa: E501

        :param collaboration: The collaboration of this AssignmentDto.  # noqa: E501
        :type: str
        """
        if collaboration is None:
            raise ValueError("Invalid value for `collaboration`, must not be `None`")  # noqa: E501
        allowed_values = ["GROUP", "SINGLE", "GROUP_OR_SINGLE"]  # noqa: E501
        if collaboration not in allowed_values:
            raise ValueError(
                "Invalid value for `collaboration` ({0}), must be one of {1}"  # noqa: E501
                .format(collaboration, allowed_values)
            )

        self._collaboration = collaboration

    @property
    def points(self):
        """Gets the points of this AssignmentDto.  # noqa: E501

        The amount of points that can be reached by a participant (excluding bonus points).  # noqa: E501

        :return: The points of this AssignmentDto.  # noqa: E501
        :rtype: float
        """
        return self._points

    @points.setter
    def points(self, points):
        """Sets the points of this AssignmentDto.

        The amount of points that can be reached by a participant (excluding bonus points).  # noqa: E501

        :param points: The points of this AssignmentDto.  # noqa: E501
        :type: float
        """
        if points is None:
            raise ValueError("Invalid value for `points`, must not be `None`")  # noqa: E501

        self._points = points

    @property
    def bonus_points(self):
        """Gets the bonus_points of this AssignmentDto.  # noqa: E501

        The amount of additional bonus points, which should be excluded from the admission criteria.  # noqa: E501

        :return: The bonus_points of this AssignmentDto.  # noqa: E501
        :rtype: float
        """
        return self._bonus_points

    @bonus_points.setter
    def bonus_points(self, bonus_points):
        """Sets the bonus_points of this AssignmentDto.

        The amount of additional bonus points, which should be excluded from the admission criteria.  # noqa: E501

        :param bonus_points: The bonus_points of this AssignmentDto.  # noqa: E501
        :type: float
        """

        self._bonus_points = bonus_points

    @property
    def comment(self):
        """Gets the comment of this AssignmentDto.  # noqa: E501

        Additional information or description of this assignment.  # noqa: E501

        :return: The comment of this AssignmentDto.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AssignmentDto.

        Additional information or description of this assignment.  # noqa: E501

        :param comment: The comment of this AssignmentDto.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def configs(self):
        """Gets the configs of this AssignmentDto.  # noqa: E501

        Optional information to allow the configuration of connected submission tools.  # noqa: E501

        :return: The configs of this AssignmentDto.  # noqa: E501
        :rtype: list[SubmissionConfigDto]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this AssignmentDto.

        Optional information to allow the configuration of connected submission tools.  # noqa: E501

        :param configs: The configs of this AssignmentDto.  # noqa: E501
        :type: list[SubmissionConfigDto]
        """

        self._configs = configs

    @property
    def links(self):
        """Gets the links of this AssignmentDto.  # noqa: E501


        :return: The links of this AssignmentDto.  # noqa: E501
        :rtype: list[LinkDto]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AssignmentDto.


        :param links: The links of this AssignmentDto.  # noqa: E501
        :type: list[LinkDto]
        """

        self._links = links

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
        if issubclass(AssignmentDto, dict):
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
        if not isinstance(other, AssignmentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other