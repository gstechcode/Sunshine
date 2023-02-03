# The PEP 484 type hints stub file for the QtPositioning module.
#
# Generated by SIP 6.5.1
#
# Copyright (c) 2022 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import enum
import typing

import PyQt6.sip

from PyQt6 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QGeoAddress(PyQt6.sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoAddress') -> None: ...

    def __hash__(self) -> int: ...
    def setStreetNumber(self, streetNumber: str) -> None: ...
    def streetNumber(self) -> str: ...
    def swap(self, other: 'QGeoAddress') -> None: ...
    def isTextGenerated(self) -> bool: ...
    def clear(self) -> None: ...
    def isEmpty(self) -> bool: ...
    def setStreet(self, street: str) -> None: ...
    def street(self) -> str: ...
    def setPostalCode(self, postalCode: str) -> None: ...
    def postalCode(self) -> str: ...
    def setDistrict(self, district: str) -> None: ...
    def district(self) -> str: ...
    def setCity(self, city: str) -> None: ...
    def city(self) -> str: ...
    def setCounty(self, county: str) -> None: ...
    def county(self) -> str: ...
    def setState(self, state: str) -> None: ...
    def state(self) -> str: ...
    def setCountryCode(self, countryCode: str) -> None: ...
    def countryCode(self) -> str: ...
    def setCountry(self, country: str) -> None: ...
    def country(self) -> str: ...
    def setText(self, text: str) -> None: ...
    def text(self) -> str: ...


class QGeoAreaMonitorInfo(PyQt6.sip.wrapper):

    @typing.overload
    def __init__(self, name: str = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoAreaMonitorInfo') -> None: ...

    def __hash__(self) -> int: ...
    def swap(self, other: 'QGeoAreaMonitorInfo') -> None: ...
    def setNotificationParameters(self, parameters: typing.Dict[str, typing.Any]) -> None: ...
    def notificationParameters(self) -> typing.Dict[str, typing.Any]: ...
    def setPersistent(self, isPersistent: bool) -> None: ...
    def isPersistent(self) -> bool: ...
    def setExpiration(self, expiry: typing.Union[QtCore.QDateTime, datetime.datetime]) -> None: ...
    def expiration(self) -> QtCore.QDateTime: ...
    def setArea(self, newShape: 'QGeoShape') -> None: ...
    def area(self) -> 'QGeoShape': ...
    def isValid(self) -> bool: ...
    def identifier(self) -> str: ...
    def setName(self, name: str) -> None: ...
    def name(self) -> str: ...


class QGeoAreaMonitorSource(QtCore.QObject):

    class AreaMonitorFeature(enum.Flag):
        PersistentAreaMonitorFeature = ... # type: QGeoAreaMonitorSource.AreaMonitorFeature
        AnyAreaMonitorFeature = ... # type: QGeoAreaMonitorSource.AreaMonitorFeature

    class Error(enum.Enum):
        AccessError = ... # type: QGeoAreaMonitorSource.Error
        InsufficientPositionInfo = ... # type: QGeoAreaMonitorSource.Error
        UnknownSourceError = ... # type: QGeoAreaMonitorSource.Error
        NoError = ... # type: QGeoAreaMonitorSource.Error

    def __init__(self, parent: QtCore.QObject) -> None: ...

    def backendProperty(self, name: str) -> typing.Any: ...
    def setBackendProperty(self, name: str, value: typing.Any) -> bool: ...
    def errorOccurred(self, error: 'QGeoAreaMonitorSource.Error') -> None: ...
    def monitorExpired(self, monitor: QGeoAreaMonitorInfo) -> None: ...
    def areaExited(self, monitor: QGeoAreaMonitorInfo, update: 'QGeoPositionInfo') -> None: ...
    def areaEntered(self, monitor: QGeoAreaMonitorInfo, update: 'QGeoPositionInfo') -> None: ...
    @typing.overload
    def activeMonitors(self) -> typing.List[QGeoAreaMonitorInfo]: ...
    @typing.overload
    def activeMonitors(self, lookupArea: 'QGeoShape') -> typing.List[QGeoAreaMonitorInfo]: ...
    def requestUpdate(self, monitor: QGeoAreaMonitorInfo, signal: str) -> bool: ...
    def stopMonitoring(self, monitor: QGeoAreaMonitorInfo) -> bool: ...
    def startMonitoring(self, monitor: QGeoAreaMonitorInfo) -> bool: ...
    def supportedAreaMonitorFeatures(self) -> 'QGeoAreaMonitorSource.AreaMonitorFeature': ...
    def error(self) -> 'QGeoAreaMonitorSource.Error': ...
    def sourceName(self) -> str: ...
    def positionInfoSource(self) -> 'QGeoPositionInfoSource': ...
    def setPositionInfoSource(self, source: 'QGeoPositionInfoSource') -> None: ...
    @staticmethod
    def availableSources() -> typing.List[str]: ...
    @staticmethod
    def createSource(sourceName: str, parent: QtCore.QObject) -> 'QGeoAreaMonitorSource': ...
    @staticmethod
    def createDefaultSource(parent: QtCore.QObject) -> 'QGeoAreaMonitorSource': ...


class QGeoShape(PyQt6.sip.wrapper):

    class ShapeType(enum.Enum):
        UnknownType = ... # type: QGeoShape.ShapeType
        RectangleType = ... # type: QGeoShape.ShapeType
        CircleType = ... # type: QGeoShape.ShapeType
        PathType = ... # type: QGeoShape.ShapeType
        PolygonType = ... # type: QGeoShape.ShapeType

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoShape') -> None: ...

    def __hash__(self) -> int: ...
    def boundingGeoRectangle(self) -> 'QGeoRectangle': ...
    def toString(self) -> str: ...
    def center(self) -> 'QGeoCoordinate': ...
    def contains(self, coordinate: 'QGeoCoordinate') -> bool: ...
    def isEmpty(self) -> bool: ...
    def isValid(self) -> bool: ...
    def type(self) -> 'QGeoShape.ShapeType': ...


class QGeoCircle(QGeoShape):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, center: 'QGeoCoordinate', radius: float = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoCircle') -> None: ...
    @typing.overload
    def __init__(self, other: QGeoShape) -> None: ...

    def extendCircle(self, coordinate: 'QGeoCoordinate') -> None: ...
    def toString(self) -> str: ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> 'QGeoCircle': ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...
    def radius(self) -> float: ...
    def setRadius(self, radius: float) -> None: ...
    def center(self) -> 'QGeoCoordinate': ...
    def setCenter(self, center: 'QGeoCoordinate') -> None: ...


class QGeoCoordinate(PyQt6.sip.wrapper):

    class CoordinateFormat(enum.Enum):
        Degrees = ... # type: QGeoCoordinate.CoordinateFormat
        DegreesWithHemisphere = ... # type: QGeoCoordinate.CoordinateFormat
        DegreesMinutes = ... # type: QGeoCoordinate.CoordinateFormat
        DegreesMinutesWithHemisphere = ... # type: QGeoCoordinate.CoordinateFormat
        DegreesMinutesSeconds = ... # type: QGeoCoordinate.CoordinateFormat
        DegreesMinutesSecondsWithHemisphere = ... # type: QGeoCoordinate.CoordinateFormat

    class CoordinateType(enum.Enum):
        InvalidCoordinate = ... # type: QGeoCoordinate.CoordinateType
        Coordinate2D = ... # type: QGeoCoordinate.CoordinateType
        Coordinate3D = ... # type: QGeoCoordinate.CoordinateType

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, latitude: float, longitude: float) -> None: ...
    @typing.overload
    def __init__(self, latitude: float, longitude: float, altitude: float) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoCoordinate') -> None: ...

    def __hash__(self) -> int: ...
    def swap(self, other: 'QGeoCoordinate') -> None: ...
    def toString(self, format: 'QGeoCoordinate.CoordinateFormat' = ...) -> str: ...
    def atDistanceAndAzimuth(self, distance: float, azimuth: float, distanceUp: float = ...) -> 'QGeoCoordinate': ...
    def azimuthTo(self, other: 'QGeoCoordinate') -> float: ...
    def distanceTo(self, other: 'QGeoCoordinate') -> float: ...
    def altitude(self) -> float: ...
    def setAltitude(self, altitude: float) -> None: ...
    def longitude(self) -> float: ...
    def setLongitude(self, longitude: float) -> None: ...
    def latitude(self) -> float: ...
    def setLatitude(self, latitude: float) -> None: ...
    def type(self) -> 'QGeoCoordinate.CoordinateType': ...
    def isValid(self) -> bool: ...


class QGeoLocation(PyQt6.sip.wrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoLocation') -> None: ...

    def __hash__(self) -> int: ...
    def setBoundingShape(self, shape: QGeoShape) -> None: ...
    def boundingShape(self) -> QGeoShape: ...
    def swap(self, other: 'QGeoLocation') -> None: ...
    def setExtendedAttributes(self, data: typing.Dict[str, typing.Any]) -> None: ...
    def extendedAttributes(self) -> typing.Dict[str, typing.Any]: ...
    def isEmpty(self) -> bool: ...
    def setCoordinate(self, position: QGeoCoordinate) -> None: ...
    def coordinate(self) -> QGeoCoordinate: ...
    def setAddress(self, address: QGeoAddress) -> None: ...
    def address(self) -> QGeoAddress: ...


class QGeoPath(QGeoShape):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, path: typing.Iterable[QGeoCoordinate], width: float = ...) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoPath') -> None: ...
    @typing.overload
    def __init__(self, other: QGeoShape) -> None: ...

    def clearPath(self) -> None: ...
    def size(self) -> int: ...
    def toString(self) -> str: ...
    @typing.overload
    def removeCoordinate(self, coordinate: QGeoCoordinate) -> None: ...
    @typing.overload
    def removeCoordinate(self, index: int) -> None: ...
    def containsCoordinate(self, coordinate: QGeoCoordinate) -> bool: ...
    def coordinateAt(self, index: int) -> QGeoCoordinate: ...
    def replaceCoordinate(self, index: int, coordinate: QGeoCoordinate) -> None: ...
    def insertCoordinate(self, index: int, coordinate: QGeoCoordinate) -> None: ...
    def addCoordinate(self, coordinate: QGeoCoordinate) -> None: ...
    def length(self, indexFrom: int = ..., indexTo: int = ...) -> float: ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> 'QGeoPath': ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...
    def width(self) -> float: ...
    def setWidth(self, width: float) -> None: ...
    def path(self) -> typing.List[QGeoCoordinate]: ...
    def setPath(self, path: typing.Iterable[QGeoCoordinate]) -> None: ...


class QGeoPolygon(QGeoShape):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, path: typing.Iterable[QGeoCoordinate]) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoPolygon') -> None: ...
    @typing.overload
    def __init__(self, other: QGeoShape) -> None: ...

    def perimeter(self) -> typing.List[QGeoCoordinate]: ...
    def setPerimeter(self, path: typing.Iterable[QGeoCoordinate]) -> None: ...
    def holesCount(self) -> int: ...
    def removeHole(self, index: int) -> None: ...
    def holePath(self, index: int) -> typing.List[QGeoCoordinate]: ...
    def hole(self, index: int) -> typing.List[typing.Any]: ...
    @typing.overload
    def addHole(self, holePath: typing.Iterable[QGeoCoordinate]) -> None: ...
    @typing.overload
    def addHole(self, holePath: typing.Any) -> None: ...
    def toString(self) -> str: ...
    @typing.overload
    def removeCoordinate(self, coordinate: QGeoCoordinate) -> None: ...
    @typing.overload
    def removeCoordinate(self, index: int) -> None: ...
    def containsCoordinate(self, coordinate: QGeoCoordinate) -> bool: ...
    def coordinateAt(self, index: int) -> QGeoCoordinate: ...
    def replaceCoordinate(self, index: int, coordinate: QGeoCoordinate) -> None: ...
    def insertCoordinate(self, index: int, coordinate: QGeoCoordinate) -> None: ...
    def addCoordinate(self, coordinate: QGeoCoordinate) -> None: ...
    def size(self) -> int: ...
    def length(self, indexFrom: int = ..., indexTo: int = ...) -> float: ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> 'QGeoPolygon': ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...


