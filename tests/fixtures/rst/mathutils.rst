Math Types & Utilities (mathutils)
==================================

.. module:: mathutils

This module provides access to math operations.

.. note::

   Classes, methods and attributes that accept vectors also accept other numeric sequences,
   such as tuples, lists.

The :mod:`mathutils` module provides the following classes:

- :class:`Color`,
- :class:`Euler`,
- :class:`Matrix`,
- :class:`Quaternion`,
- :class:`Vector`,

.. toctree::
   :maxdepth: 1
   :caption: Submodules

   mathutils.geometry.rst
   mathutils.bvhtree.rst
   mathutils.kdtree.rst
   mathutils.interpolate.rst
   mathutils.noise.rst



.. literalinclude:: ../examples/mathutils.py

.. class:: Color(rgb)

   This object gives access to Colors in Blender.

   :param rgb: (r, g, b) color values
   :type rgb: 3d vector



   .. literalinclude:: ../examples/mathutils.Color.py

   .. function:: copy()
   
      Returns a copy of this color.
   
      :return: A copy of the color.
      :rtype: :class:`Color`
   
      .. note:: use this to get a copy of a wrapped color with
         no reference to the original data.


   .. function:: freeze()
   
      Make this object immutable.
   
      After this the object can be hashed, used in dictionaries & sets.
   
      :return: An instance of this object.


   .. attribute:: b

      Blue color channel.
      
      :type: float


   .. attribute:: g

      Green color channel.
      
      :type: float


   .. attribute:: h

      HSV Hue component in [0, 1].
      
      :type: float


   .. attribute:: hsv

      HSV Values in [0, 1].
      
      :type: float triplet


   .. attribute:: is_frozen

      True when this object has been frozen (read-only).
      
      :type: boolean


   .. attribute:: is_valid

      True when the owner of this data is valid.
      
      :type: boolean


   .. attribute:: is_wrapped

      True when this object wraps external data (read-only).
      
      :type: boolean


   .. attribute:: owner

      The item this is wrapping or None  (read-only).


   .. attribute:: r

      Red color channel.
      
      :type: float


   .. attribute:: s

      HSV Saturation component in [0, 1].
      
      :type: float


   .. attribute:: v

      HSV Value component in [0, 1].
      
      :type: float




