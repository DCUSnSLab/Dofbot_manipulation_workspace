# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from zed_interfaces/Object.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import zed_interfaces.msg

class Object(genpy.Message):
  _md5sum = "850ee8ff1282c46cfce0a7d14dd04611"
  _type = "zed_interfaces/Object"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Object label
string label

# Object label ID
int16 label_id

# Object instance ID
int16 instance_id

# Object sub
string sublabel

# Object confidence level (1-99)
float32 confidence

# Object centroid position
float32[3] position

# Position covariance
float32[6] position_covariance

# Object velocity
float32[3] velocity

# Tracking available
bool tracking_available

# Tracking state
# 0 -> OFF (object not valid)
# 1 -> OK
# 2 -> SEARCHING (occlusion occurred, trajectory is estimated)
int8 tracking_state

# Action state
# 0 -> IDLE
# 2 -> MOVING
int8 action_state

# 2D Bounding box projected to Camera image
zed_interfaces/BoundingBox2Di bounding_box_2d

# 3D Bounding box in world frame
zed_interfaces/BoundingBox3D bounding_box_3d

# 3D dimensions (width, height, lenght)
float32[3] dimensions_3d

# Is skeleton available?
bool skeleton_available

# 2D Bounding box projected to Camera image of the person head
zed_interfaces/BoundingBox2Df head_bounding_box_2d

# 3D Bounding box in world frame of the person head
zed_interfaces/BoundingBox3D head_bounding_box_3d

# 3D position of the centroid of the person head
float32[3] head_position

# 2D Person skeleton projected to Camera image
zed_interfaces/Skeleton2D skeleton_2d

# 3D Person skeleton in world frame
zed_interfaces/Skeleton3D skeleton_3d

================================================================================
MSG: zed_interfaces/BoundingBox2Di
#      0 ------- 1
#      |         |
#      |         |
#      |         |
#      3 ------- 2
zed_interfaces/Keypoint2Di[4] corners

================================================================================
MSG: zed_interfaces/Keypoint2Di
uint32[2] kp

================================================================================
MSG: zed_interfaces/BoundingBox3D
#      1 ------- 2
#     /.        /|
#    0 ------- 3 |
#    | .       | |
#    | 5.......| 6
#    |.        |/
#    4 ------- 7
zed_interfaces/Keypoint3D[8] corners

================================================================================
MSG: zed_interfaces/Keypoint3D
float32[3] kp

================================================================================
MSG: zed_interfaces/BoundingBox2Df
#      0 ------- 1
#      |         |
#      |         |
#      |         |
#      3 ------- 2
zed_interfaces/Keypoint2Df[4] corners

================================================================================
MSG: zed_interfaces/Keypoint2Df
float32[2] kp

================================================================================
MSG: zed_interfaces/Skeleton2D
# Skeleton joints indices
#        16-14   15-17
#             \ /
#              0
#              |
#       2------1------5
#       |    |   |    |
#	    |    |   |    |
#       3    |   |    6
#       |    |   |    |
#       |    |   |    |
#       4    8   11   7
#            |   |
#            |   |
#            |   |
#            9   12
#            |   |
#            |   |
#            |   |
#           10   13
zed_interfaces/Keypoint2Df[18] keypoints

