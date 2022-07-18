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

class CourseAboutDto(object):
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
        'course': 'CourseDto',
        'participants_count': 'float',
        'teaching_staff': 'list[ParticipantDto]'
    }

    attribute_map = {
        'course': 'course',
        'participants_count': 'participantsCount',
        'teaching_staff': 'teachingStaff'
    }

    def __init__(self, course=None, participants_count=None, teaching_staff=None):  # noqa: E501
        """CourseAboutDto - a model defined in Swagger"""  # noqa: E501
        self._course = None
        self._participants_count = None
        self._teaching_staff = None
        self.discriminator = None
        self.course = course
        self.participants_count = participants_count
        self.teaching_staff = teaching_staff

    @property
    def course(self):
        """Gets the course of this CourseAboutDto.  # noqa: E501


        :return: The course of this CourseAboutDto.  # noqa: E501
        :rtype: CourseDto
        """
        return self._course

    @course.setter
    def course(self, course):
        """Sets the course of this CourseAboutDto.


        :param course: The course of this CourseAboutDto.  # noqa: E501
        :type: CourseDto
        """
        if course is None:
            raise ValueError("Invalid value for `course`, must not be `None`")  # noqa: E501

        self._course = course

    @property
    def participants_count(self):
        """Gets the participants_count of this CourseAboutDto.  # noqa: E501


        :return: The participants_count of this CourseAboutDto.  # noqa: E501
        :rtype: float
        """
        return self._participants_count

    @participants_count.setter
    def participants_count(self, participants_count):
        """Sets the participants_count of this CourseAboutDto.


        :param participants_count: The participants_count of this CourseAboutDto.  # noqa: E501
        :type: float
        """
        if participants_count is None:
            raise ValueError("Invalid value for `participants_count`, must not be `None`")  # noqa: E501

        self._participants_count = participants_count

    @property
    def teaching_staff(self):
        """Gets the teaching_staff of this CourseAboutDto.  # noqa: E501


        :return: The teaching_staff of this CourseAboutDto.  # noqa: E501
        :rtype: list[ParticipantDto]
        """
        return self._teaching_staff

    @teaching_staff.setter
    def teaching_staff(self, teaching_staff):
        """Sets the teaching_staff of this CourseAboutDto.


        :param teaching_staff: The teaching_staff of this CourseAboutDto.  # noqa: E501
        :type: list[ParticipantDto]
        """
        if teaching_staff is None:
            raise ValueError("Invalid value for `teaching_staff`, must not be `None`")  # noqa: E501

        self._teaching_staff = teaching_staff

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
        if issubclass(CourseAboutDto, dict):
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
        if not isinstance(other, CourseAboutDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
