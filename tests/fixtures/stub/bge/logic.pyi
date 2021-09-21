"""


Game Logic (bge.logic)
**********************


Introduction
============

Module to access logic functions, imported automatically into the python controllers namespace.

.. code:: python

  # To get the controller thats running this python script:
  cont = bge.logic.getCurrentController() # bge.logic is automatically imported

  # To get the game object this controller is on:
  obj = cont.owner

:class:`~bge.types.KX_GameObject` and :class:`~bge.types.KX_Camera` or :class:`~bge.types.KX_LightObject` methods are available depending on the type of object

.. code:: python

  # To get a sensor linked to this controller.
  # "sensorname" is the name of the sensor as defined in the Blender interface.
  # +---------------------+  +--------+
  # | Sensor "sensorname" +--+ Python +
  # +---------------------+  +--------+
  sens = cont.sensors["sensorname"]

  # To get a sequence of all sensors:
  sensors = co.sensors

See the sensor's reference for available methods:

* :class:`~bge.types.SCA_MouseFocusSensor`

* :class:`~bge.types.SCA_NearSensor`

* :class:`~bge.types.KX_NetworkMessageSensor`

* :class:`~bge.types.SCA_RadarSensor`

* :class:`~bge.types.SCA_RaySensor`

* :class:`~bge.types.SCA_CollisionSensor`

* :class:`~bge.types.SCA_DelaySensor`

* :class:`~bge.types.SCA_JoystickSensor`

* :class:`~bge.types.SCA_KeyboardSensor`

* :class:`~bge.types.SCA_MouseSensor`

* :class:`~bge.types.SCA_PropertySensor`

* :class:`~bge.types.SCA_RandomSensor`

You can also access actuators linked to the controller

.. code:: python

  # To get an actuator attached to the controller:
  #                          +--------+  +-------------------------+
  #                          + Python +--+ Actuator "actuatorname" |
  #                          +--------+  +-------------------------+
  actuator = co.actuators["actuatorname"]

  # Activate an actuator
  controller.activate(actuator)

See the actuator's reference for available methods

* :class:`~bge.types.BL_ActionActuator`

* :class:`~bge.types.SCA_CameraActuator`

* :class:`~bge.types.SCA_ConstraintActuator`

* :class:`~bge.types.SCA_GameActuator`

* :class:`~bge.types.SCA_MouseActuator`

* :class:`~bge.types.KX_NetworkMessageActuator`

* :class:`~bge.types.SCA_ObjectActuator`

* :class:`~bge.types.SCA_ParentActuator`

* :class:`~bge.types.SCA_AddObjectActuator`

* :class:`~bge.types.SCA_DynamicActuator`

* :class:`~bge.types.SCA_EndObjectActuator`

* :class:`~bge.types.SCA_ReplaceMeshActuator`

* :class:`~bge.types.SCA_SceneActuator`

* :class:`~bge.types.SCA_SoundActuator`

* :class:`~bge.types.SCA_StateActuator`

* :class:`~bge.types.SCA_TrackToActuator`

* :class:`~bge.types.SCA_VisibilityActuator`

* :class:`~bge.types.SCA_2DFilterActuator`

* :class:`~bge.types.SCA_PropertyActuator`

* :class:`~bge.types.SCA_RandomActuator`

Most logic brick's methods are accessors for the properties available in the logic buttons.
Consult the logic bricks documentation for more information on how each logic brick works.

There are also methods to access the current :class:`bge.types.KX_Scene`

.. code:: python

  # Get the current scene
  scene = bge.logic.getCurrentScene()

  # Get the current camera
  cam = scene.active_camera

Matricies as used by the game engine are **row major**
``matrix[row][col] = float``

:class:`bge.types.KX_Camera` has some examples using matrices.


Variables
=========

:data:`globalDict`

:data:`keyboard`

:data:`mouse`

:data:`joysticks`


General functions
=================

:func:`getCurrentController`

:func:`getCurrentScene`

:func:`getSceneList`

:func:`getInactiveSceneNames`

:func:`loadGlobalDict`

:func:`saveGlobalDict`

:func:`startGame`

:func:`endGame`

:func:`restartGame`

:func:`LibLoad`

:func:`LibNew`

:func:`LibFree`

:func:`LibList`

:func:`addScene`

:func:`sendMessage`

:func:`setGravity`

:func:`getSpectrum`

:func:`getMaxLogicFrame`

:func:`setMaxLogicFrame`

:func:`getMaxPhysicsFrame`

:func:`setMaxPhysicsFrame`

:func:`getLogicTicRate`

:func:`setLogicTicRate`

:func:`getPhysicsTicRate`

:func:`setPhysicsTicRate`

:func:`getExitKey`

:func:`setExitKey`

:func:`NextFrame`

:func:`setRender`

:func:`getRender`


Time related functions
======================

:func:`getClockTime`

:func:`getFrameTime`

:func:`getRealTime`

:func:`getTimeScale`

:func:`setTimeScale`

:func:`getUseExternalClock`

:func:`setUseExternalClock`

:func:`setClockTime`


Utility functions
=================

:func:`expandPath`

:func:`getAverageFrameRate`

:func:`getBlendFileList`

:func:`getRandomFloat`

:func:`PrintGLInfo`

:func:`getGraphicsCardVendor`

:func:`PrintMemInfo`

:func:`getProfileInfo`


Constants
=========

:data:`KX_TRUE`

:data:`KX_FALSE`


Sensors
-------

.. _sensor-status:


Sensor Status
~~~~~~~~~~~~~

:data:`KX_SENSOR_INACTIVE`

:data:`KX_SENSOR_JUST_ACTIVATED`

:data:`KX_SENSOR_ACTIVE`

:data:`KX_SENSOR_JUST_DEACTIVATED`


Armature Sensor
~~~~~~~~~~~~~~~

.. _armaturesensor-type:

See :class:`bge.types.SCA_ArmatureSensor.type`

:data:`KX_ARMSENSOR_STATE_CHANGED`

:data:`KX_ARMSENSOR_LIN_ERROR_BELOW`

:data:`KX_ARMSENSOR_LIN_ERROR_ABOVE`

:data:`KX_ARMSENSOR_ROT_ERROR_BELOW`

:data:`KX_ARMSENSOR_ROT_ERROR_ABOVE`

.. _logic-property-sensor:


Property Sensor
~~~~~~~~~~~~~~~

:data:`KX_PROPSENSOR_EQUAL`

:data:`KX_PROPSENSOR_NOTEQUAL`

:data:`KX_PROPSENSOR_INTERVAL`

:data:`KX_PROPSENSOR_CHANGED`

:data:`KX_PROPSENSOR_EXPRESSION`

:data:`KX_PROPSENSOR_LESSTHAN`

:data:`KX_PROPSENSOR_GREATERTHAN`


Radar Sensor
~~~~~~~~~~~~

See :class:`bge.types.SCA_RadarSensor`

:data:`KX_RADAR_AXIS_POS_X`

:data:`KX_RADAR_AXIS_POS_Y`

:data:`KX_RADAR_AXIS_POS_Z`

:data:`KX_RADAR_AXIS_NEG_X`

:data:`KX_RADAR_AXIS_NEG_Y`

:data:`KX_RADAR_AXIS_NEG_Z`


Ray Sensor
~~~~~~~~~~

See :class:`bge.types.SCA_RaySensor`

:data:`KX_RAY_AXIS_POS_X`

:data:`KX_RAY_AXIS_POS_Y`

:data:`KX_RAY_AXIS_POS_Z`

:data:`KX_RAY_AXIS_NEG_X`

:data:`KX_RAY_AXIS_NEG_Y`

:data:`KX_RAY_AXIS_NEG_Z`


Actuators
---------

.. _action-actuator:


Action Actuator
~~~~~~~~~~~~~~~

See :class:`bge.types.BL_ActionActuator`

:data:`KX_ACTIONACT_PLAY`

:data:`KX_ACTIONACT_PINGPONG`

:data:`KX_ACTIONACT_FLIPPER`

:data:`KX_ACTIONACT_LOOPSTOP`

:data:`KX_ACTIONACT_LOOPEND`

:data:`KX_ACTIONACT_PROPERTY`


Armature Actuator
~~~~~~~~~~~~~~~~~

.. _armatureactuator-constants-type:

See :class:`bge.types.BL_ArmatureActuator.type`

:data:`KX_ACT_ARMATURE_RUN`

:data:`KX_ACT_ARMATURE_ENABLE`

:data:`KX_ACT_ARMATURE_DISABLE`

:data:`KX_ACT_ARMATURE_SETTARGET`

:data:`KX_ACT_ARMATURE_SETWEIGHT`

:data:`KX_ACT_ARMATURE_SETINFLUENCE`


Constraint Actuator
~~~~~~~~~~~~~~~~~~~

.. _constraint-actuator-option:

See :class:`bge.types.SCA_ConstraintActuator.option`

* Applicable to Distance constraint:

:data:`KX_CONSTRAINTACT_NORMAL`

:data:`KX_CONSTRAINTACT_DISTANCE`

:data:`KX_CONSTRAINTACT_LOCAL`

* Applicable to Force field constraint:

:data:`KX_CONSTRAINTACT_DOROTFH`

* Applicable to both:

:data:`KX_CONSTRAINTACT_MATERIAL`

:data:`KX_CONSTRAINTACT_PERMANENT`

.. _constraint-actuator-limit:

See :class:`bge.types.SCA_ConstraintActuator.limit`

:data:`KX_CONSTRAINTACT_LOCX`

:data:`KX_CONSTRAINTACT_LOCY`

:data:`KX_CONSTRAINTACT_LOCZ`

:data:`KX_CONSTRAINTACT_ROTX`

:data:`KX_CONSTRAINTACT_ROTY`

:data:`KX_CONSTRAINTACT_ROTZ`

:data:`KX_CONSTRAINTACT_DIRNX`

:data:`KX_CONSTRAINTACT_DIRNY`

:data:`KX_CONSTRAINTACT_DIRNZ`

:data:`KX_CONSTRAINTACT_DIRPX`

:data:`KX_CONSTRAINTACT_DIRPY`

:data:`KX_CONSTRAINTACT_DIRPZ`

:data:`KX_CONSTRAINTACT_ORIX`

:data:`KX_CONSTRAINTACT_ORIY`

:data:`KX_CONSTRAINTACT_ORIZ`

:data:`KX_CONSTRAINTACT_FHNX`

:data:`KX_CONSTRAINTACT_FHNY`

:data:`KX_CONSTRAINTACT_FHNZ`

:data:`KX_CONSTRAINTACT_FHPX`

:data:`KX_CONSTRAINTACT_FHPY`

:data:`KX_CONSTRAINTACT_FHPZ`


Dynamic Actuator
~~~~~~~~~~~~~~~~

See :class:`bge.types.SCA_DynamicActuator`

:data:`KX_DYN_RESTORE_DYNAMICS`

:data:`KX_DYN_DISABLE_DYNAMICS`

:data:`KX_DYN_ENABLE_RIGID_BODY`

:data:`KX_DYN_DISABLE_RIGID_BODY`

:data:`KX_DYN_SET_MASS`

.. _game-actuator:


Game Actuator
~~~~~~~~~~~~~

See :class:`bge.types.SCA_GameActuator`

:data:`KX_GAME_LOAD`

:data:`KX_GAME_START`

:data:`KX_GAME_RESTART`

:data:`KX_GAME_QUIT`

:data:`KX_GAME_SAVECFG`

:data:`KX_GAME_LOADCFG`

.. _mouse-actuator:


Mouse Actuator
~~~~~~~~~~~~~~

:data:`KX_ACT_MOUSE_OBJECT_AXIS_X`

:data:`KX_ACT_MOUSE_OBJECT_AXIS_Y`

:data:`KX_ACT_MOUSE_OBJECT_AXIS_Z`


Parent Actuator
~~~~~~~~~~~~~~~

:data:`KX_PARENT_REMOVE`

:data:`KX_PARENT_SET`

.. _logic-random-distributions:


Random Distributions
~~~~~~~~~~~~~~~~~~~~

See :class:`bge.types.SCA_RandomActuator`

:data:`KX_RANDOMACT_BOOL_CONST`

:data:`KX_RANDOMACT_BOOL_UNIFORM`

:data:`KX_RANDOMACT_BOOL_BERNOUILLI`

:data:`KX_RANDOMACT_INT_CONST`

:data:`KX_RANDOMACT_INT_UNIFORM`

:data:`KX_RANDOMACT_INT_POISSON`

:data:`KX_RANDOMACT_FLOAT_CONST`

:data:`KX_RANDOMACT_FLOAT_UNIFORM`

:data:`KX_RANDOMACT_FLOAT_NORMAL`

:data:`KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL`


Scene Actuator
~~~~~~~~~~~~~~

See :class:`bge.types.SCA_SceneActuator`

:data:`KX_SCENE_RESTART`

:data:`KX_SCENE_SET_SCENE`

:data:`KX_SCENE_SET_CAMERA`

:data:`KX_SCENE_ADD_FRONT_SCENE`

:data:`KX_SCENE_ADD_BACK_SCENE`

:data:`KX_SCENE_REMOVE_SCENE`

:data:`KX_SCENE_SUSPEND`

:data:`KX_SCENE_RESUME`

.. _logic-sound-actuator:


Sound Actuator
~~~~~~~~~~~~~~

See :class:`bge.types.SCA_SoundActuator`

:data:`KX_SOUNDACT_PLAYSTOP`

:data:`KX_SOUNDACT_PLAYEND`

:data:`KX_SOUNDACT_LOOPSTOP`

:data:`KX_SOUNDACT_LOOPEND`

:data:`KX_SOUNDACT_LOOPBIDIRECTIONAL`

:data:`KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP`


Steering Actuator
~~~~~~~~~~~~~~~~~

.. _logic-steering-actuator:

See :class:`bge.types.SCA_SteeringActuator.behavior`

:data:`KX_STEERING_SEEK`

:data:`KX_STEERING_FLEE`

:data:`KX_STEERING_PATHFOLLOWING`

.. _logic-trackto-actuator:


TrackTo Actuator
~~~~~~~~~~~~~~~~

See :class:`bge.types.SCA_TrackToActuator`

:data:`KX_TRACK_UPAXIS_POS_X`

:data:`KX_TRACK_UPAXIS_POS_Y`

:data:`KX_TRACK_UPAXIS_POS_Z`

:data:`KX_TRACK_TRAXIS_POS_X`

:data:`KX_TRACK_TRAXIS_POS_Y`

:data:`KX_TRACK_TRAXIS_POS_Z`

:data:`KX_TRACK_TRAXIS_NEG_X`

:data:`KX_TRACK_TRAXIS_NEG_Y`

:data:`KX_TRACK_TRAXIS_NEG_Z`


Various
-------


2D Filter
~~~~~~~~~

.. _two-d-filteractuator-mode:

:data:`RAS_2DFILTER_BLUR`

:data:`RAS_2DFILTER_CUSTOMFILTER`

:data:`RAS_2DFILTER_DILATION`

:data:`RAS_2DFILTER_DISABLED`

:data:`RAS_2DFILTER_ENABLED`

:data:`RAS_2DFILTER_EROSION`

:data:`RAS_2DFILTER_GRAYSCALE`

:data:`RAS_2DFILTER_INVERT`

:data:`RAS_2DFILTER_LAPLACIAN`

:data:`RAS_2DFILTER_MOTIONBLUR`

:data:`RAS_2DFILTER_NOFILTER`

:data:`RAS_2DFILTER_PREWITT`

:data:`RAS_2DFILTER_SEPIA`

:data:`RAS_2DFILTER_SHARPEN`

:data:`RAS_2DFILTER_SOBEL`


Armature Channel
~~~~~~~~~~~~~~~~

.. _armaturechannel-constants-rotation-mode:

See :class:`bge.types.BL_ArmatureChannel.rotation_mode`

:data:`ROT_MODE_QUAT`

:data:`ROT_MODE_XYZ`

:data:`ROT_MODE_XZY`

:data:`ROT_MODE_YXZ`

:data:`ROT_MODE_YZX`

:data:`ROT_MODE_ZXY`

:data:`ROT_MODE_ZYX`


Armature Constraint
~~~~~~~~~~~~~~~~~~~

.. _armatureconstraint-constants-type:

See :class:`bge.types.BL_ArmatureConstraint.type`

:data:`CONSTRAINT_TYPE_TRACKTO`

:data:`CONSTRAINT_TYPE_KINEMATIC`

:data:`CONSTRAINT_TYPE_ROTLIKE`

:data:`CONSTRAINT_TYPE_LOCLIKE`

:data:`CONSTRAINT_TYPE_MINMAX`

:data:`CONSTRAINT_TYPE_SIZELIKE`

:data:`CONSTRAINT_TYPE_LOCKTRACK`

:data:`CONSTRAINT_TYPE_STRETCHTO`

:data:`CONSTRAINT_TYPE_CLAMPTO`

:data:`CONSTRAINT_TYPE_TRANSFORM`

:data:`CONSTRAINT_TYPE_DISTLIMIT`

.. _armatureconstraint-constants-ik-type:

See :class:`bge.types.BL_ArmatureConstraint.ik_type`

:data:`CONSTRAINT_IK_COPYPOSE`

:data:`CONSTRAINT_IK_DISTANCE`

.. _armatureconstraint-constants-ik-flag:

See :class:`bge.types.BL_ArmatureConstraint.ik_flag`

:data:`CONSTRAINT_IK_FLAG_TIP`

:data:`CONSTRAINT_IK_FLAG_ROT`

:data:`CONSTRAINT_IK_FLAG_STRETCH`

:data:`CONSTRAINT_IK_FLAG_POS`

.. _armatureconstraint-constants-ik-mode:

See :class:`bge.types.BL_ArmatureConstraint.ik_mode`

:data:`CONSTRAINT_IK_MODE_INSIDE`

:data:`CONSTRAINT_IK_MODE_OUTSIDE`

:data:`CONSTRAINT_IK_MODE_ONSURFACE`

.. _input-status:


Blender Material
~~~~~~~~~~~~~~~~

:data:`BL_DST_ALPHA`

:data:`BL_DST_COLOR`

:data:`BL_ONE`

:data:`BL_ONE_MINUS_DST_ALPHA`

:data:`BL_ONE_MINUS_DST_COLOR`

:data:`BL_ONE_MINUS_SRC_ALPHA`

:data:`BL_ONE_MINUS_SRC_COLOR`

:data:`BL_SRC_ALPHA`

:data:`BL_SRC_ALPHA_SATURATE`

:data:`BL_SRC_COLOR`

:data:`BL_ZERO`


Input Status
~~~~~~~~~~~~

See :class:`bge.types.SCA_PythonKeyboard`, :class:`bge.types.SCA_PythonMouse`, :class:`bge.types.SCA_MouseSensor`, :class:`bge.types.SCA_KeyboardSensor`

:data:`KX_INPUT_NONE`

:data:`KX_INPUT_JUST_ACTIVATED`

:data:`KX_INPUT_ACTIVE`

:data:`KX_INPUT_JUST_RELEASED`


KX_GameObject
~~~~~~~~~~~~~

.. _gameobject-playaction-mode:

See :class:`bge.types.KX_GameObject.playAction`

:data:`KX_ACTION_MODE_PLAY`

:data:`KX_ACTION_MODE_LOOP`

:data:`KX_ACTION_MODE_PING_PONG`

.. _gameobject-playaction-blend:

:data:`KX_ACTION_BLEND_BLEND`

:data:`KX_ACTION_BLEND_ADD`


Mouse Buttons
~~~~~~~~~~~~~

See :class:`bge.types.SCA_MouseSensor`

:data:`KX_MOUSE_BUT_LEFT`

:data:`KX_MOUSE_BUT_MIDDLE`

:data:`KX_MOUSE_BUT_RIGHT`

:data:`KX_MOUSE_BUT_BUTTON4`

:data:`KX_MOUSE_BUT_BUTTON5`

:data:`KX_MOUSE_BUT_BUTTON6`

:data:`KX_MOUSE_BUT_BUTTON7`


Navigation Mesh Draw Modes
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _navmesh-draw-mode:

:data:`RM_WALLS`

:data:`RM_POLYS`

:data:`RM_TRIS`


Shader
~~~~~~

.. _shader-defined-uniform:

:data:`VIEWMATRIX`

:data:`VIEWMATRIX_INVERSE`

:data:`VIEWMATRIX_INVERSETRANSPOSE`

:data:`VIEWMATRIX_TRANSPOSE`

:data:`MODELMATRIX`

:data:`MODELMATRIX_INVERSE`

:data:`MODELMATRIX_INVERSETRANSPOSE`

:data:`MODELMATRIX_TRANSPOSE`

:data:`MODELVIEWMATRIX`

:data:`MODELVIEWMATRIX_INVERSE`

:data:`MODELVIEWMATRIX_INVERSETRANSPOSE`

:data:`MODELVIEWMATRIX_TRANSPOSE`

:data:`CAM_POS`

:data:`CONSTANT_TIMER`

:data:`EYE`

:data:`SHD_TANGENT`


States
~~~~~~

See :class:`bge.types.SCA_StateActuator`

:data:`KX_STATE1`

:data:`KX_STATE2`

:data:`KX_STATE3`

:data:`KX_STATE4`

:data:`KX_STATE5`

:data:`KX_STATE6`

:data:`KX_STATE7`

:data:`KX_STATE8`

:data:`KX_STATE9`

:data:`KX_STATE10`

:data:`KX_STATE11`

:data:`KX_STATE12`

:data:`KX_STATE13`

:data:`KX_STATE14`

:data:`KX_STATE15`

:data:`KX_STATE16`

:data:`KX_STATE17`

:data:`KX_STATE18`

:data:`KX_STATE19`

:data:`KX_STATE20`

:data:`KX_STATE21`

:data:`KX_STATE22`

:data:`KX_STATE23`

:data:`KX_STATE24`

:data:`KX_STATE25`

:data:`KX_STATE26`

:data:`KX_STATE27`

:data:`KX_STATE28`

:data:`KX_STATE29`

:data:`KX_STATE30`

.. _state-actuator-operation:

See :class:`bge.types.SCA_StateActuator.operation`

:data:`KX_STATE_OP_CLR`

:data:`KX_STATE_OP_CPY`

:data:`KX_STATE_OP_NEG`

:data:`KX_STATE_OP_SET`

"""

