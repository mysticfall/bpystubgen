"""


Math Types & Utilities (mathutils)
**********************************

This module provides access to math operations.

Note: Classes, methods and attributes that accept vectors also accept other numeric sequences,
such as tuples, lists.

The :mod:`mathutils` module provides the following classes:

* :class:`Color`,

* :class:`Euler`,

* :class:`Matrix`,

* :class:`Quaternion`,

* :class:`Vector`,

:class:`Color`

:class:`Euler`

:class:`Matrix`

:class:`Quaternion`

:class:`Vector`

"""

from . import geometry

import typing

class Color:

  """

  This object gives access to Colors in Blender.

  """

  def __init__(self, rgb: Vector) -> None:

    """

    :param rgb:       
      (r, g, b) color values

    :type rgb:        
      3d vector

    """

    ...

  def copy(self) -> Color:

    """

    Returns a copy of this color.

    Note: use this to get a copy of a wrapped color with
no reference to the original data.

    """

    ...

  def freeze(self) -> None:

    """

    Make this object immutable.

    After this the object can be hashed, used in dictionaries & sets.

    """

    ...

  b: float = ...

  """

  Blue color channel.

  """

  g: float = ...

  """

  Green color channel.

  """

  h: float = ...

  """

  HSV Hue component in [0, 1].

  """

  hsv: float = ...

  """

  HSV Values in [0, 1].

  """

  is_frozen: bool = ...

  """

  True when this object has been frozen (read-only).

  """

  is_valid: bool = ...

  """

  True when the owner of this data is valid.

  """

  is_wrapped: bool = ...

  """

  True when this object wraps external data (read-only).

  """

  owner: typing.Any = ...

  """

  The item this is wrapping or None  (read-only).

  """

  r: float = ...

  """

  Red color channel.

  """

  s: float = ...

  """

  HSV Saturation component in [0, 1].

  """

  v: float = ...

  """

  HSV Value component in [0, 1].

  """

class Euler:

  """

  This object gives access to Eulers in Blender.

  `Euler angles <https://en.wikipedia.org/wiki/Euler_angles>`_ on Wikipedia.

  """

  def __init__(self, angles: Vector, order: str = 'XYZ') -> None:

    """

    :param angles:    
      Three angles, in radians.

    :type angles:     
      3d vector

    :param order:     
      Optional order of the angles, a permutation of ``XYZ``.

    :type order:      
      str

    """

    ...

  def copy(self) -> Euler:

    """

    Returns a copy of this euler.

    Note: use this to get a copy of a wrapped euler with
no reference to the original data.

    """

    ...

  def freeze(self) -> None:

    """

    Make this object immutable.

    After this the object can be hashed, used in dictionaries & sets.

    """

    ...

  def make_compatible(self, other: typing.Any) -> None:

    """

    Make this euler compatible with another,
so interpolating between them works as intended.

    Note: the rotation order is not taken into account for this function.

    """

    ...

  def rotate(self, other: Euler) -> None:

    """

    Rotates the euler by another mathutils value.

    """

    ...

  def rotate_axis(self, axis: str, angle: float) -> None:

    """

    Rotates the euler a certain amount and returning a unique euler rotation
(no 720 degree pitches).

    """

    ...

  def to_matrix(self) -> Matrix:

    """

    Return a matrix representation of the euler.

    """

    ...

  def to_quaternion(self) -> Quaternion:

    """

    Return a quaternion representation of the euler.

    """

    ...

  def zero(self) -> None:

    """

    Set all values to zero.

    """

    ...

  is_frozen: bool = ...

  """

  True when this object has been frozen (read-only).

  """

  is_valid: bool = ...

  """

  True when the owner of this data is valid.

  """

  is_wrapped: bool = ...

  """

  True when this object wraps external data (read-only).

  """

  order: str = ...

  """

  Euler rotation order.

  """

  owner: typing.Any = ...

  """

  The item this is wrapping or None  (read-only).

  """

  x: float = ...

  """

  Euler axis angle in radians.

  """

  y: float = ...

  """

  Euler axis angle in radians.

  """

  z: float = ...

  """

  Euler axis angle in radians.

  """

