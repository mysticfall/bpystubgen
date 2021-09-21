.. method:: __add__(other)

   Add another quaternion to this one.

   :arg other: A quaternion to add.
   :type other: :class:`~mathutils.Quaternion`
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __sub__(other)

   Subtract another quaternion from this one.

   :arg other: A quaternion to subtract.
   :type other: :class:`~mathutils.Quaternion`
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __mul__(other)

   Multiply this quaternion by another one or a scala value.

   :arg other: A quaternion to multiply.
   :type other: :class:`~mathutils.Quaternion` or float
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __rmul__(other)

   Multiply this quaternion by a scala value.

   :arg other: A quaternion to multiply.
   :type other: float
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __imul__(other)

   Multiply this quaternion by another one or a scala value.

   :arg other: A quaternion to multiply.
   :type other: :class:`~mathutils.Quaternion` or float
   :return: The resulting quaternion.
   :rtype: :class:`~mathutils.Quaternion`

.. method:: __matmul__(other)

   Multiply with another quaternion or a vector.

   :arg other: A quaternion to multiply.
   :type other: :class:`~mathutils.Quaternion` or :class:`~mathutils.Vector`
   :return: The resulting quaternion or vector.
   :rtype: :class:`~mathutils.Quaternion` or :class:`~mathutils.Vector`

.. method:: __imatmul__(other)

   Multiply with another quaternion or a vector.

   :arg other: A quaternion to multiply.
   :type other: :class:`~mathutils.Quaternion` or :class:`~mathutils.Vector`
   :return: The resulting quaternion or vector.
   :rtype: :class:`~mathutils.Quaternion` or :class:`~mathutils.Vector`