import typing

import mathutils

import bge

globalDict: typing.Dict[str, typing.Any] = ...

"""

A dictionary that is saved between loading blend files so you can use it to store inventory and other variables you want to store between scenes and blend files.
It can also be written to a file and loaded later on with the game load/save actuators.

Note: only python built in types such as int/string/bool/float/tuples/lists can be saved, GameObjects, Actuators etc will not work as expected.

"""

keyboard: bge.types.SCA_PythonKeyboard = ...

"""

The current keyboard wrapped in an :class:`~bge.types.SCA_PythonKeyboard` object.

"""

mouse: bge.types.SCA_PythonMouse = ...

"""

The current mouse wrapped in an :class:`~bge.types.SCA_PythonMouse` object.

"""

joysticks: typing.List[bge.types.SCA_PythonJoystick] = ...

"""

A list of attached :class:`~bge.types.SCA_PythonJoystick`.
The list size is the maximum number of supported joysticks.
If no joystick is available for a given slot, the slot is set to None.

"""

def getCurrentController() -> bge.types.SCA_PythonController:

  """

  Gets the Python controller associated with this Python script.

  """

  ...

def getCurrentScene() -> bge.types.KX_Scene:

  """

  Gets the current Scene.

  """

  ...

def getSceneList() -> typing.List[bge.types.KX_Scene]:

  """

  Gets a list of the current scenes loaded in the game engine.

  Note: Scenes in your blend file that have not been converted wont be in this list. This list will only contain scenes such as overlays scenes.

  """

  ...