class QGeoPositionInfo(PyQt6.sip.wrapper):

    class Attribute(enum.Enum):
        Direction = ... # type: QGeoPositionInfo.Attribute
        GroundSpeed = ... # type: QGeoPositionInfo.Attribute
        VerticalSpeed = ... # type: QGeoPositionInfo.Attribute
        MagneticVariation = ... # type: QGeoPositionInfo.Attribute
        HorizontalAccuracy = ... # type: QGeoPositionInfo.Attribute
        VerticalAccuracy = ... # type: QGeoPositionInfo.Attribute

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, coordinate: QGeoCoordinate, updateTime: typing.Union[QtCore.QDateTime, datetime.datetime]) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoPositionInfo') -> None: ...

    def __hash__(self) -> int: ...
    def swap(self, other: 'QGeoPositionInfo') -> None: ...
    def hasAttribute(self, attribute: 'QGeoPositionInfo.Attribute') -> bool: ...
    def removeAttribute(self, attribute: 'QGeoPositionInfo.Attribute') -> None: ...
    def attribute(self, attribute: 'QGeoPositionInfo.Attribute') -> float: ...
    def setAttribute(self, attribute: 'QGeoPositionInfo.Attribute', value: float) -> None: ...
    def coordinate(self) -> QGeoCoordinate: ...
    def setCoordinate(self, coordinate: QGeoCoordinate) -> None: ...
    def timestamp(self) -> QtCore.QDateTime: ...
    def setTimestamp(self, timestamp: typing.Union[QtCore.QDateTime, datetime.datetime]) -> None: ...
    def isValid(self) -> bool: ...