class Matrix:

  """

  This object gives access to Matrices in Blender, supporting square and rectangular
matrices from 2x2 up to 4x4.

  """

  def __init__(self, rows: typing.Any = None) -> None:

    """

    :param rows:      
      Sequence of rows.
When omitted, a 4x4 identity matrix is constructed.

    :type rows:       
      2d number sequence

    """

    ...

  @classmethod

  def Diagonal(cls, vector: Vector) -> Matrix:

    """

    Create a diagonal (scaling) matrix using the values from the vector.

    """

    ...

  @classmethod

  def Identity(cls, size: int) -> Matrix:

    """

    Create an identity matrix.

    """

    ...

  @classmethod

  def LocRotScale(cls, location: Vector, rotation: typing.Any, scale: Vector) -> typing.Any:

    """

    Create a matrix combining translation, rotation and scale,
acting as the inverse of the decompose() method.

    Any of the inputs may be replaced with None if not needed.

    """

    ...

  @classmethod

  def OrthoProjection(cls, axis: typing.Union[str, Vector], size: int) -> Matrix:

    """

    Create a matrix to represent an orthographic projection.

    """

    ...

  @classmethod

  def Rotation(cls, angle: float, size: int, axis: typing.Union[str, Vector]) -> Matrix:

    """

    Create a matrix representing a rotation.

    """

    ...

  @classmethod

  def Scale(cls, factor: float, size: int, axis: Vector) -> Matrix:

    """

    Create a matrix representing a scaling.

    """

    ...

  @classmethod

  def Shear(cls, plane: str, size: int, factor: float) -> Matrix:

    """

    Create a matrix to represent an shear transformation.

    """

    ...

  @classmethod

  def Translation(cls, vector: Vector) -> Matrix:

    """

    Create a matrix representing a translation.

    """

    ...

  def adjugate(self) -> None:

    """

    Set the matrix to its adjugate.

    `Adjugate matrix <https://en.wikipedia.org/wiki/Adjugate_matrix>`_ on Wikipedia.

    """

    ...

  def adjugated(self) -> Matrix:

    """

    Return an adjugated copy of the matrix.

    """

    ...

  def copy(self) -> Matrix:

    """

    Returns a copy of this matrix.

    """

    ...

  def decompose(self) -> typing.Any:

    """

    Return the translation, rotation, and scale components of this matrix.

    """

    ...

  def determinant(self) -> float:

    """

    Return the determinant of a matrix.

    `Determinant <https://en.wikipedia.org/wiki/Determinant>`_ on Wikipedia.

    """

    ...

  def freeze(self) -> None:

    """

    Make this object immutable.

    After this the object can be hashed, used in dictionaries & sets.

    """

    ...

  def identity(self) -> None:

    """

    Set the matrix to the identity matrix.

    Note: An object with a location and rotation of zero, and a scale of one
will have an identity matrix.

    `Identity matrix <https://en.wikipedia.org/wiki/Identity_matrix>`_ on Wikipedia.

    """

    ...

  def invert(self, fallback: Matrix = None) -> None:

    """

    Set the matrix to its inverse.

    `Inverse matrix <https://en.wikipedia.org/wiki/Inverse_matrix>`_ on Wikipedia.

    """

    ...

  def invert_safe(self) -> None:

    """

    Set the matrix to its inverse, will never error.
If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
If tweaked matrix is still degenerated, set to the identity matrix instead.

    `Inverse Matrix <https://en.wikipedia.org/wiki/Inverse_matrix>`_ on Wikipedia.

    """

    ...

  def inverted(self, fallback: typing.Any = None) -> Matrix:

    """

    Return an inverted copy of the matrix.

    """

    ...

  def inverted_safe(self) -> Matrix:

    """

    Return an inverted copy of the matrix, will never error.
If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
If tweaked matrix is still degenerated, return the identity matrix instead.

    """

    ...

  def lerp(self, other: Matrix, factor: float) -> Matrix:

    """

    Returns the interpolation of two matrices. Uses polar decomposition, see   "Matrix Animation and Polar Decomposition", Shoemake and Duff, 1992.

    """

    ...

  def normalize(self) -> None:

    """

    Normalize each of the matrix columns.

    """

    ...

  def normalized(self) -> Matrix:

    """

    Return a column normalized matrix

    """

    ...

  def resize_4x4(self) -> None:

    """

    Resize the matrix to 4x4.

    """

    ...

  def rotate(self, other: Euler) -> None:

    """

    Rotates the matrix by another mathutils value.

    Note: If any of the columns are not unit length this may not have desired results.

    """

    ...

  def to_2x2(self) -> Matrix:

    """

    Return a 2x2 copy of this matrix.

    """

    ...

  def to_3x3(self) -> Matrix:

    """

    Return a 3x3 copy of this matrix.

    """

    ...

  def to_4x4(self) -> Matrix:

    """

    Return a 4x4 copy of this matrix.

    """

    ...

  def to_euler(self, order: str, euler_compat: Euler) -> Euler:

    """

    Return an Euler representation of the rotation matrix
(3x3 or 4x4 matrix only).

    """

    ...

  def to_quaternion(self) -> Quaternion:

    """

    Return a quaternion representation of the rotation matrix.

    """

    ...

  def to_scale(self) -> Vector:

    """

    Return the scale part of a 3x3 or 4x4 matrix.

    Note: This method does not return a negative scale on any axis because it is not possible to obtain this data from the matrix alone.

    """

    ...

  def to_translation(self) -> Vector:

    """

    Return the translation part of a 4 row matrix.

    """

    ...

  def transpose(self) -> None:

    """

    Set the matrix to its transpose.

    `Transpose <https://en.wikipedia.org/wiki/Transpose>`_ on Wikipedia.

    """

    ...

  def transposed(self) -> Matrix:

    """

    Return a new, transposed matrix.

    """

    ...

  def zero(self) -> Matrix:

    """

    Set all the matrix values to zero.

    """

    ...

  col: typing.Any = ...

  """

  Access the matrix by columns, 3x3 and 4x4 only, (read-only).

  """

  is_frozen: bool = ...

  """

  True when this object has been frozen (read-only).

  """

  is_negative: bool = ...

  """

  True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only).

  """

  is_orthogonal: bool = ...

  """

  True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only).

  """

  is_orthogonal_axis_vectors: bool = ...

  """

  True if this matrix has got orthogonal axis vectors, 3x3 and 4x4 only, (read-only).

  """

  is_valid: bool = ...

  """

  True when the owner of this data is valid.

  """

  is_wrapped: bool = ...

  """

  True when this object wraps external data (read-only).

  """

  median_scale: float = ...

  """

  The average scale applied to each axis (read-only).

  """

  owner: typing.Any = ...

  """

  The item this is wrapping or None  (read-only).

  """

  row: typing.Any = ...

  """

  Access the matrix by rows (default), (read-only).

  """

  translation: Vector = ...

  """

  The translation component of the matrix.

  """