def getInactiveSceneNames() -> typing.List[str]:

  """

  Gets a list of the scene's names not loaded in the game engine.

  """

  ...

def loadGlobalDict() -> None:

  """

  Loads bge.logic.globalDict from a file.

  """

  ...

def saveGlobalDict() -> None:

  """

  Saves bge.logic.globalDict to a file.

  """

  ...

def startGame(blend: str) -> None:

  """

  Loads the blend file.

  """

  ...

def endGame() -> None:

  """

  Ends the current game.

  """

  ...

def restartGame() -> None:

  """

  Restarts the current game by reloading the .blend file (the last saved version, not what is currently running).

  """

  ...

def LibLoad(blend: str, type: str, data: typing.Any, load_actions: bool = False, verbose: bool = False, load_scripts: bool = True, asynchronous: bool = False, scene: typing.Union[bge.types.KX_Scene, str] = None) -> bge.types.KX_LibLoadStatus:

  """

  Converts the all of the datablocks of the given type from the given blend.

  Note: Asynchronously loaded libraries will not be available immediately after LibLoad() returns. Use the returned KX_LibLoadStatus to figure out when the libraries are ready.

  """

  ...

def LibNew(name: str, type: str, data: typing.List[str]) -> None:

  """

  Uses existing datablock data and loads in as a new library.

  """

  ...

