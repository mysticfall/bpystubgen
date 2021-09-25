.. method:: __add__(other)

   Add another vector to this one.

   :arg other: A vector to add.
   :type other: :class:`~mathutils.Vector`
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __sub__(other)

   Subtract another vector from this one.

   :arg other: A vector to subtract.
   :type other: :class:`~mathutils.Vector`
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __mul__(other)

   Multiply this vector by another one or a scala value.

   :arg other: A vector to multiply.
   :type other: :class:`~mathutils.Vector` or float
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __rmul__(other)

   Multiply this vector by a scala value.

   :arg other: A vector to multiply.
   :type other: float
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __imul__(other)

   Multiply this vector by another one or a scala value.

   :arg other: A vector to multiply.
   :type other: :class:`~mathutils.Vector` or float
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __matmul__(other)

   Scala product with another vector.

   :arg other: A vector to multiply.
   :type other: :class:`~mathutils.Vector`
   :return: The resulting product.
   :rtype: float

.. method:: __imatmul__(other)

   Scala product with another vector.

   :arg other: A vector to multiply.
   :type other: :class:`~mathutils.Vector`
   :return: The resulting product.
   :rtype: float

.. method:: __truediv__(value)

   Divide this vector by a float value.

   :arg value: A divider value.
   :type value: float
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`

.. method:: __itruediv__(value)

   Divide this vector by a float value.

   :arg value: A divider value.
   :type value: float
   :return: The resulting vector.
   :rtype: :class:`~mathutils.Vector`