.. class:: Euler(angles, order='XYZ')

   This object gives access to Eulers in Blender.

   .. seealso:: `Euler angles <https://en.wikipedia.org/wiki/Euler_angles>`__ on Wikipedia.

   :param angles: Three angles, in radians.
   :type angles: 3d vector
   :param order: Optional order of the angles, a permutation of ``XYZ``.
   :type order: str



   .. literalinclude:: ../examples/mathutils.Euler.py

   .. function:: copy()
   
      Returns a copy of this euler.
   
      :return: A copy of the euler.
      :rtype: :class:`Euler`
   
      .. note:: use this to get a copy of a wrapped euler with
         no reference to the original data.


   .. function:: freeze()
   
      Make this object immutable.
   
      After this the object can be hashed, used in dictionaries & sets.
   
      :return: An instance of this object.


   .. method:: make_compatible(other)
   
      Make this euler compatible with another,
      so interpolating between them works as intended.
   
      .. note:: the rotation order is not taken into account for this function.


   .. method:: rotate(other)
   
      Rotates the euler by another mathutils value.
   
      :arg other: rotation component of mathutils value
      :type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`


   .. method:: rotate_axis(axis, angle)
   
      Rotates the euler a certain amount and returning a unique euler rotation
      (no 720 degree pitches).
   
      :arg axis: single character in ['X, 'Y', 'Z'].
      :type axis: string
      :arg angle: angle in radians.
      :type angle: float


   .. method:: to_matrix()
   
      Return a matrix representation of the euler.
   
      :return: A 3x3 rotation matrix representation of the euler.
      :rtype: :class:`Matrix`


   .. method:: to_quaternion()
   
      Return a quaternion representation of the euler.
   
      :return: Quaternion representation of the euler.
      :rtype: :class:`Quaternion`


   .. method:: zero()
   
      Set all values to zero.


   .. attribute:: is_frozen

      True when this object has been frozen (read-only).
      
      :type: boolean


   .. attribute:: is_valid

      True when the owner of this data is valid.
      
      :type: boolean


   .. attribute:: is_wrapped

      True when this object wraps external data (read-only).
      
      :type: boolean


   .. attribute:: order

      Euler rotation order.
      
      :type: string in ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']


   .. attribute:: owner

      The item this is wrapping or None  (read-only).


   .. attribute:: x

      Euler axis angle in radians.
      
      :type: float


   .. attribute:: y

      Euler axis angle in radians.
      
      :type: float


   .. attribute:: z

      Euler axis angle in radians.
      
      :type: float




.. class:: Matrix([rows])

   This object gives access to Matrices in Blender, supporting square and rectangular
   matrices from 2x2 up to 4x4.

   :param rows: Sequence of rows.
      When omitted, a 4x4 identity matrix is constructed.
   :type rows: 2d number sequence



   .. literalinclude:: ../examples/mathutils.Matrix.py

   .. classmethod:: Diagonal(vector)
   
      Create a diagonal (scaling) matrix using the values from the vector.
   
      :arg vector: The vector of values for the diagonal.
      :type vector: :class:`Vector`
      :return: A diagonal matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: Identity(size)
   
      Create an identity matrix.
   
      :arg size: The size of the identity matrix to construct [2, 4].
      :type size: int
      :return: A new identity matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: LocRotScale(location, rotation, scale)
   
      Create a matrix combining translation, rotation and scale,
      acting as the inverse of the decompose() method.
   
      Any of the inputs may be replaced with None if not needed.
   
      :arg location: The translation component.
      :type location: :class:`Vector` or None
      :arg rotation: The rotation component.
      :type rotation: 3x3 :class:`Matrix`, :class:`Quaternion`, :class:`Euler` or None
      :arg scale: The scale component.
      :type scale: :class:`Vector` or None
      :return: Combined transformation matrix. 
      :rtype: 4x4 :class:`Matrix`



      .. literalinclude:: ../examples/mathutils.Matrix.LocRotScale.py


   .. classmethod:: OrthoProjection(axis, size)
   
      Create a matrix to represent an orthographic projection.
   
      :arg axis: Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'],
         where a single axis is for a 2D matrix.
         Or a vector for an arbitrary axis
      :type axis: string or :class:`Vector`
      :arg size: The size of the projection matrix to construct [2, 4].
      :type size: int
      :return: A new projection matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: Rotation(angle, size, axis)
   
      Create a matrix representing a rotation.
   
      :arg angle: The angle of rotation desired, in radians.
      :type angle: float
      :arg size: The size of the rotation matrix to construct [2, 4].
      :type size: int
      :arg axis: a string in ['X', 'Y', 'Z'] or a 3D Vector Object
         (optional when size is 2).
      :type axis: string or :class:`Vector`
      :return: A new rotation matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: Scale(factor, size, axis)
   
      Create a matrix representing a scaling.
   
      :arg factor: The factor of scaling to apply.
      :type factor: float
      :arg size: The size of the scale matrix to construct [2, 4].
      :type size: int
      :arg axis: Direction to influence scale. (optional).
      :type axis: :class:`Vector`
      :return: A new scale matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: Shear(plane, size, factor)
   
      Create a matrix to represent an shear transformation.
   
      :arg plane: Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'],
         where a single axis is for a 2D matrix only.
      :type plane: string
      :arg size: The size of the shear matrix to construct [2, 4].
      :type size: int
      :arg factor: The factor of shear to apply. For a 3 or 4 *size* matrix
         pass a pair of floats corresponding with the *plane* axis.
      :type factor: float or float pair
      :return: A new shear matrix.
      :rtype: :class:`Matrix`


   .. classmethod:: Translation(vector)
   
      Create a matrix representing a translation.
   
      :arg vector: The translation vector.
      :type vector: :class:`Vector`
      :return: An identity matrix with a translation.
      :rtype: :class:`Matrix`


   .. method:: adjugate()
   
      Set the matrix to its adjugate.
   
      :raises ValueError: if the matrix cannot be adjugate.
   
      .. seealso:: `Adjugate matrix <https://en.wikipedia.org/wiki/Adjugate_matrix>`__ on Wikipedia.


   .. method:: adjugated()
   
      Return an adjugated copy of the matrix.
   
      :return: the adjugated matrix.
      :rtype: :class:`Matrix`
      :raises ValueError: if the matrix cannot be adjugated


   .. method:: copy()
   
      Returns a copy of this matrix.
   
      :return: an instance of itself
      :rtype: :class:`Matrix`


   .. method:: decompose()
   
      Return the translation, rotation, and scale components of this matrix.
   
      :return: tuple of translation, rotation, and scale
      :rtype: (:class:`Vector`, :class:`Quaternion`, :class:`Vector`)


   .. method:: determinant()
   
      Return the determinant of a matrix.
   
      :return: Return the determinant of a matrix.
      :rtype: float
   
      .. seealso:: `Determinant <https://en.wikipedia.org/wiki/Determinant>`__ on Wikipedia.


   .. function:: freeze()
   
      Make this object immutable.
   
      After this the object can be hashed, used in dictionaries & sets.
   
      :return: An instance of this object.


   .. method:: identity()
   
      Set the matrix to the identity matrix.
   
      .. note:: An object with a location and rotation of zero, and a scale of one
         will have an identity matrix.
   
      .. seealso:: `Identity matrix <https://en.wikipedia.org/wiki/Identity_matrix>`__ on Wikipedia.


   .. method:: invert(fallback=None)
   
      Set the matrix to its inverse.
   
      :arg fallback: Set the matrix to this value when the inverse cannot be calculated
         (instead of raising a :exc:`ValueError` exception).
      :type fallback: :class:`Matrix`
   
      .. seealso:: `Inverse matrix <https://en.wikipedia.org/wiki/Inverse_matrix>`__ on Wikipedia.


   .. method:: invert_safe()
   
      Set the matrix to its inverse, will never error.
      If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
      If tweaked matrix is still degenerated, set to the identity matrix instead.
   
      .. seealso:: `Inverse Matrix <https://en.wikipedia.org/wiki/Inverse_matrix>`__ on Wikipedia.


   .. method:: inverted(fallback=None)
   
      Return an inverted copy of the matrix.
   
      :arg fallback: return this when the inverse can't be calculated
         (instead of raising a :exc:`ValueError`).
      :type fallback: any
      :return: the inverted matrix or fallback when given.
      :rtype: :class:`Matrix`


   .. method:: inverted_safe()
   
      Return an inverted copy of the matrix, will never error.
      If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
      If tweaked matrix is still degenerated, return the identity matrix instead.
   
      :return: the inverted matrix.
      :rtype: :class:`Matrix`


   .. function:: lerp(other, factor)
   
      Returns the interpolation of two matrices. Uses polar decomposition, see   "Matrix Animation and Polar Decomposition", Shoemake and Duff, 1992.
   
      :arg other: value to interpolate with.
      :type other: :class:`Matrix`
      :arg factor: The interpolation value in [0.0, 1.0].
      :type factor: float
      :return: The interpolated matrix.
      :rtype: :class:`Matrix`


   .. method:: normalize()
   
      Normalize each of the matrix columns.


   .. method:: normalized()
   
      Return a column normalized matrix
   
      :return: a column normalized matrix
      :rtype: :class:`Matrix`


   .. method:: resize_4x4()
   
      Resize the matrix to 4x4.


   .. method:: rotate(other)
   
      Rotates the matrix by another mathutils value.
   
      :arg other: rotation component of mathutils value
      :type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`
   
      .. note:: If any of the columns are not unit length this may not have desired results.


   .. method:: to_2x2()
   
      Return a 2x2 copy of this matrix.
   
      :return: a new matrix.
      :rtype: :class:`Matrix`


   .. method:: to_3x3()
   
      Return a 3x3 copy of this matrix.
   
      :return: a new matrix.
      :rtype: :class:`Matrix`


   .. method:: to_4x4()
   
      Return a 4x4 copy of this matrix.
   
      :return: a new matrix.
      :rtype: :class:`Matrix`


   .. method:: to_euler(order, euler_compat)
   
      Return an Euler representation of the rotation matrix
      (3x3 or 4x4 matrix only).
   
      :arg order: Optional rotation order argument in
         ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
      :type order: string
      :arg euler_compat: Optional euler argument the new euler will be made
         compatible with (no axis flipping between them).
         Useful for converting a series of matrices to animation curves.
      :type euler_compat: :class:`Euler`
      :return: Euler representation of the matrix.
      :rtype: :class:`Euler`


   .. method:: to_quaternion()
   
      Return a quaternion representation of the rotation matrix.
   
      :return: Quaternion representation of the rotation matrix.
      :rtype: :class:`Quaternion`


   .. method:: to_scale()
   
      Return the scale part of a 3x3 or 4x4 matrix.
   
      :return: Return the scale of a matrix.
      :rtype: :class:`Vector`
   
      .. note:: This method does not return a negative scale on any axis because it is not possible to obtain this data from the matrix alone.


   .. method:: to_translation()
   
      Return the translation part of a 4 row matrix.
   
      :return: Return the translation of a matrix.
      :rtype: :class:`Vector`


   .. method:: transpose()
   
      Set the matrix to its transpose.
   
      .. seealso:: `Transpose <https://en.wikipedia.org/wiki/Transpose>`__ on Wikipedia.


   .. method:: transposed()
   
      Return a new, transposed matrix.
   
      :return: a transposed matrix
      :rtype: :class:`Matrix`


   .. method:: zero()
   
      Set all the matrix values to zero.
   
      :rtype: :class:`Matrix`


   .. attribute:: col

      Access the matrix by columns, 3x3 and 4x4 only, (read-only).
      
      :type: Matrix Access


   .. attribute:: is_frozen

      True when this object has been frozen (read-only).
      
      :type: boolean


   .. attribute:: is_negative

      True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only).
      
      :type: bool


   .. attribute:: is_orthogonal

      True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only).
      
      :type: bool


   .. attribute:: is_orthogonal_axis_vectors

      True if this matrix has got orthogonal axis vectors, 3x3 and 4x4 only, (read-only).
      
      :type: bool


   .. attribute:: is_valid

      True when the owner of this data is valid.
      
      :type: boolean


   .. attribute:: is_wrapped

      True when this object wraps external data (read-only).
      
      :type: boolean


   .. attribute:: median_scale

      The average scale applied to each axis (read-only).
      
      :type: float


   .. attribute:: owner

      The item this is wrapping or None  (read-only).


   .. attribute:: row

      Access the matrix by rows (default), (read-only).
      
      :type: Matrix Access


   .. attribute:: translation

      The translation component of the matrix.
      
      :type: Vector




