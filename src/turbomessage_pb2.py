# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/turbomessage.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16src/turbomessage.proto\x12\x0cturbomessage\"\x93\x01\n\rNew_User_Data\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tlast_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05\x65mail\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x15\n\x08password\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_nameB\x0c\n\n_last_nameB\x08\n\x06_emailB\x0b\n\t_password\"M\n\tUser_Data\x12\x12\n\x05\x65mail\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08password\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_emailB\x0b\n\t_password\"J\n\x06Status\x12\x13\n\x06status\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\t\n\x07_statusB\n\n\x08_message\"\xde\x01\n\nEmail_Data\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07subject\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04read\x18\x03 \x01(\x08H\x02\x88\x01\x01\x12\x14\n\x07\x64\x65leted\x18\x04 \x01(\x08H\x03\x88\x01\x01\x12\x19\n\x0c\x65mail_sender\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x1a\n\remail_reciver\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\x05\n\x03_idB\n\n\x08_subjectB\x07\n\x05_readB\n\n\x08_deletedB\x0f\n\r_email_senderB\x10\n\x0e_email_reciver\"\x1b\n\nUser_Email\x12\r\n\x05\x65mail\x18\x01 \x01(\t\":\n\x0e\x45mail_Response\x12(\n\x06\x65mails\x18\x01 \x03(\x0b\x32\x18.turbomessage.Email_Data2\x91\x01\n\rAuthenticator\x12?\n\x08new_user\x12\x1b.turbomessage.New_User_Data\x1a\x14.turbomessage.Status\"\x00\x12?\n\x0c\x61uthenticate\x12\x17.turbomessage.User_Data\x1a\x14.turbomessage.Status\"\x00\x32\xdc\x01\n\x0b\x45mailServer\x12>\n\nsend_email\x12\x18.turbomessage.Email_Data\x1a\x14.turbomessage.Status\"\x00\x12K\n\rrecive_emails\x12\x18.turbomessage.User_Email\x1a\x1c.turbomessage.Email_Response\"\x00\x30\x01\x12@\n\x0cmark_as_read\x12\x18.turbomessage.Email_Data\x1a\x14.turbomessage.Status\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.turbomessage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_NEW_USER_DATA']._serialized_start=41
  _globals['_NEW_USER_DATA']._serialized_end=188
  _globals['_USER_DATA']._serialized_start=190
  _globals['_USER_DATA']._serialized_end=267
  _globals['_STATUS']._serialized_start=269
  _globals['_STATUS']._serialized_end=343
  _globals['_EMAIL_DATA']._serialized_start=346
  _globals['_EMAIL_DATA']._serialized_end=568
  _globals['_USER_EMAIL']._serialized_start=570
  _globals['_USER_EMAIL']._serialized_end=597
  _globals['_EMAIL_RESPONSE']._serialized_start=599
  _globals['_EMAIL_RESPONSE']._serialized_end=657
  _globals['_AUTHENTICATOR']._serialized_start=660
  _globals['_AUTHENTICATOR']._serialized_end=805
  _globals['_EMAILSERVER']._serialized_start=808
  _globals['_EMAILSERVER']._serialized_end=1028
# @@protoc_insertion_point(module_scope)