class QGeoPositionInfoSource(QtCore.QObject):

    class PositioningMethod(enum.Flag):
        NoPositioningMethods = ... # type: QGeoPositionInfoSource.PositioningMethod
        SatellitePositioningMethods = ... # type: QGeoPositionInfoSource.PositioningMethod
        NonSatellitePositioningMethods = ... # type: QGeoPositionInfoSource.PositioningMethod
        AllPositioningMethods = ... # type: QGeoPositionInfoSource.PositioningMethod

    class Error(enum.Enum):
        AccessError = ... # type: QGeoPositionInfoSource.Error
        ClosedError = ... # type: QGeoPositionInfoSource.Error
        UnknownSourceError = ... # type: QGeoPositionInfoSource.Error
        UpdateTimeoutError = ... # type: QGeoPositionInfoSource.Error
        NoError = ... # type: QGeoPositionInfoSource.Error

    def __init__(self, parent: QtCore.QObject) -> None: ...

    def backendProperty(self, name: str) -> typing.Any: ...
    def setBackendProperty(self, name: str, value: typing.Any) -> bool: ...
    def errorOccurred(self, a0: 'QGeoPositionInfoSource.Error') -> None: ...
    def supportedPositioningMethodsChanged(self) -> None: ...
    def positionUpdated(self, update: QGeoPositionInfo) -> None: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def stopUpdates(self) -> None: ...
    def startUpdates(self) -> None: ...
    def error(self) -> 'QGeoPositionInfoSource.Error': ...
    @staticmethod
    def availableSources() -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def createSource(sourceName: str, parent: QtCore.QObject) -> 'QGeoPositionInfoSource': ...
    @typing.overload
    @staticmethod
    def createSource(sourceName: str, parameters: typing.Dict[str, typing.Any], parent: QtCore.QObject) -> 'QGeoPositionInfoSource': ...
    @typing.overload
    @staticmethod
    def createDefaultSource(parent: QtCore.QObject) -> 'QGeoPositionInfoSource': ...
    @typing.overload
    @staticmethod
    def createDefaultSource(parameters: typing.Dict[str, typing.Any], parent: QtCore.QObject) -> 'QGeoPositionInfoSource': ...
    def sourceName(self) -> str: ...
    def minimumUpdateInterval(self) -> int: ...
    def supportedPositioningMethods(self) -> 'QGeoPositionInfoSource.PositioningMethod': ...
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = ...) -> QGeoPositionInfo: ...
    def preferredPositioningMethods(self) -> 'QGeoPositionInfoSource.PositioningMethod': ...
    def setPreferredPositioningMethods(self, methods: 'QGeoPositionInfoSource.PositioningMethod') -> None: ...
    def updateInterval(self) -> int: ...
    def setUpdateInterval(self, msec: int) -> None: ...