def LibFree(name: str) -> None:

  """

  Frees a library, removing all objects and meshes from the currently active scenes.

  """

  ...

def LibList() -> typing.List[str]:

  """

  Returns a list of currently loaded libraries.

  """

  ...

def addScene(name: str, overlay: int = 1) -> None:

  """

  Loads a scene into the game engine.

  Note: This function is not effective immediately, the scene is queued
and added on the next logic cycle where it will be available
from *getSceneList*

  """

  ...

def sendMessage(subject: str, body: str = '', to: str = '', message_from: str = '') -> None:

  """

  Sends a message to sensors in any active scene.

  """

  ...

def setGravity(gravity: mathutils.Vector) -> None:

  """

  Sets the world gravity.

  """

  ...

def getSpectrum() -> typing.List[float]:

  """

  Returns a 512 point list from the sound card.
This only works if the fmod sound driver is being used.

  Deprecated since version 0.2.2.

  """

  ...

def getMaxLogicFrame() -> int:

  """

  Gets the maximum number of logic frames per render frame.

  """

  ...

def setMaxLogicFrame(maxlogic: int) -> None:

  """

  Sets the maximum number of logic frames that are executed per render frame.
This does not affect the physic system that still runs at full frame rate.

  """

  ...

def getMaxPhysicsFrame() -> int:

  """

  Gets the maximum number of physics frames per render frame.

  """

  ...

