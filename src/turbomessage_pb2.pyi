from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class New_User_Data(_message.Message):
    __slots__ = ("name", "last_name", "email", "password")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    last_name: str
    email: str
    password: str
    def __init__(self, name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class User_Data(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: bool
    message: str
    def __init__(self, status: bool = ..., message: _Optional[str] = ...) -> None: ...

class Email_Data(_message.Message):
    __slots__ = ("id", "subject", "read", "deleted", "email_sender", "email_reciver")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    EMAIL_SENDER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_RECIVER_FIELD_NUMBER: _ClassVar[int]
    id: int
    subject: str
    read: bool
    deleted: bool
    email_sender: str
    email_reciver: str
    def __init__(self, id: _Optional[int] = ..., subject: _Optional[str] = ..., read: bool = ..., deleted: bool = ..., email_sender: _Optional[str] = ..., email_reciver: _Optional[str] = ...) -> None: ...

class User_Email(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class Email_Response(_message.Message):
    __slots__ = ("emails",)
    EMAILS_FIELD_NUMBER: _ClassVar[int]
    emails: _containers.RepeatedCompositeFieldContainer[Email_Data]
    def __init__(self, emails: _Optional[_Iterable[_Union[Email_Data, _Mapping]]] = ...) -> None: ...
