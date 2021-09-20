import typing

import mathutils

import logging

import bpy

import bge

class KX_GameObject(bge.types.SCA_IObject):

  """

  All game objects are derived from this class.

  Properties assigned to game objects are accessible as attributes of this class.

  Note: Calling ANY method or attribute on an object that has been removed from a scene will raise a SystemError,
if an object may have been removed since last accessing it use the :attr:`invalid <bge.types.EXP_PyObjectPlus.invalid>` attribute to check.

  KX_GameObject can be subclassed to extend functionality. For example:

  .. code:: python

    import bge

    class CustomGameObject(bge.types.KX_GameObject):
        RATE = 0.05

        def __init__(self, old_owner):
            # "old_owner" can just be ignored. At this point, "self" is
            # already the object in the scene, and "old_owner" has been
            # destroyed.

            # New attributes can be defined - but we could also use a game
            # property, like "self['rate']".
            self.rate = CustomGameObject.RATE

        def update(self):
            self.worldPosition.z += self.rate

            # switch direction
            if self.worldPosition.z > 1.0:
                self.rate = -CustomGameObject.RATE
            elif self.worldPosition.z < 0.0:
                self.rate = CustomGameObject.RATE

    # Called first
    def mutate(cont):
        old_object = cont.owner
        mutated_object = CustomGameObject(cont.owner)

        # After calling the constructor above, references to the old object
        # should not be used.
        assert(old_object is not mutated_object)
        assert(old_object.invalid)
        assert(mutated_object is cont.owner)

    # Called later - note we are now working with the mutated object.
    def update(cont):
        cont.owner.update()

  When subclassing objects other than empties and meshes, the specific type
should be used - e.g. inherit from :class:`BL_ArmatureObject <bge.types.BL_ArmatureObject>` when the object
to mutate is an armature.

  """

  name: str = ...

  """

  The object's name.

  """

  mass: float = ...

  """

  The object's mass

  Note: The object must have a physics controller for the mass to be applied, otherwise the mass value will be returned as 0.0.

  """

  friction: float = ...

  """

  The object's friction

  Note: The object must have a physics controller for the friction to be applied, otherwise the friction value will be returned as 0.0.

  """

  isSuspendDynamics: bool = ...

  """

  The object's dynamic state (read-only).

  :meth:`suspendDynamics` and :meth:`restoreDynamics` allow you to change the state.

  """

  linearDamping: float = ...

  """

  The object's linear damping, also known as translational damping. Can be set simultaneously with angular damping using the :meth:`setDamping` method.

  Note: The object must have a physics controller for the linear damping to be applied, otherwise the value will be returned as 0.0.

  """

  angularDamping: float = ...

  """

  The object's angular damping, also known as rotationation damping. Can be set simultaneously with linear damping using the :meth:`setDamping` method.

  Note: The object must have a physics controller for the angular damping to be applied, otherwise the value will be returned as 0.0.

  """

  linVelocityMin: float = ...

  """

  Enforces the object keeps moving at a minimum velocity.

  Note: Applies to dynamic and rigid body objects only.

  Note: A value of 0.0 disables this option.

  Note: While objects are stationary the minimum velocity will not be applied.

  """

  linVelocityMax: float = ...

  """

  Clamp the maximum linear velocity to prevent objects moving beyond a set speed.

  Note: Applies to dynamic and rigid body objects only.

  Note: A value of 0.0 disables this option (rather than setting it stationary).

  """

  angularVelocityMin: typing.Any = ...

  """

  Enforces the object keeps rotating at a minimum velocity. A value of 0.0 disables this.

  Note: Applies to dynamic and rigid body objects only.
While objects are stationary the minimum velocity will not be applied.

  """

  angularVelocityMax: typing.Any = ...

  """

  Clamp the maximum angular velocity to prevent objects rotating beyond a set speed.
A value of 0.0 disables clamping; it does not stop rotation.

  Note: Applies to dynamic and rigid body objects only.

  """

  localInertia: mathutils.Vector = ...

  """

  the object's inertia vector in local coordinates. Read only.

  """

  parent: bge.types.KX_GameObject = ...

  """

  The object's parent object. (read-only).

  """

  groupMembers: bge.types.EXP_ListValue = ...

  """

  Returns the list of group members if the object is a group object (dupli group instance), otherwise None is returned.

  """

  groupObject: bge.types.KX_GameObject = ...

  """

  Returns the group object (dupli group instance) that the object belongs to or None if the object is not part of a group.

  """

  collisionGroup: typing.Any = ...

  """

  The object's collision group.

  """

  collisionMask: typing.Any = ...

  """

  The object's collision mask.

  """

  collisionCallbacks: typing.List[typing.Callable] = ...

  """

  A list of functions to be called when a collision occurs.

  Callbacks should either accept one argument *(object)*, or four
arguments *(object, point, normal, points)*. For simplicity, per
colliding object the first collision point is reported in second
and third argument.

  .. code:: python

    # Function form
    def callback_four(object, point, normal, points):
        print('Hit by %r with %i contacts points' % (object.name, len(points)))

    def callback_three(object, point, normal):
        print('Hit by %r at %s with normal %s' % (object.name, point, normal))

    def callback_one(object):
        print('Hit by %r' % object.name)

    def register_callback(controller):
        controller.owner.collisionCallbacks.append(callback_four)
        controller.owner.collisionCallbacks.append(callback_three)
        controller.owner.collisionCallbacks.append(callback_one)


    # Method form
    class YourGameEntity(bge.types.KX_GameObject):
        def __init__(self, old_owner):
            self.collisionCallbacks.append(self.on_collision_four)
            self.collisionCallbacks.append(self.on_collision_three)
            self.collisionCallbacks.append(self.on_collision_one)

        def on_collision_four(self, object, point, normal, points):
            print('Hit by %r with %i contacts points' % (object.name, len(points)))

        def on_collision_three(self, object, point, normal):
            print('Hit by %r at %s with normal %s' % (object.name, point, normal))

        def on_collision_one(self, object):
            print('Hit by %r' % object.name)

  Note: For backward compatibility, a callback with variable number of
arguments (using **args*) will be passed only the *object*
argument. Only when there is more than one fixed argument (not
counting *self* for methods) will the four-argument form be
used.

  """

  scene: bge.types.KX_Scene = ...

  """

  The object's scene. (read-only).

  """

  visible: bool = ...

  """

  visibility flag.

  Note: Game logic will still run for invisible objects.

  """

  layer: typing.Any = ...

  """

  The layer mask used for shadow and real-time cube map render.

  """

  cullingBox: bge.types.KX_BoundingBox = ...

  """

  The object's bounding volume box used for culling.

  """

  culled: bool = ...

  """

  Returns True if the object is culled, else False.

  Warning: This variable returns an invalid value if it is called outside the scene's callbacks :attr:`KX_Scene.pre_draw <~bge.types.KX_Scene.pre_draw>` and :attr:`KX_Scene.post_draw <~bge.types.KX_Scene.post_draw>`.

  """

  color: mathutils.Vector = ...

  """

  The object color of the object. [r, g, b, a]

  """

  occlusion: bool = ...

  """

  occlusion capability flag.

  """

  position: mathutils.Vector = ...

  """

  The object's position. [x, y, z] On write: local position, on read: world position

  Deprecated since version 0.0.1: Use :attr:`localPosition` and :attr:`worldPosition`.

  """

  orientation: mathutils.Matrix = ...

  """

  The object's orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector. On write: local orientation, on read: world orientation

  Deprecated since version 0.0.1: Use :attr:`localOrientation` and :attr:`worldOrientation`.

  """

  scaling: mathutils.Vector = ...

  """

  The object's scaling factor. [sx, sy, sz] On write: local scaling, on read: world scaling

  Deprecated since version 0.0.1: Use :attr:`localScale` and :attr:`worldScale`.

  """

  localOrientation: mathutils.Matrix = ...

  """

  The object's local orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector.

  """

  worldOrientation: mathutils.Matrix = ...

  """

  The object's world orientation. 3x3 Matrix.

  """

  localScale: mathutils.Vector = ...

  """

  The object's local scaling factor. [sx, sy, sz]

  """

  worldScale: mathutils.Vector = ...

  """

  The object's world scaling factor. [sx, sy, sz]

  """

  localPosition: mathutils.Vector = ...

  """

  The object's local position. [x, y, z]

  """

  worldPosition: mathutils.Vector = ...

  """

  The object's world position. [x, y, z]

  """

  localTransform: mathutils.Matrix = ...

  """

  The object's local space transform matrix. 4x4 Matrix.

  """

  worldTransform: mathutils.Matrix = ...

  """

  The object's world space transform matrix. 4x4 Matrix.

  """

  localLinearVelocity: mathutils.Vector = ...

  """

  The object's local linear velocity. [x, y, z]

  """

  worldLinearVelocity: mathutils.Vector = ...

  """

  The object's world linear velocity. [x, y, z]

  """

  localAngularVelocity: mathutils.Vector = ...

  """

  The object's local angular velocity. [x, y, z]

  """

  worldAngularVelocity: mathutils.Vector = ...

  """

  The object's world angular velocity. [x, y, z]

  """

  gravity: mathutils.Vector = ...

  """

  The object's gravity. [x, y, z]

  """

  timeOffset: float = ...

  """

  adjust the slowparent delay at runtime.

  """

  blenderObject: bpy.types.Object = ...

  """

  This KX_GameObject's Object.

  """

  state: int = ...

  """

  the game object's state bitmask, using the first 30 bits, one bit must always be set.

  """

  meshes: typing.List[bge.types.KX_MeshProxy] = ...

  """

  a list meshes for this object.

  Note: Most objects use only 1 mesh.

  Note: Changes to this list will not update the KX_GameObject.

  """

  batchGroup: bge.types.KX_BatchGroup = ...

  """

  The object batch group containing the batched mesh.

  """

  sensors: typing.List[typing.Any] = ...

  """

  a sequence of :class:`SCA_ISensor <bge.types.SCA_ISensor>` objects with string/index lookups and iterator support.

  Note: This attribute is experimental and may be removed (but probably wont be).

  Note: Changes to this list will not update the KX_GameObject.

  """

  controllers: typing.List[bge.types.SCA_ISensor] = ...

  """

  a sequence of :class:`SCA_IController <bge.types.SCA_IController>` objects with string/index lookups and iterator support.

  Note: This attribute is experimental and may be removed (but probably wont be).

  Note: Changes to this list will not update the KX_GameObject.

  """

  actuators: typing.List[typing.Any] = ...

  """

  a list of :class:`SCA_IActuator <bge.types.SCA_IActuator>` with string/index lookups and iterator support.

  Note: This attribute is experemental and may be removed (but probably wont be).

  Note: Changes to this list will not update the KX_GameObject.

  """

  attrDict: typing.Dict[str, typing.Any] = ...

  """

  get the objects internal python attribute dictionary for direct (faster) access.

  """

  components: bge.types.EXP_ListValue = ...

  """

  All python components.

  """

  children: bge.types.EXP_ListValue = ...

  """

  direct children of this object, (read-only).

  """

  childrenRecursive: bge.types.EXP_ListValue = ...

  """

  all children of this object including children's children, (read-only).

  """

  life: float = ...

  """

  The number of frames until the object ends, assumes one frame is 1/50 second (read-only).

  """

  debug: bool = ...

  """

  If true, the object's debug properties will be displayed on screen.

  """

  debugRecursive: bool = ...

  """

  If true, the object's and children's debug properties will be displayed on screen.

  """

  currentLodLevel: int = ...

  """

  The index of the level of detail (LOD) currently used by this object (read-only).

  """

  lodManager: bge.types.KX_LodManager = ...

  """

  Return the lod manager of this object.
Needed to access to lod manager to set attributes of levels of detail of this object.
The lod manager is shared between instance objects and can be changed to use the lod levels of an other object.
If the lod manager is set to *None* the object's mesh backs to the mesh of the previous first lod level.

  """

  onRemove: typing.List[typing.Any] = ...

  """

  A list of callables to run when the KX_GameObject is destroyed.

  .. code:: python

    @gameobj.onRemove.append
    def callback(gameobj):
       print('exiting %s...' % gameobj.name)

  or

  .. code:: python

    cont = bge.logic.getCurrentController()
    gameobj = cont.owner

    def callback():
       print('exiting' %s...' % gameobj.name)

    gameobj.onRemove.append(callback)

  """

  @property

  def logger(self) -> logging.Logger:

    """

    A logger instance that can be used to log messages related to this object (read-only).

    """

    ...

  @property

  def loggerName(self) -> str:

    """

    A name used to create the logger instance. By default, it takes the form *Type[Name]*
and can be optionally overridden as below:

    .. code:: python

      @property
      def loggerName():
         return "MyObject"

    """

    ...

  def endObject(self) -> None:

    """

    Delete this object, can be used in place of the EndObject Actuator.

    The actual removal of the object from the scene is delayed.

    """

    ...

  def replaceMesh(self, mesh: bge.types.KX_MeshProxy, useDisplayMesh: bool = True, usePhysicsMesh: bool = False) -> None:

    """

    Replace the mesh of this object with a new mesh. This works the same was as the actuator.

    """

    ...

  def setVisible(self, visible: bool, recursive: bool = None) -> None:

    """

    Sets the game object's visible flag.

    """

    ...

  def setOcclusion(self, occlusion: bool, recursive: bool = None) -> None:

    """

    Sets the game object's occlusion capability.

    """

    ...

  def alignAxisToVect(self, vect: mathutils.Vector, axis: int = 2, factor: float = 1.0) -> None:

    """

    Aligns any of the game object's axis along the given vector.

    """

    ...

  def getAxisVect(self, vect: mathutils.Vector) -> typing.Any:

    """

    Returns the axis vector rotates by the object's worldspace orientation.
This is the equivalent of multiplying the vector by the orientation matrix.

    """

    ...

  def applyMovement(self, movement: mathutils.Vector, local: typing.Any = None) -> None:

    """

    Sets the game object's movement.

    """

    ...

  def applyRotation(self, rotation: mathutils.Vector, local: typing.Any = None) -> None:

    """

    Sets the game object's rotation.

    """

    ...

  def applyForce(self, force: mathutils.Vector, local: bool = None) -> None:

    """

    Sets the game object's force.

    This requires a dynamic object.

    """

    ...

  def applyTorque(self, torque: mathutils.Vector, local: bool = None) -> None:

    """

    Sets the game object's torque.

    This requires a dynamic object.

    """

    ...

  def getLinearVelocity(self, local: bool = None) -> mathutils.Vector:

    """

    Gets the game object's linear velocity.

    This method returns the game object's velocity through it's center of mass, ie no angular velocity component.

    """

    ...

  def setLinearVelocity(self, velocity: mathutils.Vector, local: bool = None) -> None:

    """

    Sets the game object's linear velocity.

    This method sets game object's velocity through it's center of mass,
ie no angular velocity component.

    This requires a dynamic object.

    """

    ...

  def getAngularVelocity(self, local: bool = None) -> mathutils.Vector:

    """

    Gets the game object's angular velocity.

    """

    ...

  def setAngularVelocity(self, velocity: bool, local: typing.Any = None) -> None:

    """

    Sets the game object's angular velocity.

    This requires a dynamic object.

    """

    ...

  def getVelocity(self, point: mathutils.Vector = None) -> mathutils.Vector:

    """

    Gets the game object's velocity at the specified point.

    Gets the game object's velocity at the specified point, including angular
components.

    """

    ...

  def getReactionForce(self) -> mathutils.Vector:

    """

    Gets the game object's reaction force.

    The reaction force is the force applied to this object over the last simulation timestep.
This also includes impulses, eg from collisions.

    Note: This is not implimented at the moment.

    """

    ...

  def applyImpulse(self, point: typing.Any, impulse: mathutils.Vector, local: bool = None) -> None:

    """

    Applies an impulse to the game object.

    This will apply the specified impulse to the game object at the specified point.
If point != position, applyImpulse will also change the object's angular momentum.
Otherwise, only linear momentum will change.

    """

    ...

  def setDamping(self, linear_damping: float, angular_damping: float) -> None:

    """

    Sets both the :attr:`linearDamping` and :attr:`angularDamping` simultaneously. This is more efficient than setting both properties individually.

    """

    ...

  def suspendPhysics(self, freeConstraints: bool = None) -> None:

    """

    Suspends physics for this object.

    """

    ...

  def restorePhysics(self) -> None:

    """

    Resumes physics for this object. Also reinstates collisions.

    """

    ...

  def suspendDynamics(self, ghost: bool = None) -> None:

    """

    Suspends dynamics physics for this object.

    :attr:`isSuspendDynamics` allows you to inspect whether the object is in a suspended state.

    """

    ...

  def restoreDynamics(self) -> None:

    """

    Resumes dynamics physics for this object. Also reinstates collisions; the object will no longer be a ghost.

    Note: The objects linear velocity will be applied from when the dynamics were suspended.

    """

    ...

  def enableRigidBody(self) -> None:

    """

    Enables rigid body physics for this object.

    Rigid body physics allows the object to roll on collisions.

    """

    ...

  def disableRigidBody(self) -> None:

    """

    Disables rigid body physics for this object.

    """

    ...

  def setCcdMotionThreshold(self, ccd_motion_threshold: float) -> None:

    """

    Sets :attr:`ccdMotionThreshold` that is the delta of movement that has to happen in one physics tick to trigger the continuous motion detection.

    Note: Setting the motion threshold to 0.0 deactive the Collision Continuous Detection (CCD).

    """

    ...

  def setCcdSweptSphereRadius(self, ccd_swept_sphere_radius: float) -> None:

    """

    Sets :attr:`ccdSweptSphereRadius` that is the radius of the sphere that is used to check for possible collisions when ccd is actived.

    """

    ...

  def setParent(self, parent: bge.types.KX_GameObject, compound: bool = True, ghost: bool = True) -> None:

    """

    Sets this object's parent.
Control the shape status with the optional compound and ghost parameters:

    In that case you can control if it should be ghost or not:

    Note: If the object type is sensor, it stays ghost regardless of ghost parameter

    """

    ...

  def removeParent(self) -> None:

    """

    Removes this objects parent.

    """

    ...

  def getPhysicsId(self) -> None:

    """

    Returns the user data object associated with this game object's physics controller.

    """

    ...

  def getPropertyNames(self) -> typing.List[typing.Any]:

    """

    Gets a list of all property names.

    """

    ...

  def getDistanceTo(self, other: bge.types.KX_GameObject) -> float:

    ...

  def getVectTo(self, other: bge.types.KX_GameObject) -> typing.Any:

    """

    Returns the vector and the distance to another object or point.
The vector is normalized unless the distance is 0, in which a zero length vector is returned.

    """

    ...

  def rayCastTo(self, other: bge.types.KX_GameObject, dist: float = 0, prop: str = '') -> bge.types.KX_GameObject:

    """

    Look towards another point/object and find first object hit within dist that matches prop.

    The ray is always casted from the center of the object, ignoring the object itself.
The ray is casted towards the center of another object or an explicit [x, y, z] point.
Use rayCast() if you need to retrieve the hit point

    """

    ...

  def rayCast(self, objto: bge.types.KX_GameObject, objfrom: bge.types.KX_GameObject = None, dist: float = 0, prop: str = '', face: int = False, xray: int = False, poly: int = 0, mask: typing.Any = 65535) -> typing.Any:

    """

    Look from a point/object to another point/object and find first object hit within dist that matches prop.
if poly is 0, returns a 3-tuple with object reference, hit point and hit normal or (None, None, None) if no hit.
if poly is 1, returns a 4-tuple with in addition a :class:`KX_PolyProxy <bge.types.KX_PolyProxy>` as 4th element.
if poly is 2, returns a 5-tuple with in addition a 2D vector with the UV mapping of the hit point as 5th element.

    .. code:: python

      # shoot along the axis gun-gunAim (gunAim should be collision-free)
      obj, point, normal = gun.rayCast(gunAim, None, 50)
      if obj:
         # do something
         pass

    The face parameter determines the orientation of the normal.

    * 0 => hit normal is always oriented towards the ray origin (as if you casted the ray from outside)

    * 1 => hit normal is the real face normal (only for mesh object, otherwise face has no effect)

    The ray has X-Ray capability if xray parameter is 1, otherwise the first object hit (other than self object) stops the ray.
The prop and xray parameters interact as follow.

    * prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray.

    * prop off, xray on : idem.

    * prop on, xray off: return closest hit if it matches prop, no hit otherwise.

    * prop on, xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray.

    The :class:`KX_PolyProxy <bge.types.KX_PolyProxy>` 4th element of the return tuple when poly=1 allows to retrieve information on the polygon hit by the ray.
If there is no hit or the hit object is not a static mesh, None is returned as 4th element.

    The ray ignores collision-free objects and faces that dont have the collision flag enabled, you can however use ghost objects.

    Note: The ray ignores the object on which the method is called. It is casted from/to object center or explicit [x, y, z] points.

    """

    ...

  def setCollisionMargin(self, margin: float) -> None:

    """

    Set the objects collision margin.

    Note: If this object has no physics controller (a physics ID of zero), this function will raise RuntimeError.

    """

    ...

  def sendMessage(self, subject: str, body: str = '', to: str = '') -> None:

    """

    Sends a message.

    """

    ...

  def reinstancePhysicsMesh(self, gameObject: str, meshObject: str, dupli: bool, evaluated: typing.Any) -> bool:

    """

    Updates the physics system with the changed mesh.

    If no arguments are given the physics mesh will be re-created from the first mesh assigned to the game object.

    Note: If this object has instances the other instances will be updated too.

    Note: The gameObject argument has an advantage that it can convert from a mesh with modifiers applied (such as the Subdivision Surface modifier).

    Warning: Only triangle mesh type objects are supported currently (not convex hull)

    Warning: If the object is a part of a compound object it will fail (parent or child)

    Warning: Rebuilding the physics mesh can be slow, running many times per second will give a performance hit.

    Warning: Duplicate the physics mesh can use much more memory, use this option only for duplicated meshes else use :meth:`replacePhysicsShape`.

    """

    ...

  def replacePhysicsShape(self, gameObject: str) -> bool:

    """

    Replace the current physics shape.

    Warning: Triangle mesh shapes are not supported.

    """

    ...

  def get(self, key: typing.Any, default: typing.Any = None) -> None:

    """

    Return the value matching key, or the default value if its not found.
:arg key: the matching key
:type key: string
:arg default: optional default value is the key isn't matching, defaults to None if no value passed.
:return: The key value or a default.

    """

    ...

  def playAction(self, name: str, start_frame: typing.Any, end_frame: typing.Any, layer: int = 0, priority: int = 0, blendin: float = 0, play_mode: typing.Any = KX_ACTION_MODE_PLAY, layer_weight: float = 0.0, ipo_flags: int = 0, speed: float = 1.0, blend_mode: typing.Any = KX_ACTION_BLEND_BLEND) -> None:

    """

    Plays an action.

    """

    ...

  def stopAction(self, layer: int = None) -> None:

    """

    Stop playing the action on the given layer.

    """

    ...

  def getActionFrame(self, layer: int = None) -> float:

    """

    Gets the current frame of the action playing in the supplied layer.

    """

    ...

  def getActionName(self, layer: int = None) -> str:

    """

    Gets the name of the current action playing in the supplied layer.

    """

    ...

  def setActionFrame(self, frame: float, layer: int = None) -> None:

    """

    Set the current frame of the action playing in the supplied layer.

    """

    ...

  def isPlayingAction(self, layer: int = None) -> bool:

    """

    Checks to see if there is an action playing in the given layer.

    """

    ...

  def addDebugProperty(self, name: str, debug: bool = None) -> None:

    """

    Adds a single debug property to the debug list.

    """

    ...