def setMaxPhysicsFrame(maxphysics: int) -> None:

  """

  Sets the maximum number of physics timestep that are executed per render frame.
Higher value allows physics to keep up with realtime even if graphics slows down the game.
Physics timestep is fixed and equal to 1/tickrate (see setLogicTicRate)
maxphysics/ticrate is the maximum delay of the renderer that physics can compensate.

  """

  ...

def getLogicTicRate() -> float:

  """

  Gets the logic update frequency.

  """

  ...

def setLogicTicRate(ticrate: float) -> None:

  """

  Sets the logic update frequency.

  The logic update frequency is the number of times logic bricks are executed every second.
The default is 60 Hz.

  """

  ...

def getPhysicsTicRate() -> float:

  """

  Gets the physics update frequency

  """

  ...

def setPhysicsTicRate(ticrate: float) -> None:

  """

  Sets the physics update frequency

  The physics update frequency is the number of times the physics system is executed every second.
The default is 60 Hz.

  """

  ...

def getExitKey() -> int:

  """

  Gets the key used to exit the game engine

  """

  ...

def setExitKey(key: int) -> None:

  """

  Sets the key used to exit the game engine

  """

  ...

def NextFrame() -> None:

  """

  Render next frame (if Python has control)

  """

  ...

def setRender(render: bool) -> None:

  """

  Sets the global flag that controls the render of the scene.
If True, the render is done after the logic frame.
If False, the render is skipped and another logic frame starts immediately.

  Note: GPU VSync no longer limits the number of frame per second when render is off,
but the *Use Frame Rate* option still regulates the fps. To run as many frames
as possible, untick this option (Render Properties, System panel).

  """

  ...

def getRender() -> bool:

  """

  Get the current value of the global render flag

  """

  ...

def getClockTime() -> float:

  """

  Get the current BGE render time, in seconds. The BGE render time is the
simulation time corresponding to the next scene that will be rendered.

  """

  ...

def getFrameTime() -> float:

  """

  Get the current BGE frame time, in seconds. The BGE frame time is the
simulation time corresponding to the current call of the logic system.
Generally speaking, it is what the user is interested in.

  """

  ...

def getRealTime() -> float:

  """

  Get the number of real (system-clock) seconds elapsed since the beginning
of the simulation.

  """

  ...

def getTimeScale() -> float:

  """

  Get the time multiplier between real-time and simulation time. The default
value is 1.0. A value greater than 1.0 means that the simulation is going
faster than real-time, a value lower than 1.0 means that the simulation is
going slower than real-time.

  """

  ...

def setTimeScale(time_scale: typing.Any) -> None:

  """

  Set the time multiplier between real-time and simulation time. A value
greater than 1.0 means that the simulation is going faster than real-time,
a value lower than 1.0 means that the simulation is going slower than
real-time. Note that a too large value may lead to some physics
instabilities.

  """

  ...

def getUseExternalClock() -> bool:

  """

  Get if the BGE use the inner BGE clock, or rely or on an external
clock. The default is to use the inner BGE clock.

  """

  ...

def setUseExternalClock(use_external_clock: typing.Any) -> None:

  """

  Set if the BGE use the inner BGE clock, or rely or on an external
clock. If the user selects the use of an external clock, he should call
regularly the setClockTime method.

  """

  ...

def setClockTime(new_time: typing.Any) -> None:

  """

  Set the next value of the simulation clock. It is preferable to use this
method from a custom main function in python, as calling it in the logic
block can easily lead to a blocked system (if the time does not advance
enough to run at least the next logic step).

  """

  ...

def expandPath(path: str) -> str:

  """

  Converts a blender internal path into a proper file system path.

  Use / as directory separator in path
You can use '//' at the start of the string to define a relative path;
Blender replaces that string by the directory of the current .blend or runtime file
to make a full path name. The function also converts the directory separator to
the local file system format.

  """

  ...

def getAverageFrameRate() -> float:

  """

  Gets the estimated/average framerate for all the active scenes, not only the current scene.

  """

  ...

def getBlendFileList(path: str = '//') -> typing.List[typing.Any]:

  """

  Returns a list of blend files in the same directory as the open blend file, or from using the option argument.

  """

  ...

def getRandomFloat() -> None:

  """

  Returns a random floating point value in the range [0 - 1)

  """

  ...

def PrintGLInfo() -> None:

  """

  Prints GL Extension Info into the console

  """

  ...

def getGraphicsCardVendor() -> None:

  """

  Returns the graphics card vendor name. Very useful to make different setups depending on the graphic card used by the user.

  """

  ...

def PrintMemInfo() -> None:

  """

  Prints engine statistics into the console

  """

  ...

def getProfileInfo() -> None:

  """

  Returns a Python dictionary that contains the same information as the on screen profiler. The keys are the profiler categories and the values are tuples with the first element being time taken (in ms) and the second element being the percentage of total time.

  """

  ...

KX_TRUE: typing.Any = ...

"""

True value used by some modules.

"""

KX_FALSE: typing.Any = ...

"""

False value used by some modules.

"""

KX_SENSOR_INACTIVE: typing.Any = ...

KX_SENSOR_JUST_ACTIVATED: typing.Any = ...

KX_SENSOR_ACTIVE: typing.Any = ...

KX_SENSOR_JUST_DEACTIVATED: typing.Any = ...

KX_ARMSENSOR_STATE_CHANGED: typing.Any = ...

"""

Detect that the constraint is changing state (active/inactive)

"""