.. class:: Quaternion([seq, [angle]])

   This object gives access to Quaternions in Blender.

   :param seq: size 3 or 4
   :type seq: :class:`Vector`
   :param angle: rotation angle, in radians
   :type angle: float

   The constructor takes arguments in various forms:

   (), *no args*
      Create an identity quaternion
   (*wxyz*)
      Create a quaternion from a ``(w, x, y, z)`` vector.
   (*exponential_map*)
      Create a quaternion from a 3d exponential map vector.

      .. seealso:: :meth:`to_exponential_map`
   (*axis, angle*)
      Create a quaternion representing a rotation of *angle* radians over *axis*.

      .. seealso:: :meth:`to_axis_angle`



   .. literalinclude:: ../examples/mathutils.Quaternion.py

   .. function:: conjugate()
   
      Set the quaternion to its conjugate (negate x, y, z).


   .. function:: conjugated()
   
      Return a new conjugated quaternion.
   
      :return: a new quaternion.
      :rtype: :class:`Quaternion`


   .. function:: copy()
   
      Returns a copy of this quaternion.
   
      :return: A copy of the quaternion.
      :rtype: :class:`Quaternion`
   
      .. note:: use this to get a copy of a wrapped quaternion with
         no reference to the original data.


   .. method:: cross(other)
   
      Return the cross product of this quaternion and another.
   
      :arg other: The other quaternion to perform the cross product with.
      :type other: :class:`Quaternion`
      :return: The cross product.
      :rtype: :class:`Quaternion`


   .. method:: dot(other)
   
      Return the dot product of this quaternion and another.
   
      :arg other: The other quaternion to perform the dot product with.
      :type other: :class:`Quaternion`
      :return: The dot product.
      :rtype: float


   .. function:: freeze()
   
      Make this object immutable.
   
      After this the object can be hashed, used in dictionaries & sets.
   
      :return: An instance of this object.


   .. function:: identity()
   
      Set the quaternion to an identity quaternion.
   
      :rtype: :class:`Quaternion`


   .. function:: invert()
   
      Set the quaternion to its inverse.


   .. function:: inverted()
   
      Return a new, inverted quaternion.
   
      :return: the inverted value.
      :rtype: :class:`Quaternion`


   .. method:: make_compatible(other)
   
      Make this quaternion compatible with another,
      so interpolating between them works as intended.


   .. function:: negate()
   
      Set the quaternion to its negative.
   
      :rtype: :class:`Quaternion`


   .. function:: normalize()
   
      Normalize the quaternion.


   .. function:: normalized()
   
      Return a new normalized quaternion.
   
      :return: a normalized copy.
      :rtype: :class:`Quaternion`


   .. method:: rotate(other)
   
      Rotates the quaternion by another mathutils value.
   
      :arg other: rotation component of mathutils value
      :type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`


   .. function:: rotation_difference(other)
   
      Returns a quaternion representing the rotational difference.
   
      :arg other: second quaternion.
      :type other: :class:`Quaternion`
      :return: the rotational difference between the two quat rotations.
      :rtype: :class:`Quaternion`


   .. function:: slerp(other, factor)
   
      Returns the interpolation of two quaternions.
   
      :arg other: value to interpolate with.
      :type other: :class:`Quaternion`
      :arg factor: The interpolation value in [0.0, 1.0].
      :type factor: float
      :return: The interpolated rotation.
      :rtype: :class:`Quaternion`


   .. method:: to_axis_angle()
   
      Return the axis, angle representation of the quaternion.
   
      :return: axis, angle.
      :rtype: (:class:`Vector`, float) pair


   .. method:: to_euler(order, euler_compat)
   
      Return Euler representation of the quaternion.
   
      :arg order: Optional rotation order argument in
         ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
      :type order: string
      :arg euler_compat: Optional euler argument the new euler will be made
         compatible with (no axis flipping between them).
         Useful for converting a series of matrices to animation curves.
      :type euler_compat: :class:`Euler`
      :return: Euler representation of the quaternion.
      :rtype: :class:`Euler`


   .. method:: to_exponential_map()
   
      Return the exponential map representation of the quaternion.
   
      This representation consist of the rotation axis multiplied by the rotation angle.
      Such a representation is useful for interpolation between multiple orientations.
   
      :return: exponential map.
      :rtype: :class:`Vector` of size 3
   
      To convert back to a quaternion, pass it to the :class:`Quaternion` constructor.


   .. method:: to_matrix()
   
      Return a matrix representation of the quaternion.
   
      :return: A 3x3 rotation matrix representation of the quaternion.
      :rtype: :class:`Matrix`


   .. method:: to_swing_twist(axis)
   
      Split the rotation into a swing quaternion with the specified
      axis fixed at zero, and the remaining twist rotation angle.
   
      :arg axis: twist axis as a string in ['X', 'Y', 'Z']
      :return: swing, twist angle.
      :rtype: (:class:`Quaternion`, float) pair


   .. attribute:: angle

      Angle of the quaternion.
      
      :type: float


   .. attribute:: axis

      Quaternion axis as a vector.
      
      :type: :class:`Vector`


   .. attribute:: is_frozen

      True when this object has been frozen (read-only).
      
      :type: boolean


   .. attribute:: is_valid

      True when the owner of this data is valid.
      
      :type: boolean


   .. attribute:: is_wrapped

      True when this object wraps external data (read-only).
      
      :type: boolean


   .. attribute:: magnitude

      Size of the quaternion (read-only).
      
      :type: float


   .. attribute:: owner

      The item this is wrapping or None  (read-only).


   .. attribute:: w

      Quaternion axis value.
      
      :type: float


   .. attribute:: x

      Quaternion axis value.
      
      :type: float


   .. attribute:: y

      Quaternion axis value.
      
      :type: float


   .. attribute:: z

      Quaternion axis value.
      
      :type: float




.. class:: Vector(seq)

   This object gives access to Vectors in Blender.

   :param seq: Components of the vector, must be a sequence of at least two
   :type seq: sequence of numbers



   .. literalinclude:: ../examples/mathutils.Vector.py

   .. classmethod:: Fill(size, fill=0.0)
   
      Create a vector of length size with all values set to fill.
   
      :arg size: The length of the vector to be created.
      :type size: int
      :arg fill: The value used to fill the vector.
      :type fill: float


   .. classmethod:: Linspace(start, stop, size)
   
      Create a vector of the specified size which is filled with linearly spaced values between start and stop values.
   
      :arg start: The start of the range used to fill the vector.
      :type start: int
      :arg stop: The end of the range used to fill the vector.
      :type stop: int
      :arg size: The size of the vector to be created.
      :type size: int


   .. classmethod:: Range(start, stop, step=1)
   
      Create a filled with a range of values.
   
      :arg start: The start of the range used to fill the vector.
      :type start: int
      :arg stop: The end of the range used to fill the vector.
      :type stop: int
      :arg step: The step between successive values in the vector.
      :type step: int


   .. classmethod:: Repeat(vector, size)
   
      Create a vector by repeating the values in vector until the required size is reached.
   
      :arg tuple: The vector to draw values from.
      :type tuple: :class:`mathutils.Vector`
      :arg size: The size of the vector to be created.
      :type size: int


   .. function:: angle(other, fallback=None)
   
      Return the angle between two vectors.
   
      :arg other: another vector to compare the angle with
      :type other: :class:`Vector`
      :arg fallback: return this when the angle can't be calculated (zero length vector),
         (instead of raising a :exc:`ValueError`).
      :type fallback: any
      :return: angle in radians or fallback when given
      :rtype: float


   .. function:: angle_signed(other, fallback)
   
      Return the signed angle between two 2D vectors (clockwise is positive).
   
      :arg other: another vector to compare the angle with
      :type other: :class:`Vector`
      :arg fallback: return this when the angle can't be calculated (zero length vector),
         (instead of raising a :exc:`ValueError`).
      :type fallback: any
      :return: angle in radians or fallback when given
      :rtype: float


   .. function:: copy()
   
      Returns a copy of this vector.
   
      :return: A copy of the vector.
      :rtype: :class:`Vector`
   
      .. note:: use this to get a copy of a wrapped vector with
         no reference to the original data.


   .. method:: cross(other)
   
      Return the cross product of this vector and another.
   
      :arg other: The other vector to perform the cross product with.
      :type other: :class:`Vector`
      :return: The cross product.
      :rtype: :class:`Vector` or float when 2D vectors are used
   
      .. note:: both vectors must be 2D or 3D


   .. method:: dot(other)
   
      Return the dot product of this vector and another.
   
      :arg other: The other vector to perform the dot product with.
      :type other: :class:`Vector`
      :return: The dot product.
      :rtype: float


   .. function:: freeze()
   
      Make this object immutable.
   
      After this the object can be hashed, used in dictionaries & sets.
   
      :return: An instance of this object.


   .. function:: lerp(other, factor)
   
      Returns the interpolation of two vectors.
   
      :arg other: value to interpolate with.
      :type other: :class:`Vector`
      :arg factor: The interpolation value in [0.0, 1.0].
      :type factor: float
      :return: The interpolated vector.
      :rtype: :class:`Vector`


   .. method:: negate()
   
      Set all values to their negative.


   .. method:: normalize()
   
      Normalize the vector, making the length of the vector always 1.0.
   
      .. warning:: Normalizing a vector where all values are zero has no effect.
   
      .. note:: Normalize works for vectors of all sizes,
         however 4D Vectors w axis is left untouched.


   .. method:: normalized()
   
      Return a new, normalized vector.
   
      :return: a normalized copy of the vector
      :rtype: :class:`Vector`


   .. method:: orthogonal()
   
      Return a perpendicular vector.
   
      :return: a new vector 90 degrees from this vector.
      :rtype: :class:`Vector`
   
      .. note:: the axis is undefined, only use when any orthogonal vector is acceptable.


   .. function:: project(other)
   
      Return the projection of this vector onto the *other*.
   
      :arg other: second vector.
      :type other: :class:`Vector`
      :return: the parallel projection vector
      :rtype: :class:`Vector`


   .. method:: reflect(mirror)
   
      Return the reflection vector from the *mirror* argument.
   
      :arg mirror: This vector could be a normal from the reflecting surface.
      :type mirror: :class:`Vector`
      :return: The reflected vector matching the size of this vector.
      :rtype: :class:`Vector`


   .. method:: resize(size=3)
   
      Resize the vector to have size number of elements.


   .. method:: resize_2d()
   
      Resize the vector to 2D  (x, y).


   .. method:: resize_3d()
   
      Resize the vector to 3D  (x, y, z).


   .. method:: resize_4d()
   
      Resize the vector to 4D (x, y, z, w).


   .. method:: resized(size=3)
   
      Return a resized copy of the vector with size number of elements.
   
      :return: a new vector
      :rtype: :class:`Vector`


   .. function:: rotate(other)
   
      Rotate the vector by a rotation value.
   
      .. note:: 2D vectors are a special case that can only be rotated by a 2x2 matrix.
   
      :arg other: rotation component of mathutils value
      :type other: :class:`Euler`, :class:`Quaternion` or :class:`Matrix`


   .. function:: rotation_difference(other)
   
      Returns a quaternion representing the rotational difference between this
      vector and another.
   
      :arg other: second vector.
      :type other: :class:`Vector`
      :return: the rotational difference between the two vectors.
      :rtype: :class:`Quaternion`
   
      .. note:: 2D vectors raise an :exc:`AttributeError`.


   .. function:: slerp(other, factor, fallback=None)
   
      Returns the interpolation of two non-zero vectors (spherical coordinates).
   
      :arg other: value to interpolate with.
      :type other: :class:`Vector`
      :arg factor: The interpolation value typically in [0.0, 1.0].
      :type factor: float
      :arg fallback: return this when the vector can't be calculated (zero length vector or direct opposites),
         (instead of raising a :exc:`ValueError`).
      :type fallback: any
      :return: The interpolated vector.
      :rtype: :class:`Vector`


   .. method:: to_2d()
   
      Return a 2d copy of the vector.
   
      :return: a new vector
      :rtype: :class:`Vector`


   .. method:: to_3d()
   
      Return a 3d copy of the vector.
   
      :return: a new vector
      :rtype: :class:`Vector`


   .. method:: to_4d()
   
      Return a 4d copy of the vector.
   
      :return: a new vector
      :rtype: :class:`Vector`


   .. method:: to_track_quat(track, up)
   
      Return a quaternion rotation from the vector and the track and up axis.
   
      :arg track: Track axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z'].
      :type track: string
      :arg up: Up axis in ['X', 'Y', 'Z'].
      :type up: string
      :return: rotation from the vector and the track and up axis.
      :rtype: :class:`Quaternion`


   .. method:: to_tuple(precision=-1)
   
      Return this vector as a tuple with.
   
      :arg precision: The number to round the value to in [-1, 21].
      :type precision: int
      :return: the values of the vector rounded by *precision*
      :rtype: tuple


   .. method:: zero()
   
      Set all values to zero.


   .. attribute:: is_frozen

      True when this object has been frozen (read-only).
      
      :type: boolean


   .. attribute:: is_valid

      True when the owner of this data is valid.
      
      :type: boolean


   .. attribute:: is_wrapped

      True when this object wraps external data (read-only).
      
      :type: boolean


   .. attribute:: length

      Vector Length.
      
      :type: float


   .. attribute:: length_squared

      Vector length squared (v.dot(v)).
      
      :type: float


   .. attribute:: magnitude

      Vector Length.
      
      :type: float


   .. attribute:: owner

      The item this is wrapping or None  (read-only).


   .. attribute:: w

      Vector W axis (4D Vectors only).
      
      :type: float


   .. attribute:: ww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: www

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wwzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wxzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wywx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wywy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wywz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wyzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: wzzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: x

      Vector X axis.
      
      :type: float


   .. attribute:: xw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xwzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xxzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xywx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xywy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xywz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xyzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: xzzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: y

      Vector Y axis.
      
      :type: float


   .. attribute:: yw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: ywzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yxzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yywx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yywy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yywz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yyzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: yzzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: z

      Vector Z axis (3D Vectors only).
      
      :type: float


   .. attribute:: zw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zwzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zxzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zywx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zywy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zywz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zyzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzww

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzwx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzwy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzwz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzxw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzxx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzxy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzxz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzyw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzyx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzyy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzyz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzzw

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzzx

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzzy

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.


   .. attribute:: zzzz

      Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.