class KX_PythonComponent(bge.types.EXP_Value):

  """

  Python component can be compared to python logic bricks with parameters.
The python component is a script loaded in the UI, this script defined a component class by inheriting from :class:`KX_PythonComponent <bge.types.KX_PythonComponent>`.
This class must contain a dictionary of properties: :attr:`args` and two default functions: :meth:`start` and :meth:`update`.

  The script must have .py extension.

  The component properties are loaded from the :attr:`args` attribute from the UI at loading time.
When the game start the function :meth:`start` is called with as arguments a dictionary of the properties' name and value.
The :meth:`update` function is called every frames during the logic stage before running logics bricks,
the goal of this function is to handle and process everything.

  The following component example moves and rotates the object when pressing the keys W, A, S and D.

  .. code:: python

    import bge
    from collections import OrderedDict

    class ThirdPerson(bge.types.KX_PythonComponent):
        \"\"\"Basic third person controls

        W: move forward
        A: turn left
        S: move backward
        D: turn right

        \"\"\"

        #

        args = OrderedDict([
            ("Move Speed", 0.1),
            ("Turn Speed", 0.04)
        ])

        def start(self, args):
            self.move_speed = args['Move Speed']
            self.turn_speed = args['Turn Speed']

        def update(self):
            keyboard = bge.logic.keyboard.events

            move = 0
            rotate = 0

            if keyboard[bge.events.WKEY]:
                move += self.move_speed
            if keyboard[bge.events.SKEY]:
                move -= self.move_speed

            if keyboard[bge.events.AKEY]:
                rotate += self.turn_speed
            if keyboard[bge.events.DKEY]:
                rotate -= self.turn_speed

            self.object.applyMovement((0, move, 0), True)
            self.object.applyRotation((0, 0, rotate), True)

  Since the components are loaded for the first time outside the bge, then :attr:`bge` is a fake module that contains only the class
:class:`KX_PythonComponent <bge.types.KX_PythonComponent>` to avoid importing all the bge modules.
This behavior is safer but creates some issues at loading when the user want to use functions or attributes from the bge modules other
than the :class:`KX_PythonComponent <bge.types.KX_PythonComponent>` class. The way is to not call these functions at loading outside the bge. To detect it, the bge
module contains the attribute :attr:`__component__` when it's imported outside the bge.

  The following component example add a "Cube" object at initialization and move it along x for each update. It shows that the user can
use functions from scene and load the component outside the bge by setting global attributes in a condition at the beginning of the
script.

  .. code:: python

    import bge

    if not hasattr(bge, "__component__"):
        global scene
        scene = bge.logic.getCurrentScene()

    class Component(bge.types.KX_PythonComponent):
        args = {}

        def start(self, args):
            scene.addObject("Cube")

        def update(self):
            scene.objects["Cube"].worldPosition.x += 0.1

  The property types supported are float, integer, boolean, string, set (for enumeration) and Vector 2D, 3D and 4D. The following example
show all of these property types.

  .. code:: python

    from bge import *
    from mathutils import *
    from collections import OrderedDict

    class Component(types.KX_PythonComponent):
         args = OrderedDict([
             ("Float", 58.6),
             ("Integer", 150),
             ("Boolean", True),
             ("String", "Cube"),
             ("Enum", {"Enum 1", "Enum 2", "Enum 3"}),
             ("Vector 2D", Vector((0.8, 0.7))),
             ("Vector 3D", Vector((0.4, 0.3, 0.1))),
             ("Vector 4D", Vector((0.5, 0.2, 0.9, 0.6)))
         ])

         def start(self, args):
             print(args)

         def update(self):
             pass

  """

  object: bge.types.KX_GameObject = ...

  """

  The object owner of the component.

  """

  args: typing.Dict[str, typing.Any] = ...

  """

  Dictionary of the component properties, the keys are string and the value can be: float, integer, Vector(2D/3D/4D), set, string.

  """

  @property

  def logger(self) -> logging.Logger:

    """

    A logger instance that can be used to log messages related to this object (read-only).

    """

    ...

  @property

  def loggerName(self) -> str:

    """

    A name used to create the logger instance. By default, it takes the form *Type[Name]*
and can be optionally overridden as below:

    .. code:: python

      @property
      def loggerName():
         return "MyObject"

    """

    ...

  def start(self, args: typing.Dict[str, typing.Any]) -> None:

    """

    Initialize the component.

    Warning: This function must be inherited in the python component class.

    """

    ...

  def update(self) -> None:

    """

    Process the logic of the component.

    Warning: This function must be inherited in the python component class.

    """

    ...

  def dispose(self) -> None:

    """

    Function called when the component is destroyed.

    Warning: This function must be inherited in the python component class.

    """

    ...