class QGeoRectangle(QGeoShape):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, center: QGeoCoordinate, degreesWidth: float, degreesHeight: float) -> None: ...
    @typing.overload
    def __init__(self, topLeft: QGeoCoordinate, bottomRight: QGeoCoordinate) -> None: ...
    @typing.overload
    def __init__(self, coordinates: typing.Iterable[QGeoCoordinate]) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoRectangle') -> None: ...
    @typing.overload
    def __init__(self, other: QGeoShape) -> None: ...

    def extendRectangle(self, coordinate: QGeoCoordinate) -> None: ...
    def toString(self) -> str: ...
    def united(self, rectangle: 'QGeoRectangle') -> 'QGeoRectangle': ...
    def translated(self, degreesLatitude: float, degreesLongitude: float) -> 'QGeoRectangle': ...
    def translate(self, degreesLatitude: float, degreesLongitude: float) -> None: ...
    def intersects(self, rectangle: 'QGeoRectangle') -> bool: ...
    def contains(self, rectangle: 'QGeoRectangle') -> bool: ...
    def height(self) -> float: ...
    def setHeight(self, degreesHeight: float) -> None: ...
    def width(self) -> float: ...
    def setWidth(self, degreesWidth: float) -> None: ...
    def center(self) -> QGeoCoordinate: ...
    def setCenter(self, center: QGeoCoordinate) -> None: ...
    def bottomRight(self) -> QGeoCoordinate: ...
    def setBottomRight(self, bottomRight: QGeoCoordinate) -> None: ...
    def bottomLeft(self) -> QGeoCoordinate: ...
    def setBottomLeft(self, bottomLeft: QGeoCoordinate) -> None: ...
    def topRight(self) -> QGeoCoordinate: ...
    def setTopRight(self, topRight: QGeoCoordinate) -> None: ...
    def topLeft(self) -> QGeoCoordinate: ...
    def setTopLeft(self, topLeft: QGeoCoordinate) -> None: ...


