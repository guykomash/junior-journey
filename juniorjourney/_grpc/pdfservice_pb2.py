# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pdfservice.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10pdfservice.proto\x12\npdfservice\"\x1d\n\nPdfRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\".\n\x03URL\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\")\n\x08PdfReply\x12\x1d\n\x04urls\x18\x01 \x03(\x0b\x32\x0f.pdfservice.URL2O\n\nPdfService\x12\x41\n\x0fGetPdfsByUserID\x12\x16.pdfservice.PdfRequest\x1a\x14.pdfservice.PdfReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pdfservice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PDFREQUEST']._serialized_start=32
  _globals['_PDFREQUEST']._serialized_end=61
  _globals['_URL']._serialized_start=63
  _globals['_URL']._serialized_end=109
  _globals['_PDFREPLY']._serialized_start=111
  _globals['_PDFREPLY']._serialized_end=152
  _globals['_PDFSERVICE']._serialized_start=154
  _globals['_PDFSERVICE']._serialized_end=233
# @@protoc_insertion_point(module_scope)
