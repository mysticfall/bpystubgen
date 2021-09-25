.. method:: __add__(value)

   Add another vector to this one.

   :arg value: The vector to add.
   :type value: :class:`~mathutils.Vector`
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __sub__(value)

   Subtract another vector from this one.

   :arg value: The vector to subtract.
   :type value: :class:`~mathutils.Vector`
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __mul__(value)

   Multiply this vector with another one or a scala value.

   :arg value: The multiplier value.
   :type value: :class:`~mathutils.Vector` or float
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __rmul__(value)

   Multiply this vector with a scala value.

   :arg value: The multiplier value.
   :type value: float
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __imul__(value)

   Multiply this vector with another one or a scala value.

   :arg value: The multiplier value.
   :type value: :class:`~mathutils.Vector` or float
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __matmul__(value)

   Scala product with another vector.

   :arg value: The vector to multiply with.
   :type value: :class:`~mathutils.Vector`
   :return: The resulting product.
   :rtype: float

.. method:: __imatmul__(value)

   Scala product with another vector.

   :arg value: The vector to multiply with.
   :type value: :class:`~mathutils.Vector`
   :return: The resulting product.
   :rtype: float

.. method:: __truediv__(value)

   Divide this vector by a float value.

   :arg value: The divider value.
   :type value: float
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __itruediv__(value)

   Divide this vector by a float value.

   :arg value: The divider value.
   :type value: float
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`
