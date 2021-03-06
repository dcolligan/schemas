# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/schemas/ga4gh/sequence_annotations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh.schemas.ga4gh import common_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/schemas/ga4gh/sequence_annotations.proto',
  package='ga4gh.schemas.ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n.ga4gh/schemas/ga4gh/sequence_annotations.proto\x12\x13ga4gh.schemas.ga4gh\x1a ga4gh/schemas/ga4gh/common.proto\"\xc5\x02\n\x07\x46\x65\x61ture\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bgene_symbol\x18\x03 \x01(\t\x12\x11\n\tparent_id\x18\x04 \x01(\t\x12\x11\n\tchild_ids\x18\x05 \x03(\t\x12\x16\n\x0e\x66\x65\x61ture_set_id\x18\x06 \x01(\t\x12\x16\n\x0ereference_name\x18\x07 \x01(\t\x12\r\n\x05start\x18\x08 \x01(\x03\x12\x0b\n\x03\x65nd\x18\t \x01(\x03\x12+\n\x06strand\x18\n \x01(\x0e\x32\x1b.ga4gh.schemas.ga4gh.Strand\x12\x37\n\x0c\x66\x65\x61ture_type\x18\x0b \x01(\x0b\x32!.ga4gh.schemas.ga4gh.OntologyTerm\x12\x33\n\nattributes\x18\x0c \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\"\x9d\x01\n\nFeatureSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x18\n\x10reference_set_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nsource_uri\x18\x05 \x01(\t\x12\x33\n\nattributes\x18\x0c \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\"^\n\nContinuous\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0e\n\x06values\x18\x02 \x03(\x01\x12\x19\n\x11\x63ontinuous_set_id\x18\x03 \x01(\t\x12\x16\n\x0ereference_name\x18\x04 \x01(\t\"\xa0\x01\n\rContinuousSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x18\n\x10reference_set_id\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\nsource_uri\x18\x05 \x01(\t\x12\x33\n\nattributes\x18\x0c \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributesb\x06proto3')
  ,
  dependencies=[ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='ga4gh.schemas.ga4gh.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.Feature.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.Feature.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gene_symbol', full_name='ga4gh.schemas.ga4gh.Feature.gene_symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent_id', full_name='ga4gh.schemas.ga4gh.Feature.parent_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='child_ids', full_name='ga4gh.schemas.ga4gh.Feature.child_ids', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_set_id', full_name='ga4gh.schemas.ga4gh.Feature.feature_set_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='ga4gh.schemas.ga4gh.Feature.reference_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh.schemas.ga4gh.Feature.start', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='ga4gh.schemas.ga4gh.Feature.end', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strand', full_name='ga4gh.schemas.ga4gh.Feature.strand', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature_type', full_name='ga4gh.schemas.ga4gh.Feature.feature_type', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.Feature.attributes', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=431,
)


_FEATURESET = _descriptor.Descriptor(
  name='FeatureSet',
  full_name='ga4gh.schemas.ga4gh.FeatureSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.FeatureSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.schemas.ga4gh.FeatureSet.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='ga4gh.schemas.ga4gh.FeatureSet.reference_set_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.FeatureSet.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_uri', full_name='ga4gh.schemas.ga4gh.FeatureSet.source_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.FeatureSet.attributes', index=5,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=591,
)


_CONTINUOUS = _descriptor.Descriptor(
  name='Continuous',
  full_name='ga4gh.schemas.ga4gh.Continuous',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='ga4gh.schemas.ga4gh.Continuous.start', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='ga4gh.schemas.ga4gh.Continuous.values', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='continuous_set_id', full_name='ga4gh.schemas.ga4gh.Continuous.continuous_set_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_name', full_name='ga4gh.schemas.ga4gh.Continuous.reference_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=593,
  serialized_end=687,
)


_CONTINUOUSSET = _descriptor.Descriptor(
  name='ContinuousSet',
  full_name='ga4gh.schemas.ga4gh.ContinuousSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.ContinuousSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.schemas.ga4gh.ContinuousSet.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='ga4gh.schemas.ga4gh.ContinuousSet.reference_set_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.ContinuousSet.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_uri', full_name='ga4gh.schemas.ga4gh.ContinuousSet.source_uri', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.ContinuousSet.attributes', index=5,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=690,
  serialized_end=850,
)

_FEATURE.fields_by_name['strand'].enum_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._STRAND
_FEATURE.fields_by_name['feature_type'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ONTOLOGYTERM
_FEATURE.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
_FEATURESET.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
_CONTINUOUSSET.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['FeatureSet'] = _FEATURESET
DESCRIPTOR.message_types_by_name['Continuous'] = _CONTINUOUS
DESCRIPTOR.message_types_by_name['ContinuousSet'] = _CONTINUOUSSET

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'ga4gh.schemas.ga4gh.sequence_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Feature)
  ))
_sym_db.RegisterMessage(Feature)

FeatureSet = _reflection.GeneratedProtocolMessageType('FeatureSet', (_message.Message,), dict(
  DESCRIPTOR = _FEATURESET,
  __module__ = 'ga4gh.schemas.ga4gh.sequence_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.FeatureSet)
  ))
_sym_db.RegisterMessage(FeatureSet)

Continuous = _reflection.GeneratedProtocolMessageType('Continuous', (_message.Message,), dict(
  DESCRIPTOR = _CONTINUOUS,
  __module__ = 'ga4gh.schemas.ga4gh.sequence_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.Continuous)
  ))
_sym_db.RegisterMessage(Continuous)

ContinuousSet = _reflection.GeneratedProtocolMessageType('ContinuousSet', (_message.Message,), dict(
  DESCRIPTOR = _CONTINUOUSSET,
  __module__ = 'ga4gh.schemas.ga4gh.sequence_annotations_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.ContinuousSet)
  ))
_sym_db.RegisterMessage(ContinuousSet)


# @@protoc_insertion_point(module_scope)