KX_ARMSENSOR_LIN_ERROR_BELOW: typing.Any = ...

"""

Detect that the constraint linear error is above a threshold

"""

KX_ARMSENSOR_LIN_ERROR_ABOVE: typing.Any = ...

"""

Detect that the constraint linear error is below a threshold

"""

KX_ARMSENSOR_ROT_ERROR_BELOW: typing.Any = ...

"""

Detect that the constraint rotation error is above a threshold

"""

KX_ARMSENSOR_ROT_ERROR_ABOVE: typing.Any = ...

"""

Detect that the constraint rotation error is below a threshold

"""

KX_PROPSENSOR_EQUAL: typing.Any = ...

"""

Activate when the property is equal to the sensor value.

"""

KX_PROPSENSOR_NOTEQUAL: typing.Any = ...

"""

Activate when the property is not equal to the sensor value.

"""

KX_PROPSENSOR_INTERVAL: typing.Any = ...

"""

Activate when the property is between the specified limits.

"""

KX_PROPSENSOR_CHANGED: typing.Any = ...

"""

Activate when the property changes

"""

KX_PROPSENSOR_EXPRESSION: typing.Any = ...

"""

Activate when the expression matches

"""

KX_PROPSENSOR_LESSTHAN: typing.Any = ...

"""

Activate when the property is less than the sensor value

"""

KX_PROPSENSOR_GREATERTHAN: typing.Any = ...

"""

Activate when the property is greater than the sensor value

"""

KX_RADAR_AXIS_POS_X: typing.Any = ...

KX_RADAR_AXIS_POS_Y: typing.Any = ...

KX_RADAR_AXIS_POS_Z: typing.Any = ...

KX_RADAR_AXIS_NEG_X: typing.Any = ...

KX_RADAR_AXIS_NEG_Y: typing.Any = ...

KX_RADAR_AXIS_NEG_Z: typing.Any = ...

KX_RAY_AXIS_POS_X: typing.Any = ...

KX_RAY_AXIS_POS_Y: typing.Any = ...

KX_RAY_AXIS_POS_Z: typing.Any = ...

KX_RAY_AXIS_NEG_X: typing.Any = ...

KX_RAY_AXIS_NEG_Y: typing.Any = ...

KX_RAY_AXIS_NEG_Z: typing.Any = ...

KX_ACTIONACT_PLAY: typing.Any = ...

KX_ACTIONACT_PINGPONG: typing.Any = ...

KX_ACTIONACT_FLIPPER: typing.Any = ...

KX_ACTIONACT_LOOPSTOP: typing.Any = ...

KX_ACTIONACT_LOOPEND: typing.Any = ...

KX_ACTIONACT_PROPERTY: typing.Any = ...

KX_ACT_ARMATURE_RUN: typing.Any = ...

"""

Just make sure the armature will be updated on the next graphic frame.
This is the only persistent mode of the actuator:
it executes automatically once per frame until stopped by a controller

"""

KX_ACT_ARMATURE_ENABLE: typing.Any = ...

"""

Enable the constraint.

"""

KX_ACT_ARMATURE_DISABLE: typing.Any = ...

"""

Disable the constraint (runtime constraint values are not updated).

"""

KX_ACT_ARMATURE_SETTARGET: typing.Any = ...

"""

Change target and subtarget of constraint.

"""

KX_ACT_ARMATURE_SETWEIGHT: typing.Any = ...

"""

Change weight of constraint (IK only).

"""

KX_ACT_ARMATURE_SETINFLUENCE: typing.Any = ...

"""

Change influence of constraint.

"""

KX_CONSTRAINTACT_NORMAL: typing.Any = ...

"""

Activate alignment to surface

"""

KX_CONSTRAINTACT_DISTANCE: typing.Any = ...

"""

Activate distance control

"""

KX_CONSTRAINTACT_LOCAL: typing.Any = ...

"""

Direction of the ray is along the local axis

"""

KX_CONSTRAINTACT_DOROTFH: typing.Any = ...

"""

Force field act on rotation as well

"""

KX_CONSTRAINTACT_MATERIAL: typing.Any = ...

"""

Detect material rather than property

"""

KX_CONSTRAINTACT_PERMANENT: typing.Any = ...

"""

No deactivation if ray does not hit target

"""

KX_CONSTRAINTACT_LOCX: typing.Any = ...

"""

Limit X coord.

"""

KX_CONSTRAINTACT_LOCY: typing.Any = ...

"""

Limit Y coord

"""

KX_CONSTRAINTACT_LOCZ: typing.Any = ...

"""

Limit Z coord

"""

KX_CONSTRAINTACT_ROTX: typing.Any = ...

"""

Limit X rotation

"""

KX_CONSTRAINTACT_ROTY: typing.Any = ...

"""

Limit Y rotation

"""

KX_CONSTRAINTACT_ROTZ: typing.Any = ...

"""

Limit Z rotation

"""

KX_CONSTRAINTACT_DIRNX: typing.Any = ...

"""

Set distance along negative X axis

"""

KX_CONSTRAINTACT_DIRNY: typing.Any = ...

"""

Set distance along negative Y axis

"""

KX_CONSTRAINTACT_DIRNZ: typing.Any = ...

"""

Set distance along negative Z axis

"""

KX_CONSTRAINTACT_DIRPX: typing.Any = ...

"""

Set distance along positive X axis

"""

KX_CONSTRAINTACT_DIRPY: typing.Any = ...

"""

Set distance along positive Y axis

"""

KX_CONSTRAINTACT_DIRPZ: typing.Any = ...

"""

Set distance along positive Z axis

"""

KX_CONSTRAINTACT_ORIX: typing.Any = ...

"""

Set orientation of X axis

"""

KX_CONSTRAINTACT_ORIY: typing.Any = ...

"""

Set orientation of Y axis

"""

KX_CONSTRAINTACT_ORIZ: typing.Any = ...

"""

Set orientation of Z axis

"""

KX_CONSTRAINTACT_FHNX: typing.Any = ...

"""

Set force field along negative X axis

"""

KX_CONSTRAINTACT_FHNY: typing.Any = ...

"""

Set force field along negative Y axis

"""

KX_CONSTRAINTACT_FHNZ: typing.Any = ...

"""

Set force field along negative Z axis

"""

KX_CONSTRAINTACT_FHPX: typing.Any = ...

"""

Set force field along positive X axis

"""

KX_CONSTRAINTACT_FHPY: typing.Any = ...

"""

Set force field along positive Y axis

"""