================================================================================
MSG: zed_interfaces/Skeleton3D
# Skeleton joints indices
#        16-14   15-17
#             \ /
#              0
#              |
#       2------1------5
#       |    |   |    |
#	    |    |   |    |
#       3    |   |    6
#       |    |   |    |
#       |    |   |    |
#       4    8   11   7
#            |   |
#            |   |
#            |   |
#            9   12
#            |   |
#            |   |
#            |   |
#           10   13
zed_interfaces/Keypoint3D[18] keypoints
"""
  __slots__ = ['label','label_id','instance_id','sublabel','confidence','position','position_covariance','velocity','tracking_available','tracking_state','action_state','bounding_box_2d','bounding_box_3d','dimensions_3d','skeleton_available','head_bounding_box_2d','head_bounding_box_3d','head_position','skeleton_2d','skeleton_3d']
  _slot_types = ['string','int16','int16','string','float32','float32[3]','float32[6]','float32[3]','bool','int8','int8','zed_interfaces/BoundingBox2Di','zed_interfaces/BoundingBox3D','float32[3]','bool','zed_interfaces/BoundingBox2Df','zed_interfaces/BoundingBox3D','float32[3]','zed_interfaces/Skeleton2D','zed_interfaces/Skeleton3D']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       label,label_id,instance_id,sublabel,confidence,position,position_covariance,velocity,tracking_available,tracking_state,action_state,bounding_box_2d,bounding_box_3d,dimensions_3d,skeleton_available,head_bounding_box_2d,head_bounding_box_3d,head_position,skeleton_2d,skeleton_3d

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Object, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.label is None:
        self.label = ''
      if self.label_id is None:
        self.label_id = 0
      if self.instance_id is None:
        self.instance_id = 0
      if self.sublabel is None:
        self.sublabel = ''
      if self.confidence is None:
        self.confidence = 0.
      if self.position is None:
        self.position = [0.] * 3
      if self.position_covariance is None:
        self.position_covariance = [0.] * 6
      if self.velocity is None:
        self.velocity = [0.] * 3
      if self.tracking_available is None:
        self.tracking_available = False
      if self.tracking_state is None:
        self.tracking_state = 0
      if self.action_state is None:
        self.action_state = 0
      if self.bounding_box_2d is None:
        self.bounding_box_2d = zed_interfaces.msg.BoundingBox2Di()
      if self.bounding_box_3d is None:
        self.bounding_box_3d = zed_interfaces.msg.BoundingBox3D()
      if self.dimensions_3d is None:
        self.dimensions_3d = [0.] * 3
      if self.skeleton_available is None:
        self.skeleton_available = False
      if self.head_bounding_box_2d is None:
        self.head_bounding_box_2d = zed_interfaces.msg.BoundingBox2Df()
      if self.head_bounding_box_3d is None:
        self.head_bounding_box_3d = zed_interfaces.msg.BoundingBox3D()
      if self.head_position is None:
        self.head_position = [0.] * 3
      if self.skeleton_2d is None:
        self.skeleton_2d = zed_interfaces.msg.Skeleton2D()
      if self.skeleton_3d is None:
        self.skeleton_3d = zed_interfaces.msg.Skeleton3D()
    else:
      self.label = ''
      self.label_id = 0
      self.instance_id = 0
      self.sublabel = ''
      self.confidence = 0.
      self.position = [0.] * 3
      self.position_covariance = [0.] * 6
      self.velocity = [0.] * 3
      self.tracking_available = False
      self.tracking_state = 0
      self.action_state = 0
      self.bounding_box_2d = zed_interfaces.msg.BoundingBox2Di()
      self.bounding_box_3d = zed_interfaces.msg.BoundingBox3D()
      self.dimensions_3d = [0.] * 3
      self.skeleton_available = False
      self.head_bounding_box_2d = zed_interfaces.msg.BoundingBox2Df()
      self.head_bounding_box_3d = zed_interfaces.msg.BoundingBox3D()
      self.head_position = [0.] * 3
      self.skeleton_2d = zed_interfaces.msg.Skeleton2D()
      self.skeleton_3d = zed_interfaces.msg.Skeleton3D()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.label
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2h().pack(_x.label_id, _x.instance_id))
      _x = self.sublabel
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.confidence
      buff.write(_get_struct_f().pack(_x))
      buff.write(_get_struct_3f().pack(*self.position))
      buff.write(_get_struct_6f().pack(*self.position_covariance))
      buff.write(_get_struct_3f().pack(*self.velocity))
      _x = self
      buff.write(_get_struct_B2b().pack(_x.tracking_available, _x.tracking_state, _x.action_state))
      if len(self.bounding_box_2d.corners) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.bounding_box_2d.corners), 'self.bounding_box_2d.corners')))
      for val1 in self.bounding_box_2d.corners:
        buff.write(_get_struct_2I().pack(*val1.kp))
      if len(self.bounding_box_3d.corners) != 8:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (8, len(self.bounding_box_3d.corners), 'self.bounding_box_3d.corners')))
      for val1 in self.bounding_box_3d.corners:
        buff.write(_get_struct_3f().pack(*val1.kp))
      buff.write(_get_struct_3f().pack(*self.dimensions_3d))
      _x = self.skeleton_available
      buff.write(_get_struct_B().pack(_x))
      if len(self.head_bounding_box_2d.corners) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.head_bounding_box_2d.corners), 'self.head_bounding_box_2d.corners')))
      for val1 in self.head_bounding_box_2d.corners:
        buff.write(_get_struct_2f().pack(*val1.kp))
      if len(self.head_bounding_box_3d.corners) != 8:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (8, len(self.head_bounding_box_3d.corners), 'self.head_bounding_box_3d.corners')))
      for val1 in self.head_bounding_box_3d.corners:
        buff.write(_get_struct_3f().pack(*val1.kp))
      buff.write(_get_struct_3f().pack(*self.head_position))
      if len(self.skeleton_2d.keypoints) != 18:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (18, len(self.skeleton_2d.keypoints), 'self.skeleton_2d.keypoints')))
      for val1 in self.skeleton_2d.keypoints:
        buff.write(_get_struct_2f().pack(*val1.kp))
      if len(self.skeleton_3d.keypoints) != 18:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (18, len(self.skeleton_3d.keypoints), 'self.skeleton_3d.keypoints')))
      for val1 in self.skeleton_3d.keypoints:
        buff.write(_get_struct_3f().pack(*val1.kp))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.bounding_box_2d is None:
        self.bounding_box_2d = zed_interfaces.msg.BoundingBox2Di()
      if self.bounding_box_3d is None:
        self.bounding_box_3d = zed_interfaces.msg.BoundingBox3D()
      if self.head_bounding_box_2d is None:
        self.head_bounding_box_2d = zed_interfaces.msg.BoundingBox2Df()
      if self.head_bounding_box_3d is None:
        self.head_bounding_box_3d = zed_interfaces.msg.BoundingBox3D()
      if self.skeleton_2d is None:
        self.skeleton_2d = zed_interfaces.msg.Skeleton2D()
      if self.skeleton_3d is None:
        self.skeleton_3d = zed_interfaces.msg.Skeleton3D()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.label = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.label = str[start:end]
      _x = self
      start = end
      end += 4
      (_x.label_id, _x.instance_id,) = _get_struct_2h().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.sublabel = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.sublabel = str[start:end]
      start = end
      end += 4
      (self.confidence,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 12
      self.position = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 24
      self.position_covariance = _get_struct_6f().unpack(str[start:end])
      start = end
      end += 12
      self.velocity = _get_struct_3f().unpack(str[start:end])
      _x = self
      start = end
      end += 3
      (_x.tracking_available, _x.tracking_state, _x.action_state,) = _get_struct_B2b().unpack(str[start:end])
      self.tracking_available = bool(self.tracking_available)
      self.bounding_box_2d.corners = []
      for i in range(0, 4):
        val1 = zed_interfaces.msg.Keypoint2Di()
        start = end
        end += 8
        val1.kp = _get_struct_2I().unpack(str[start:end])
        self.bounding_box_2d.corners.append(val1)
      self.bounding_box_3d.corners = []
      for i in range(0, 8):
        val1 = zed_interfaces.msg.Keypoint3D()
        start = end
        end += 12
        val1.kp = _get_struct_3f().unpack(str[start:end])
        self.bounding_box_3d.corners.append(val1)
      start = end
      end += 12
      self.dimensions_3d = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 1
      (self.skeleton_available,) = _get_struct_B().unpack(str[start:end])
      self.skeleton_available = bool(self.skeleton_available)
      self.head_bounding_box_2d.corners = []
      for i in range(0, 4):
        val1 = zed_interfaces.msg.Keypoint2Df()
        start = end
        end += 8
        val1.kp = _get_struct_2f().unpack(str[start:end])
        self.head_bounding_box_2d.corners.append(val1)
      self.head_bounding_box_3d.corners = []
      for i in range(0, 8):
        val1 = zed_interfaces.msg.Keypoint3D()
        start = end
        end += 12
        val1.kp = _get_struct_3f().unpack(str[start:end])
        self.head_bounding_box_3d.corners.append(val1)
      start = end
      end += 12
      self.head_position = _get_struct_3f().unpack(str[start:end])
      self.skeleton_2d.keypoints = []
      for i in range(0, 18):
        val1 = zed_interfaces.msg.Keypoint2Df()
        start = end
        end += 8
        val1.kp = _get_struct_2f().unpack(str[start:end])
        self.skeleton_2d.keypoints.append(val1)
      self.skeleton_3d.keypoints = []
      for i in range(0, 18):
        val1 = zed_interfaces.msg.Keypoint3D()
        start = end
        end += 12
        val1.kp = _get_struct_3f().unpack(str[start:end])
        self.skeleton_3d.keypoints.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.label
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2h().pack(_x.label_id, _x.instance_id))
      _x = self.sublabel
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.confidence
      buff.write(_get_struct_f().pack(_x))
      buff.write(self.position.tostring())
      buff.write(self.position_covariance.tostring())
      buff.write(self.velocity.tostring())
      _x = self
      buff.write(_get_struct_B2b().pack(_x.tracking_available, _x.tracking_state, _x.action_state))
      if len(self.bounding_box_2d.corners) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.bounding_box_2d.corners), 'self.bounding_box_2d.corners')))
      for val1 in self.bounding_box_2d.corners:
        buff.write(val1.kp.tostring())
      if len(self.bounding_box_3d.corners) != 8:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (8, len(self.bounding_box_3d.corners), 'self.bounding_box_3d.corners')))
      for val1 in self.bounding_box_3d.corners:
        buff.write(val1.kp.tostring())
      buff.write(self.dimensions_3d.tostring())
      _x = self.skeleton_available
      buff.write(_get_struct_B().pack(_x))
      if len(self.head_bounding_box_2d.corners) != 4:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (4, len(self.head_bounding_box_2d.corners), 'self.head_bounding_box_2d.corners')))
      for val1 in self.head_bounding_box_2d.corners:
        buff.write(val1.kp.tostring())
      if len(self.head_bounding_box_3d.corners) != 8:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (8, len(self.head_bounding_box_3d.corners), 'self.head_bounding_box_3d.corners')))
      for val1 in self.head_bounding_box_3d.corners:
        buff.write(val1.kp.tostring())
      buff.write(self.head_position.tostring())
      if len(self.skeleton_2d.keypoints) != 18:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (18, len(self.skeleton_2d.keypoints), 'self.skeleton_2d.keypoints')))
      for val1 in self.skeleton_2d.keypoints:
        buff.write(val1.kp.tostring())
      if len(self.skeleton_3d.keypoints) != 18:
        self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (18, len(self.skeleton_3d.keypoints), 'self.skeleton_3d.keypoints')))
      for val1 in self.skeleton_3d.keypoints:
        buff.write(val1.kp.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.bounding_box_2d is None:
        self.bounding_box_2d = zed_interfaces.msg.BoundingBox2Di()
      if self.bounding_box_3d is None:
        self.bounding_box_3d = zed_interfaces.msg.BoundingBox3D()
      if self.head_bounding_box_2d is None:
        self.head_bounding_box_2d = zed_interfaces.msg.BoundingBox2Df()
      if self.head_bounding_box_3d is None:
        self.head_bounding_box_3d = zed_interfaces.msg.BoundingBox3D()
      if self.skeleton_2d is None:
        self.skeleton_2d = zed_interfaces.msg.Skeleton2D()
      if self.skeleton_3d is None:
        self.skeleton_3d = zed_interfaces.msg.Skeleton3D()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.label = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.label = str[start:end]
      _x = self
      start = end
      end += 4
      (_x.label_id, _x.instance_id,) = _get_struct_2h().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.sublabel = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.sublabel = str[start:end]
      start = end
      end += 4
      (self.confidence,) = _get_struct_f().unpack(str[start:end])
      start = end
      end += 12
      self.position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 24
      self.position_covariance = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=6)
      start = end
      end += 12
      self.velocity = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      _x = self
      start = end
      end += 3
      (_x.tracking_available, _x.tracking_state, _x.action_state,) = _get_struct_B2b().unpack(str[start:end])
      self.tracking_available = bool(self.tracking_available)
      self.bounding_box_2d.corners = []
      for i in range(0, 4):
        val1 = zed_interfaces.msg.Keypoint2Di()
        start = end
        end += 8
        val1.kp = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=2)
        self.bounding_box_2d.corners.append(val1)
      self.bounding_box_3d.corners = []
      for i in range(0, 8):
        val1 = zed_interfaces.msg.Keypoint3D()
        start = end
        end += 12
        val1.kp = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
        self.bounding_box_3d.corners.append(val1)
      start = end
      end += 12
      self.dimensions_3d = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 1
      (self.skeleton_available,) = _get_struct_B().unpack(str[start:end])
      self.skeleton_available = bool(self.skeleton_available)
      self.head_bounding_box_2d.corners = []
      for i in range(0, 4):
        val1 = zed_interfaces.msg.Keypoint2Df()
        start = end
        end += 8
        val1.kp = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
        self.head_bounding_box_2d.corners.append(val1)
      self.head_bounding_box_3d.corners = []
      for i in range(0, 8):
        val1 = zed_interfaces.msg.Keypoint3D()
        start = end
        end += 12
        val1.kp = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
        self.head_bounding_box_3d.corners.append(val1)
      start = end
      end += 12
      self.head_position = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      self.skeleton_2d.keypoints = []
      for i in range(0, 18):
        val1 = zed_interfaces.msg.Keypoint2Df()
        start = end
        end += 8
        val1.kp = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
        self.skeleton_2d.keypoints.append(val1)
      self.skeleton_3d.keypoints = []
      for i in range(0, 18):
        val1 = zed_interfaces.msg.Keypoint3D()
        start = end
        end += 12
        val1.kp = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
        self.skeleton_3d.keypoints.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_2h = None
def _get_struct_2h():
    global _struct_2h
    if _struct_2h is None:
        _struct_2h = struct.Struct("<2h")
    return _struct_2h
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_6f = None
def _get_struct_6f():
    global _struct_6f
    if _struct_6f is None:
        _struct_6f = struct.Struct("<6f")
    return _struct_6f
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_B2b = None
def _get_struct_B2b():
    global _struct_B2b
    if _struct_B2b is None:
        _struct_B2b = struct.Struct("<B2b")
    return _struct_B2b
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