class QGeoSatelliteInfo(PyQt6.sip.wrapper):

    class SatelliteSystem(enum.Enum):
        Undefined = ... # type: QGeoSatelliteInfo.SatelliteSystem
        GPS = ... # type: QGeoSatelliteInfo.SatelliteSystem
        GLONASS = ... # type: QGeoSatelliteInfo.SatelliteSystem
        GALILEO = ... # type: QGeoSatelliteInfo.SatelliteSystem
        BEIDOU = ... # type: QGeoSatelliteInfo.SatelliteSystem
        QZSS = ... # type: QGeoSatelliteInfo.SatelliteSystem
        Multiple = ... # type: QGeoSatelliteInfo.SatelliteSystem
        CustomType = ... # type: QGeoSatelliteInfo.SatelliteSystem

    class Attribute(enum.Enum):
        Elevation = ... # type: QGeoSatelliteInfo.Attribute
        Azimuth = ... # type: QGeoSatelliteInfo.Attribute

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QGeoSatelliteInfo') -> None: ...

    def __hash__(self) -> int: ...
    def swap(self, other: 'QGeoSatelliteInfo') -> None: ...
    def hasAttribute(self, attribute: 'QGeoSatelliteInfo.Attribute') -> bool: ...
    def removeAttribute(self, attribute: 'QGeoSatelliteInfo.Attribute') -> None: ...
    def attribute(self, attribute: 'QGeoSatelliteInfo.Attribute') -> float: ...
    def setAttribute(self, attribute: 'QGeoSatelliteInfo.Attribute', value: float) -> None: ...
    def signalStrength(self) -> int: ...
    def setSignalStrength(self, signalStrength: int) -> None: ...
    def satelliteIdentifier(self) -> int: ...
    def setSatelliteIdentifier(self, satId: int) -> None: ...
    def satelliteSystem(self) -> 'QGeoSatelliteInfo.SatelliteSystem': ...
    def setSatelliteSystem(self, system: 'QGeoSatelliteInfo.SatelliteSystem') -> None: ...


class QGeoSatelliteInfoSource(QtCore.QObject):

    class Error(enum.Enum):
        AccessError = ... # type: QGeoSatelliteInfoSource.Error
        ClosedError = ... # type: QGeoSatelliteInfoSource.Error
        NoError = ... # type: QGeoSatelliteInfoSource.Error
        UnknownSourceError = ... # type: QGeoSatelliteInfoSource.Error
        UpdateTimeoutError = ... # type: QGeoSatelliteInfoSource.Error

    def __init__(self, parent: QtCore.QObject) -> None: ...

    def backendProperty(self, name: str) -> typing.Any: ...
    def setBackendProperty(self, name: str, value: typing.Any) -> bool: ...
    def errorOccurred(self, a0: 'QGeoSatelliteInfoSource.Error') -> None: ...
    def satellitesInUseUpdated(self, satellites: typing.Iterable[QGeoSatelliteInfo]) -> None: ...
    def satellitesInViewUpdated(self, satellites: typing.Iterable[QGeoSatelliteInfo]) -> None: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def stopUpdates(self) -> None: ...
    def startUpdates(self) -> None: ...
    def error(self) -> 'QGeoSatelliteInfoSource.Error': ...
    def minimumUpdateInterval(self) -> int: ...
    def updateInterval(self) -> int: ...
    def setUpdateInterval(self, msec: int) -> None: ...
    def sourceName(self) -> str: ...
    @staticmethod
    def availableSources() -> typing.List[str]: ...
    @typing.overload
    @staticmethod
    def createSource(sourceName: str, parent: QtCore.QObject) -> 'QGeoSatelliteInfoSource': ...
    @typing.overload
    @staticmethod
    def createSource(sourceName: str, parameters: typing.Dict[str, typing.Any], parent: QtCore.QObject) -> 'QGeoSatelliteInfoSource': ...
    @typing.overload
    @staticmethod
    def createDefaultSource(parent: QtCore.QObject) -> 'QGeoSatelliteInfoSource': ...
    @typing.overload
    @staticmethod
    def createDefaultSource(parameters: typing.Dict[str, typing.Any], parent: QtCore.QObject) -> 'QGeoSatelliteInfoSource': ...