KX_CONSTRAINTACT_FHPZ: typing.Any = ...

"""

Set force field along positive Z axis

"""

KX_DYN_RESTORE_DYNAMICS: typing.Any = ...

KX_DYN_DISABLE_DYNAMICS: typing.Any = ...

KX_DYN_ENABLE_RIGID_BODY: typing.Any = ...

KX_DYN_DISABLE_RIGID_BODY: typing.Any = ...

KX_DYN_SET_MASS: typing.Any = ...

KX_GAME_LOAD: typing.Any = ...

KX_GAME_START: typing.Any = ...

KX_GAME_RESTART: typing.Any = ...

KX_GAME_QUIT: typing.Any = ...

KX_GAME_SAVECFG: typing.Any = ...

KX_GAME_LOADCFG: typing.Any = ...

KX_ACT_MOUSE_OBJECT_AXIS_X: typing.Any = ...

KX_ACT_MOUSE_OBJECT_AXIS_Y: typing.Any = ...

KX_ACT_MOUSE_OBJECT_AXIS_Z: typing.Any = ...

KX_PARENT_REMOVE: typing.Any = ...

KX_PARENT_SET: typing.Any = ...

KX_RANDOMACT_BOOL_CONST: typing.Any = ...

KX_RANDOMACT_BOOL_UNIFORM: typing.Any = ...

KX_RANDOMACT_BOOL_BERNOUILLI: typing.Any = ...

KX_RANDOMACT_INT_CONST: typing.Any = ...

KX_RANDOMACT_INT_UNIFORM: typing.Any = ...

KX_RANDOMACT_INT_POISSON: typing.Any = ...

KX_RANDOMACT_FLOAT_CONST: typing.Any = ...

KX_RANDOMACT_FLOAT_UNIFORM: typing.Any = ...

KX_RANDOMACT_FLOAT_NORMAL: typing.Any = ...

KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL: typing.Any = ...

KX_SCENE_RESTART: typing.Any = ...

KX_SCENE_SET_SCENE: typing.Any = ...

KX_SCENE_SET_CAMERA: typing.Any = ...

KX_SCENE_ADD_FRONT_SCENE: typing.Any = ...

KX_SCENE_ADD_BACK_SCENE: typing.Any = ...

KX_SCENE_REMOVE_SCENE: typing.Any = ...

KX_SCENE_SUSPEND: typing.Any = ...

KX_SCENE_RESUME: typing.Any = ...

KX_SOUNDACT_PLAYSTOP: typing.Any = ...

KX_SOUNDACT_PLAYEND: typing.Any = ...

KX_SOUNDACT_LOOPSTOP: typing.Any = ...

KX_SOUNDACT_LOOPEND: typing.Any = ...

KX_SOUNDACT_LOOPBIDIRECTIONAL: typing.Any = ...

KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP: typing.Any = ...

KX_STEERING_SEEK: typing.Any = ...

KX_STEERING_FLEE: typing.Any = ...

KX_STEERING_PATHFOLLOWING: typing.Any = ...

KX_TRACK_UPAXIS_POS_X: typing.Any = ...

KX_TRACK_UPAXIS_POS_Y: typing.Any = ...

KX_TRACK_UPAXIS_POS_Z: typing.Any = ...

KX_TRACK_TRAXIS_POS_X: typing.Any = ...

KX_TRACK_TRAXIS_POS_Y: typing.Any = ...

KX_TRACK_TRAXIS_POS_Z: typing.Any = ...

KX_TRACK_TRAXIS_NEG_X: typing.Any = ...

KX_TRACK_TRAXIS_NEG_Y: typing.Any = ...

KX_TRACK_TRAXIS_NEG_Z: typing.Any = ...

RAS_2DFILTER_BLUR: typing.Any = ...

RAS_2DFILTER_CUSTOMFILTER: typing.Any = ...

"""

Customer filter, the code code is set via shaderText property.

"""

RAS_2DFILTER_DILATION: typing.Any = ...

RAS_2DFILTER_DISABLED: typing.Any = ...

"""

Disable the filter that is currently active

"""

RAS_2DFILTER_ENABLED: typing.Any = ...

"""

Enable the filter that was previously disabled

"""

RAS_2DFILTER_EROSION: typing.Any = ...

RAS_2DFILTER_GRAYSCALE: typing.Any = ...

RAS_2DFILTER_INVERT: typing.Any = ...

RAS_2DFILTER_LAPLACIAN: typing.Any = ...

RAS_2DFILTER_MOTIONBLUR: typing.Any = ...

"""

Create and enable preset filters

"""

RAS_2DFILTER_NOFILTER: typing.Any = ...

"""

Disable and destroy the filter that is currently active

"""

RAS_2DFILTER_PREWITT: typing.Any = ...

RAS_2DFILTER_SEPIA: typing.Any = ...

RAS_2DFILTER_SHARPEN: typing.Any = ...

RAS_2DFILTER_SOBEL: typing.Any = ...

ROT_MODE_QUAT: typing.Any = ...

"""

Use quaternion in rotation attribute to update bone rotation.

"""

ROT_MODE_XYZ: typing.Any = ...

"""

Use euler_rotation and apply angles on bone's Z, Y, X axis successively.

"""

ROT_MODE_XZY: typing.Any = ...

"""

Use euler_rotation and apply angles on bone's Y, Z, X axis successively.

"""

ROT_MODE_YXZ: typing.Any = ...

"""

Use euler_rotation and apply angles on bone's Z, X, Y axis successively.

"""

ROT_MODE_YZX: typing.Any = ...

"""

Use euler_rotation and apply angles on bone's X, Z, Y axis successively.

"""

ROT_MODE_ZXY: typing.Any = ...

"""

Use euler_rotation and apply angles on bone's Y, X, Z axis successively.

"""

ROT_MODE_ZYX: typing.Any = ...

"""

Use euler_rotation and apply angles on bone's X, Y, Z axis successively.

"""

CONSTRAINT_TYPE_TRACKTO: typing.Any = ...

CONSTRAINT_TYPE_KINEMATIC: typing.Any = ...

CONSTRAINT_TYPE_ROTLIKE: typing.Any = ...

CONSTRAINT_TYPE_LOCLIKE: typing.Any = ...

CONSTRAINT_TYPE_MINMAX: typing.Any = ...

CONSTRAINT_TYPE_SIZELIKE: typing.Any = ...

CONSTRAINT_TYPE_LOCKTRACK: typing.Any = ...

CONSTRAINT_TYPE_STRETCHTO: typing.Any = ...