class Quaternion:

  """

  This object gives access to Quaternions in Blender.

  The constructor takes arguments in various forms:

  (), *no args*
    Create an identity quaternion

  (*wxyz*)
    Create a quaternion from a ``(w, x, y, z)`` vector.

  (*exponential_map*)
    Create a quaternion from a 3d exponential map vector.

    :meth:`to_exponential_map`

  (*axis, angle*)
    Create a quaternion representing a rotation of *angle* radians over *axis*.

    :meth:`to_axis_angle`

  """

  def __init__(self, seq: Vector, angle: float = None) -> None:

    """

    :param seq:       
      size 3 or 4

    :type seq:        
      :class:`Vector`

    :param angle:     
      rotation angle, in radians

    :type angle:      
      float

    """

    ...

  def conjugate(self) -> None:

    """

    Set the quaternion to its conjugate (negate x, y, z).

    """

    ...

  def conjugated(self) -> Quaternion:

    """

    Return a new conjugated quaternion.

    """

    ...

  def copy(self) -> Quaternion:

    """

    Returns a copy of this quaternion.

    Note: use this to get a copy of a wrapped quaternion with
no reference to the original data.

    """

    ...

  def cross(self, other: Quaternion) -> Quaternion:

    """

    Return the cross product of this quaternion and another.

    """

    ...

  def dot(self, other: Quaternion) -> float:

    """

    Return the dot product of this quaternion and another.

    """

    ...

  def freeze(self) -> None:

    """

    Make this object immutable.

    After this the object can be hashed, used in dictionaries & sets.

    """

    ...

  def identity(self) -> Quaternion:

    """

    Set the quaternion to an identity quaternion.

    """

    ...

  def invert(self) -> None:

    """

    Set the quaternion to its inverse.

    """

    ...

  def inverted(self) -> Quaternion:

    """

    Return a new, inverted quaternion.

    """

    ...

  def make_compatible(self, other: typing.Any) -> None:

    """

    Make this quaternion compatible with another,
so interpolating between them works as intended.

    """

    ...

  def negate(self) -> Quaternion:

    """

    Set the quaternion to its negative.

    """

    ...

  def normalize(self) -> None:

    """

    Normalize the quaternion.

    """

    ...

  def normalized(self) -> Quaternion:

    """

    Return a new normalized quaternion.

    """

    ...

  def rotate(self, other: Euler) -> None:

    """

    Rotates the quaternion by another mathutils value.

    """

    ...

  def rotation_difference(self, other: Quaternion) -> Quaternion:

    """

    Returns a quaternion representing the rotational difference.

    """

    ...

  def slerp(self, other: Quaternion, factor: float) -> Quaternion:

    """

    Returns the interpolation of two quaternions.

    """

    ...

  def to_axis_angle(self) -> typing.Any:

    """

    Return the axis, angle representation of the quaternion.

    """

    ...

  def to_euler(self, order: str, euler_compat: Euler) -> Euler:

    """

    Return Euler representation of the quaternion.

    """

    ...

  def to_exponential_map(self) -> Vector:

    """

    Return the exponential map representation of the quaternion.

    This representation consist of the rotation axis multiplied by the rotation angle.
Such a representation is useful for interpolation between multiple orientations.

    To convert back to a quaternion, pass it to the :class:`Quaternion` constructor.

    """

    ...

  def to_matrix(self) -> Matrix:

    """

    Return a matrix representation of the quaternion.

    """

    ...

  def to_swing_twist(self, axis: typing.Any) -> typing.Any:

    """

    Split the rotation into a swing quaternion with the specified
axis fixed at zero, and the remaining twist rotation angle.

    """

    ...

  angle: float = ...

  """

  Angle of the quaternion.

  """

  axis: Vector = ...

  """

  Quaternion axis as a vector.

  """

  is_frozen: bool = ...

  """

  True when this object has been frozen (read-only).

  """

  is_valid: bool = ...

  """

  True when the owner of this data is valid.

  """

  is_wrapped: bool = ...

  """

  True when this object wraps external data (read-only).

  """

  magnitude: float = ...

  """

  Size of the quaternion (read-only).

  """

  owner: typing.Any = ...

  """

  The item this is wrapping or None  (read-only).

  """

  w: float = ...

  """

  Quaternion axis value.

  """

  x: float = ...

  """

  Quaternion axis value.

  """

  y: float = ...

  """

  Quaternion axis value.

  """

  z: float = ...

  """

  Quaternion axis value.

  """

