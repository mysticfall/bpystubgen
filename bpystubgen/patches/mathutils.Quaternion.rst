.. method:: __add__(value)

   Add another quaternion to this one.

   :arg value: The quaternion to add.
   :type value: :class:`~mathutils.Quaternion`
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __sub__(value)

   Subtract another quaternion from this one.

   :arg value: The quaternion to subtract.
   :type value: :class:`~mathutils.Quaternion`
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __mul__(value)

   Multiply this quaternion with another one or a scala value.

   :arg value: The multiplier value.
   :type value: :class:`~mathutils.Quaternion` or float
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __rmul__(value)

   Multiply this quaternion with a scala value.

   :arg value: The multiplier value.
   :type value: float
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __imul__(value)

   Multiply this quaternion with another one or a scala value.

   :arg value: The multiplier value.
   :type value: :class:`~mathutils.Quaternion` or float
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __matmul__(value)

   Multiply with another quaternion or a vector.

   :arg value: The quaternion or vector to multiply.
   :type value: :class:`~mathutils.Quaternion` or :class:`~mathutils.Vector`
   :return: The resulting quaternion or vector.
   :rtype: :class:`~mathutils.Quaternion` or :class:`~mathutils.Vector`

.. method:: __imatmul__(value)

   Multiply with another quaternion or a vector.

   :arg value: The quaternion or vector to multiply.
   :type value: :class:`~mathutils.Quaternion` or :class:`~mathutils.Vector`
   :return: The resulting quaternion or vector.
   :rtype: :class:`~mathutils.Quaternion` or :class:`~mathutils.Vector`


.. method:: __truediv__(value)

   Divide this quaternion by a float value.

   :arg value: The divider value.
   :type value: float
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __itruediv__(value)

   Divide this quaternion by a float value.

   :arg value: The divider value.
   :type value: float
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __getitem__(index)

   Get quaternion component at index.

   :arg index: The index of the component.
   :type index: int
   :return: The component value.
   :rtype: float

.. method:: __setitem__(index, value)

   Set quaternion component at index.

   :arg index: The index of the component.
   :type index: int
   :arg value: The value to set.
   :type value: float
