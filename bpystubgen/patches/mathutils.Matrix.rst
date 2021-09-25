.. method:: __add__(value)

   Add another matrix to this one.

   :arg value: The matrix to add.
   :type value: :class:`~mathutils.Matrix`
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __sub__(value)

   Subtract another matrix from this one.

   :arg value: The matrix to subtract.
   :type value: :class:`~mathutils.Matrix`
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __mul__(value)

   Multiply this matrix with another one or a scala value.

   :arg value: The multiplier value.
   :type value: :class:`~mathutils.Matrix` or float
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __rmul__(value)

   Multiply this matrix with a scala value.

   :arg value: The multiplier value.
   :type value: float
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __imul__(value)

   Multiply this matrix by another one or a scala value.

   :arg value: The multiplier value.
   :type value: :class:`~mathutils.Matrix` or float
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __matmul__(value)

   Multiply this matrix with another matrix, a vector, or quaternion.

   :arg value: The multiplier value.
   :type value: :class:`~mathutils.Matrix` or :class:`~mathutils.Vector` or :class:`~mathutils.Quaternion`
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix` or :class:`~mathutils.Vector` or :class:`~mathutils.Quaternion`

.. method:: __imatmul__(value)

   Multiply this matrix with another matrix, a vector, or quaternion.

   :arg value: The multiplier value.
   :type value: :class:`~mathutils.Matrix` or :class:`~mathutils.Vector` or :class:`~mathutils.Quaternion`
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix` or :class:`~mathutils.Vector` or :class:`~mathutils.Quaternion`

.. method:: __invert__()

   Invert this matrix.

   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __truediv__(value)

   Divide this matrix by a float value.

   :arg value: The divider value.
   :type value: float
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __itruediv__(value)

   Divide this matrix by a float value.

   :arg value: The divider value.
   :type value: float
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __getitem__(index)

   Get the row at given index.

   :arg index: The index of the row.
   :type index: int
   :return: The row at the given index.
   :rtype: :class:`~mathutils.Vector`

.. method:: __setitem__(index, value)

   Set the row at given index.

   :arg index: The index of the row.
   :type index: int
   :arg value: The row to set.
   :type value: :class:`~mathutils.Vector` or a tuple of floats.