class Vector:

  """

  This object gives access to Vectors in Blender.

  """

  def __init__(self, seq: typing.Sequence[typing.Any]) -> None:

    """

    :param seq:       
      Components of the vector, must be a sequence of at least two

    :type seq:        
      sequence of numbers

    """

    ...

  @classmethod

  def Fill(cls, size: int, fill: float = 0.0) -> None:

    """

    Create a vector of length size with all values set to fill.

    """

    ...

  @classmethod

  def Linspace(cls, start: int, stop: int, size: int) -> None:

    """

    Create a vector of the specified size which is filled with linearly spaced values between start and stop values.

    """

    ...

  @classmethod

  def Range(cls, start: int, stop: int, step: int = 1) -> None:

    """

    Create a filled with a range of values.

    """

    ...

  @classmethod

  def Repeat(cls, vector: typing.Any, size: int) -> None:

    """

    Create a vector by repeating the values in vector until the required size is reached.

    """

    ...

  def angle(self, other: Vector, fallback: typing.Any = None) -> float:

    """

    Return the angle between two vectors.

    """

    ...

  def angle_signed(self, other: Vector, fallback: typing.Any) -> float:

    """

    Return the signed angle between two 2D vectors (clockwise is positive).

    """

    ...

  def copy(self) -> Vector:

    """

    Returns a copy of this vector.

    Note: use this to get a copy of a wrapped vector with
no reference to the original data.

    """

    ...

  def cross(self, other: Vector) -> typing.Union[Vector, float]:

    """

    Return the cross product of this vector and another.

    Note: both vectors must be 2D or 3D

    """

    ...

  def dot(self, other: Vector) -> float:

    """

    Return the dot product of this vector and another.

    """

    ...

  def freeze(self) -> None:

    """

    Make this object immutable.

    After this the object can be hashed, used in dictionaries & sets.

    """

    ...

  def lerp(self, other: Vector, factor: float) -> Vector:

    """

    Returns the interpolation of two vectors.

    """

    ...

  def negate(self) -> None:

    """

    Set all values to their negative.

    """

    ...

  def normalize(self) -> None:

    """

    Normalize the vector, making the length of the vector always 1.0.

    Warning: Normalizing a vector where all values are zero has no effect.

    Note: Normalize works for vectors of all sizes,
however 4D Vectors w axis is left untouched.

    """

    ...

  def normalized(self) -> Vector:

    """

    Return a new, normalized vector.

    """

    ...

  def orthogonal(self) -> Vector:

    """

    Return a perpendicular vector.

    Note: the axis is undefined, only use when any orthogonal vector is acceptable.

    """

    ...

  def project(self, other: Vector) -> Vector:

    """

    Return the projection of this vector onto the *other*.

    """

    ...

  def reflect(self, mirror: Vector) -> Vector:

    """

    Return the reflection vector from the *mirror* argument.

    """

    ...

  def resize(self, size: typing.Any = 3) -> None:

    """

    Resize the vector to have size number of elements.

    """

    ...

  def resize_2d(self) -> None:

    """

    Resize the vector to 2D  (x, y).

    """

    ...

  def resize_3d(self) -> None:

    """

    Resize the vector to 3D  (x, y, z).

    """

    ...

  def resize_4d(self) -> None:

    """

    Resize the vector to 4D (x, y, z, w).

    """

    ...

  def resized(self, size: typing.Any = 3) -> Vector:

    """

    Return a resized copy of the vector with size number of elements.

    """

    ...

  def rotate(self, other: Euler) -> None:

    """

    Rotate the vector by a rotation value.

    Note: 2D vectors are a special case that can only be rotated by a 2x2 matrix.

    """

    ...

  def rotation_difference(self, other: Vector) -> Quaternion:

    """

    Returns a quaternion representing the rotational difference between this
vector and another.

    Note: 2D vectors raise an :exc:`AttributeError`.

    """

    ...

  def slerp(self, other: Vector, factor: float, fallback: typing.Any = None) -> Vector:

    """

    Returns the interpolation of two non-zero vectors (spherical coordinates).

    """

    ...

  def to_2d(self) -> Vector:

    """

    Return a 2d copy of the vector.

    """

    ...

  def to_3d(self) -> Vector:

    """

    Return a 3d copy of the vector.

    """

    ...

  def to_4d(self) -> Vector:

    """

    Return a 4d copy of the vector.

    """

    ...

  def to_track_quat(self, track: str, up: str) -> Quaternion:

    """

    Return a quaternion rotation from the vector and the track and up axis.

    """

    ...

  def to_tuple(self, precision: int = -1) -> typing.Tuple[typing.Any, ...]:

    """

    Return this vector as a tuple with.

    """

    ...

  def zero(self) -> None:

    """

    Set all values to zero.

    """

    ...

  is_frozen: bool = ...

  """

  True when this object has been frozen (read-only).

  """

  is_valid: bool = ...

  """

  True when the owner of this data is valid.

  """

  is_wrapped: bool = ...

  """

  True when this object wraps external data (read-only).

  """

  length: float = ...

  """

  Vector Length.

  """

  length_squared: float = ...

  """

  Vector length squared (v.dot(v)).

  """

  magnitude: float = ...

  """

  Vector Length.

  """

  owner: typing.Any = ...

  """

  The item this is wrapping or None  (read-only).

  """

  w: float = ...

  """

  Vector W axis (4D Vectors only).

  """

  ww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  www: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wwzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wxzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wywx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wywy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wywz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wyzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  wzzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  x: float = ...

  """

  Vector X axis.

  """

  xw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xwzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xxzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xywx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xywy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xywz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xyzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  xzzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  y: float = ...

  """

  Vector Y axis.

  """

  yw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  ywzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yxzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yywx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yywy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yywz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yyzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  yzzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  z: float = ...

  """

  Vector Z axis (3D Vectors only).

  """

  zw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zwzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zxzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zywx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zywy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zywz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zyzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzww: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzwx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzwy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzwz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzxw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzxx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzxy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzxz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzyw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzyx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzyy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzyz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzzw: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzzx: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzzy: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """

  zzzz: typing.Any = ...

  """

  Undocumented, consider `contributing <https://developer.blender.org/T51061>`_.

  """