class QNmeaPositionInfoSource(QGeoPositionInfoSource):

    class UpdateMode(enum.Enum):
        RealTimeMode = ... # type: QNmeaPositionInfoSource.UpdateMode
        SimulationMode = ... # type: QNmeaPositionInfoSource.UpdateMode

    def __init__(self, updateMode: 'QNmeaPositionInfoSource.UpdateMode', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def userEquivalentRangeError(self) -> float: ...
    def setUserEquivalentRangeError(self, uere: float) -> None: ...
    def parsePosInfoFromNmeaData(self, data: bytes, size: int, posInfo: QGeoPositionInfo) -> typing.Tuple[bool, bool]: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def stopUpdates(self) -> None: ...
    def startUpdates(self) -> None: ...
    def error(self) -> QGeoPositionInfoSource.Error: ...
    def minimumUpdateInterval(self) -> int: ...
    def supportedPositioningMethods(self) -> QGeoPositionInfoSource.PositioningMethod: ...
    def lastKnownPosition(self, fromSatellitePositioningMethodsOnly: bool = ...) -> QGeoPositionInfo: ...
    def setUpdateInterval(self, msec: int) -> None: ...
    def device(self) -> QtCore.QIODevice: ...
    def setDevice(self, source: QtCore.QIODevice) -> None: ...
    def updateMode(self) -> 'QNmeaPositionInfoSource.UpdateMode': ...


class QNmeaSatelliteInfoSource(QGeoSatelliteInfoSource):

    class SatelliteInfoParseStatus(enum.Enum):
        NotParsed = ... # type: QNmeaSatelliteInfoSource.SatelliteInfoParseStatus
        PartiallyParsed = ... # type: QNmeaSatelliteInfoSource.SatelliteInfoParseStatus
        FullyParsed = ... # type: QNmeaSatelliteInfoSource.SatelliteInfoParseStatus

    class UpdateMode(enum.Enum):
        RealTimeMode = ... # type: QNmeaSatelliteInfoSource.UpdateMode
        SimulationMode = ... # type: QNmeaSatelliteInfoSource.UpdateMode

    SimulationUpdateInterval = ... # type: str

    def __init__(self, mode: 'QNmeaSatelliteInfoSource.UpdateMode', parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def parseSatelliteInfoFromNmea(self, data: bytes, size: int, infos: typing.Iterable[QGeoSatelliteInfo]) -> typing.Tuple['QNmeaSatelliteInfoSource.SatelliteInfoParseStatus', QGeoSatelliteInfo.SatelliteSystem]: ...
    def parseSatellitesInUseFromNmea(self, data: bytes, size: int, pnrsInUse: typing.Iterable[int]) -> QGeoSatelliteInfo.SatelliteSystem: ...
    def requestUpdate(self, timeout: int = ...) -> None: ...
    def stopUpdates(self) -> None: ...
    def startUpdates(self) -> None: ...
    def backendProperty(self, name: str) -> typing.Any: ...
    def setBackendProperty(self, name: str, value: typing.Any) -> bool: ...
    def error(self) -> QGeoSatelliteInfoSource.Error: ...
    def minimumUpdateInterval(self) -> int: ...
    def setUpdateInterval(self, msec: int) -> None: ...
    def device(self) -> QtCore.QIODevice: ...
    def setDevice(self, source: QtCore.QIODevice) -> None: ...
    def updateMode(self) -> 'QNmeaSatelliteInfoSource.UpdateMode': ...
