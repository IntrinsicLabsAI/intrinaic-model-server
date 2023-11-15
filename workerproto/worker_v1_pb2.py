# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: worker_v1.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fworker_v1.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"G\n\x10HeartbeatRequest\x12\x11\n\tworker_id\x18\x01 \x01(\t\x12 \n\x0esupported_jobs\x18\x02 \x03(\x0e\x32\x08.JobType\"7\n\x0eHeartbeatReply\x12%\n\x0e\x61ssigned_tasks\x18\x01 \x03(\x0b\x32\r.AssignedTask\"\x9d\x01\n\x0c\x46ineTuneTask\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x18\n\x10pytorch_hf_model\x18\x03 \x01(\t\x12+\n\x12training_data_file\x18\x04 \x01(\x0b\x32\r.InMemoryFileH\x00\x12\'\n\x0e\x66ile_data_path\x18\x05 \x01(\x0b\x32\r.FileDataPathH\x00\x42\x0f\n\rtraining_data\".\n\x0cInMemoryFile\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x1c\n\x0c\x46ileDataPath\x12\x0c\n\x04path\x18\x01 \x01(\t\"9\n\x0c\x41ssignedTask\x12!\n\x08\x66inetune\x18\x01 \x01(\x0b\x32\r.FineTuneTaskH\x00\x42\x06\n\x04task\"\x0c\n\nOutputFile\"M\n\x17WriteOutputChunkRequest\x12\x11\n\ttask_uuid\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\r\n\x05\x63hunk\x18\x03 \x01(\x0c\".\n\x15WriteOutputChunkReply\x12\x15\n\rbytes_written\x18\x01 \x01(\r\"u\n\x12\x43ompleteJobRequest\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12#\n\x10\x63ompletion_state\x18\x02 \x01(\x0e\x32\t.JobState\x12\x1a\n\rfailed_reason\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x10\n\x0e_failed_reason\"(\n\x10\x43ompleteJobReply\x12\x14\n\x0coutput_files\x18\x01 \x03(\t*\x17\n\x07JobType\x12\x0c\n\x08\x46INETUNE\x10\x00*L\n\x08JobState\x12\n\n\x06QUEUED\x10\x00\x12\r\n\tSCHEDULED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0c\n\x08\x43OMPLETE\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x32\xca\x01\n\x14WorkerManagerService\x12\x31\n\tHeartbeat\x12\x11.HeartbeatRequest\x1a\x0f.HeartbeatReply\"\x00\x12\x46\n\x10WriteOutputChunk\x12\x18.WriteOutputChunkRequest\x1a\x16.WriteOutputChunkReply\"\x00\x12\x37\n\x0b\x43ompleteJob\x12\x13.CompleteJobRequest\x1a\x11.CompleteJobReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'worker_v1_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_JOBTYPE']._serialized_start=781
  _globals['_JOBTYPE']._serialized_end=804
  _globals['_JOBSTATE']._serialized_start=806
  _globals['_JOBSTATE']._serialized_end=882
  _globals['_HEARTBEATREQUEST']._serialized_start=52
  _globals['_HEARTBEATREQUEST']._serialized_end=123
  _globals['_HEARTBEATREPLY']._serialized_start=125
  _globals['_HEARTBEATREPLY']._serialized_end=180
  _globals['_FINETUNETASK']._serialized_start=183
  _globals['_FINETUNETASK']._serialized_end=340
  _globals['_INMEMORYFILE']._serialized_start=342
  _globals['_INMEMORYFILE']._serialized_end=388
  _globals['_FILEDATAPATH']._serialized_start=390
  _globals['_FILEDATAPATH']._serialized_end=418
  _globals['_ASSIGNEDTASK']._serialized_start=420
  _globals['_ASSIGNEDTASK']._serialized_end=477
  _globals['_OUTPUTFILE']._serialized_start=479
  _globals['_OUTPUTFILE']._serialized_end=491
  _globals['_WRITEOUTPUTCHUNKREQUEST']._serialized_start=493
  _globals['_WRITEOUTPUTCHUNKREQUEST']._serialized_end=570
  _globals['_WRITEOUTPUTCHUNKREPLY']._serialized_start=572
  _globals['_WRITEOUTPUTCHUNKREPLY']._serialized_end=618
  _globals['_COMPLETEJOBREQUEST']._serialized_start=620
  _globals['_COMPLETEJOBREQUEST']._serialized_end=737
  _globals['_COMPLETEJOBREPLY']._serialized_start=739
  _globals['_COMPLETEJOBREPLY']._serialized_end=779
  _globals['_WORKERMANAGERSERVICE']._serialized_start=885
  _globals['_WORKERMANAGERSERVICE']._serialized_end=1087
# @@protoc_insertion_point(module_scope)