class KX_Scene(bge.types.EXP_PyObjectPlus):

  """

  An active scene that gives access to objects, cameras, lights and scene attributes.

  The activity culling stuff is supposed to disable logic bricks when their owner gets too far
from the active camera.  It was taken from some code lurking at the back of KX_Scene - who knows
what it does!

  .. code:: python

    from bge import logic

    # get the scene
    scene = logic.getCurrentScene()

    # print all the objects in the scene
    for object in scene.objects:
       print(object.name)

    # get an object named 'Cube'
    object = scene.objects["Cube"]

    # get the first object in the scene.
    object = scene.objects[0]

  .. code:: python

    # Get the depth of an object in the camera view.
    from bge import logic

    object = logic.getCurrentController().owner
    cam = logic.getCurrentScene().active_camera

    # Depth is negative and decreasing further from the camera
    depth = object.position[0]*cam.world_to_camera[2][0] + object.position[1]*cam.world_to_camera[2][1] + object.position[2]*cam.world_to_camera[2][2] + cam.world_to_camera[2][3]

  @bug: All attributes are read only at the moment.

  """

  name: str = ...

  """

  The scene's name, (read-only).

  """

  objects: bge.types.EXP_ListValue = ...

  """

  A list of objects in the scene, (read-only).

  """

  objectsInactive: bge.types.EXP_ListValue = ...

  """

  A list of objects on background layers (used for the addObject actuator), (read-only).

  """

  lights: bge.types.EXP_ListValue = ...

  """

  A list of lights in the scene, (read-only).

  """

  cameras: bge.types.EXP_ListValue = ...

  """

  A list of cameras in the scene, (read-only).

  """

  texts: bge.types.EXP_ListValue = ...

  """

  A list of texts in the scene, (read-only).

  """

  active_camera: bge.types.KX_Camera = ...

  """

  The current active camera.

  .. code:: python

    import bge

    own = bge.logic.getCurrentController().owner
    scene = own.scene

    scene.active_camera = scene.objects["Camera.001"]

  Note: This can be set directly from python to avoid using the :class:`KX_SceneActuator <bge.types.KX_SceneActuator>`.

  """

  overrideCullingCamera: bge.types.KX_Camera = ...

  """

  The override camera used for scene culling, if set to None the culling is proceeded with the camera used to render.

  """

  world: bge.types.KX_WorldInfo = ...

  """

  The current active world, (read-only).

  """

  filterManager: bge.types.KX_2DFilterManager = ...

  """

  The scene's 2D filter manager, (read-only).

  """

  suspended: bool = ...

  """

  True if the scene is suspended, (read-only).

  """

  activity_culling: bool = ...

  """

  True if the scene is activity culling.

  """

  activity_culling_radius: float = ...

  """

  The distance outside which to do activity culling. Measured in manhattan distance.

  """

  dbvt_culling: bool = ...

  """

  True when Dynamic Bounding box Volume Tree is set (read-only).

  """

  pre_draw: typing.List[typing.Any] = ...

  """

  A list of callables to be run before the render step. The callbacks can take as argument the rendered camera.

  """

  post_draw: typing.List[typing.Any] = ...

  """

  A list of callables to be run after the render step.

  """

  pre_draw_setup: typing.List[typing.Any] = ...

  """

  A list of callables to be run before the drawing setup (i.e., before the model view and projection matrices are computed).
The callbacks can take as argument the rendered camera, the camera could be temporary in case of stereo rendering.

  """

  onRemove: typing.List[typing.Any] = ...

  """

  A list of callables to run when the scene is destroyed.

  .. code:: python

    @scene.onRemove.append
    def callback(scene):
       print('exiting %s...' % scene.name)

  """

  gravity: mathutils.Vector = ...

  """

  The scene gravity using the world x, y and z axis.

  """

  @property

  def logger(self) -> logging.Logger:

    """

    A logger instance that can be used to log messages related to this object (read-only).

    """

    ...

  @property

  def loggerName(self) -> str:

    """

    A name used to create the logger instance. By default, it takes the form *KX_Scene[Name]*.

    """

    ...

  def addObject(self, object: bge.types.KX_GameObject, reference: bge.types.KX_GameObject, time: float = 0.0, dupli: bool = False) -> bge.types.KX_GameObject:

    """

    Adds an object to the scene like the Add Object Actuator would.

    """

    ...

  def end(self) -> None:

    """

    Removes the scene from the game.

    """

    ...

  def restart(self) -> None:

    """

    Restarts the scene.

    """

    ...

  def replace(self, scene: str) -> bool:

    """

    Replaces this scene with another one.

    """

    ...

  def suspend(self) -> None:

    """

    Suspends this scene.

    """

    ...

  def resume(self) -> None:

    """

    Resume this scene.

    """

    ...

  def get(self, key: typing.Any, default: typing.Any = None) -> None:

    """

    Return the value matching key, or the default value if its not found.
:return: The key value or a default.

    """

    ...

  def drawObstacleSimulation(self) -> None:

    """

    Draw debug visualization of obstacle simulation.

    """

    ...

  def convertBlenderObject(self, blenderObject: typing.Any) -> None:

    """

    Converts a bpy.types.Object into a :class:`KX_GameObject <bge.types.KX_GameObject>` during runtime.
For example, you can append an Object from another .blend file during bge runtime
using: bpy.ops.wm.append(...) then convert this Object into a KX_GameObject to have
logic bricks, physics... converted. This is meant to replace libload.

    """

    ...

  def convertBlenderObjectsList(self, blenderObjectsList: typing.List[bpy.types.Object], asynchronous: bool) -> None:

    """

    Converts all bpy.types.Object inside a python List into its correspondent :class:`KX_GameObject <bge.types.KX_GameObject>` during runtime.
For example, you can append an Object List during bge runtime using: ob = object_data_add(...) and ML.append(ob) then convert the Objects
inside the List into several KX_GameObject to have logic bricks, physics... converted. This is meant to replace libload.
The conversion can be asynchronous or synchronous.

    """

    ...

  def convertBlenderCollection(self, blenderCollection: bpy.types.Collection, asynchronous: bool) -> None:

    """

    Converts all bpy.types.Object inside a Collection into its correspondent :class:`KX_GameObject <bge.types.KX_GameObject>` during runtime.
For example, you can append a Collection from another .blend file during bge runtime
using: bpy.ops.wm.append(...) then convert the Objects inside the Collection into several KX_GameObject to have
logic bricks, physics... converted. This is meant to replace libload. The conversion can be asynchronous
or synchronous.

    """

    ...

  def convertBlenderAction(self, Action: bpy.types.Action) -> None:

    """

    Registers a bpy.types.Action into the bge logic manager to be abled to play it during runtime.
For example, you can append an Action from another .blend file during bge runtime
using: bpy.ops.wm.append(...) then register this Action to be abled to play it.

    """

    ...

  def unregisterBlenderAction(self, Action: bpy.types.Action) -> None:

    """

    Unregisters a bpy.types.Action from the bge logic manager.
The unregistered action will still be in the .blend file
but can't be played anymore with bge. If you want to completely
remove the action you need to call bpy.data.actions.remove(Action, do_unlink=True)
after you unregistered it from bge logic manager.

    """

    ...

  def addOverlayCollection(self, kxCamera: typing.Any, blenderCollection: bpy.types.Collection) -> None:

    """

    Adds an overlay collection (as with collection actuator) to render this collection objects
during a second render pass in overlay using the KX_Camera passed as argument.

    """

    ...

  def removeOverlayCollection(self, blenderCollection: bpy.types.Collection) -> None:

    """

    Removes an overlay collection (as with collection actuator).

    """

    ...

  def getGameObjectFromObject(self, blenderObject: bpy.types.Object) -> None:

    """

    Get the KX_GameObject corresponding to the blenderObject.

    """

    ...