CONSTRAINT_TYPE_CLAMPTO: typing.Any = ...

CONSTRAINT_TYPE_TRANSFORM: typing.Any = ...

CONSTRAINT_TYPE_DISTLIMIT: typing.Any = ...

CONSTRAINT_IK_COPYPOSE: typing.Any = ...

"""

constraint is trying to match the position and eventually the rotation of the target.

"""

CONSTRAINT_IK_DISTANCE: typing.Any = ...

"""

Constraint is maintaining a certain distance to target subject to ik_mode

"""

CONSTRAINT_IK_FLAG_TIP: typing.Any = ...

"""

Set when the constraint operates on the head of the bone and not the tail

"""

CONSTRAINT_IK_FLAG_ROT: typing.Any = ...

"""

Set when the constraint tries to match the orientation of the target

"""

CONSTRAINT_IK_FLAG_STRETCH: typing.Any = ...

"""

Set when the armature is allowed to stretch (only the bones with stretch factor > 0.0)

"""

CONSTRAINT_IK_FLAG_POS: typing.Any = ...

"""

Set when the constraint tries to match the position of the target.

"""

CONSTRAINT_IK_MODE_INSIDE: typing.Any = ...

"""

The constraint tries to keep the bone within ik_dist of target

"""

CONSTRAINT_IK_MODE_OUTSIDE: typing.Any = ...

"""

The constraint tries to keep the bone outside ik_dist of the target

"""

CONSTRAINT_IK_MODE_ONSURFACE: typing.Any = ...

"""

The constraint tries to keep the bone exactly at ik_dist of the target.

"""

BL_DST_ALPHA: typing.Any = ...

BL_DST_COLOR: typing.Any = ...

BL_ONE: typing.Any = ...

BL_ONE_MINUS_DST_ALPHA: typing.Any = ...

BL_ONE_MINUS_DST_COLOR: typing.Any = ...

BL_ONE_MINUS_SRC_ALPHA: typing.Any = ...

BL_ONE_MINUS_SRC_COLOR: typing.Any = ...

BL_SRC_ALPHA: typing.Any = ...

BL_SRC_ALPHA_SATURATE: typing.Any = ...

BL_SRC_COLOR: typing.Any = ...

BL_ZERO: typing.Any = ...

KX_INPUT_NONE: typing.Any = ...

KX_INPUT_JUST_ACTIVATED: typing.Any = ...

KX_INPUT_ACTIVE: typing.Any = ...

KX_INPUT_JUST_RELEASED: typing.Any = ...

KX_ACTION_MODE_PLAY: typing.Any = ...

"""

Play the action once.

"""

KX_ACTION_MODE_LOOP: typing.Any = ...

"""

Loop the action (repeat it).

"""

KX_ACTION_MODE_PING_PONG: typing.Any = ...

"""

Play the action one direct then back the other way when it has completed.

"""

KX_ACTION_BLEND_BLEND: typing.Any = ...

"""

Blend layers using linear interpolation

"""

KX_ACTION_BLEND_ADD: typing.Any = ...

"""

Adds the layers together

"""

KX_MOUSE_BUT_LEFT: typing.Any = ...

KX_MOUSE_BUT_MIDDLE: typing.Any = ...

KX_MOUSE_BUT_RIGHT: typing.Any = ...

KX_MOUSE_BUT_BUTTON4: typing.Any = ...

KX_MOUSE_BUT_BUTTON5: typing.Any = ...

KX_MOUSE_BUT_BUTTON6: typing.Any = ...

KX_MOUSE_BUT_BUTTON7: typing.Any = ...

RM_WALLS: typing.Any = ...

"""

Draw only the walls.

"""

RM_POLYS: typing.Any = ...

"""

Draw only polygons.

"""

RM_TRIS: typing.Any = ...

"""

Draw triangle mesh.

"""

VIEWMATRIX: typing.Any = ...

VIEWMATRIX_INVERSE: typing.Any = ...

VIEWMATRIX_INVERSETRANSPOSE: typing.Any = ...

VIEWMATRIX_TRANSPOSE: typing.Any = ...

MODELMATRIX: typing.Any = ...

MODELMATRIX_INVERSE: typing.Any = ...

MODELMATRIX_INVERSETRANSPOSE: typing.Any = ...

MODELMATRIX_TRANSPOSE: typing.Any = ...

MODELVIEWMATRIX: typing.Any = ...

MODELVIEWMATRIX_INVERSE: typing.Any = ...

MODELVIEWMATRIX_INVERSETRANSPOSE: typing.Any = ...

MODELVIEWMATRIX_TRANSPOSE: typing.Any = ...

CAM_POS: typing.Any = ...

"""

Current camera position

"""

CONSTANT_TIMER: typing.Any = ...

EYE: typing.Any = ...

"""

User a timer for the uniform value.

"""

SHD_TANGENT: typing.Any = ...

KX_STATE1: typing.Any = ...

KX_STATE2: typing.Any = ...

KX_STATE3: typing.Any = ...

KX_STATE4: typing.Any = ...

KX_STATE5: typing.Any = ...

KX_STATE6: typing.Any = ...

KX_STATE7: typing.Any = ...

KX_STATE8: typing.Any = ...

KX_STATE9: typing.Any = ...

KX_STATE10: typing.Any = ...

KX_STATE11: typing.Any = ...

KX_STATE12: typing.Any = ...

KX_STATE13: typing.Any = ...

KX_STATE14: typing.Any = ...

KX_STATE15: typing.Any = ...

KX_STATE16: typing.Any = ...

KX_STATE17: typing.Any = ...

KX_STATE18: typing.Any = ...

KX_STATE19: typing.Any = ...

KX_STATE20: typing.Any = ...

KX_STATE21: typing.Any = ...

KX_STATE22: typing.Any = ...

KX_STATE23: typing.Any = ...

KX_STATE24: typing.Any = ...

KX_STATE25: typing.Any = ...

KX_STATE26: typing.Any = ...

KX_STATE27: typing.Any = ...

KX_STATE28: typing.Any = ...

KX_STATE29: typing.Any = ...

KX_STATE30: typing.Any = ...

KX_STATE_OP_CLR: typing.Any = ...

"""

Substract bits to state mask

"""

KX_STATE_OP_CPY: typing.Any = ...

"""

Copy state mask

"""

KX_STATE_OP_NEG: typing.Any = ...

"""

Invert bits to state mask

"""

KX_STATE_OP_SET: typing.Any = ...

"""

Add bits to state mask

"""
