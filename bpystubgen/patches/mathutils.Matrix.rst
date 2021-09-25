.. method:: __add__(other)

   Add another matrix to this one.

   :arg other: A matrix to add.
   :type other: :class:`~mathutils.Matrix`
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __sub__(other)

   Subtract another matrix from this one.

   :arg other: A matrix to subtract.
   :type other: :class:`~mathutils.Matrix`
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __mul__(other)

   Multiply this matrix by another one or a scala value.

   :arg other: A matrix to multiply.
   :type other: :class:`~mathutils.Matrix` or float
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __rmul__(other)

   Multiply this matrix by a scala value.

   :arg other: A value to multiply.
   :type other: float
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __imul__(other)

   Multiply this matrix by another one or a scala value.

   :arg other: A matrix to multiply.
   :type other: :class:`~mathutils.Matrix` or float
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __matmul__(other)

   Multiply this matrix by another one.

   :arg other: A matrix to multiply.
   :type other: :class:`~mathutils.Matrix` or :class:`~mathutils.Vector` or :class:`~mathutils.Quaternion`
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix` or :class:`~mathutils.Vector` or :class:`~mathutils.Quaternion`

.. method:: __imatmul__(other)

   Multiply this matrix by another one.

   :arg other: A matrix to multiply.
   :type other: :class:`~mathutils.Matrix` or :class:`~mathutils.Vector` or :class:`~mathutils.Quaternion`
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix` or :class:`~mathutils.Vector` or :class:`~mathutils.Quaternion`

.. method:: __invert__()

   Invert this matrix.

   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __truediv__(value)

   Divide this matrix by a float value.

   :arg value: A divider value.
   :type value: float
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`

.. method:: __itruediv__(value)

   Divide this matrix by a float value.

   :arg value: A divider value.
   :type value: float
   :return: The resulting matrix.
   :rtype: :class:`~mathutils.Matrix`
