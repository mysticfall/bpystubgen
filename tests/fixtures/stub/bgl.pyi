"""


OpenGL Wrapper (bgl)
********************

This module wraps OpenGL constants and functions, making them available from
within Blender Python.

The complete list can be retrieved from the module itself, by listing its
contents: dir(bgl).  A simple search on the web can point to more
than enough material to teach OpenGL programming, from books to many
collections of tutorials.

Here is a comprehensive `list of books <https://www.khronos.org/developers/books/>`_ (non free).
`Learn OpenGL <https://learnopengl.com/>`_ is one of the best resources to learn modern OpenGL and
`opengl-tutorial.org <http://www.opengl-tutorial.org/>`_ offers a set of extensive examples,
including advanced features.

Note: You can use the :class:`bpy.types.Image` type to load and set textures.
See :class:`bpy.types.Image.gl_load` and :class:`bpy.types.Image.gl_free`,
for example.

:func:`glBindTexture`

:func:`glBlendFunc`

:func:`glClear`

:func:`glClearColor`

:func:`glClearDepth`

:func:`glClearStencil`

:func:`glClipPlane`

:func:`glColor`

:func:`glColorMask`

:func:`glCopyTexImage2D`

:func:`glCullFace`

:func:`glDeleteTextures`

:func:`glDepthFunc`

:func:`glDepthMask`

:func:`glDepthRange`

:func:`glDisable`

:func:`glDrawBuffer`

:func:`glEdgeFlag`

:func:`glEnable`

:func:`glEvalCoord`

:func:`glEvalMesh`

:func:`glEvalPoint`

:func:`glFeedbackBuffer`

:func:`glFinish`

:func:`glFlush`

:func:`glFog`

:func:`glFrontFace`

:func:`glGenTextures`

:func:`glGet`

:func:`glGetError`

:func:`glGetLight`

:func:`glGetMap`

:func:`glGetMaterial`

:func:`glGetPixelMap`

:func:`glGetString`

:func:`glGetTexEnv`

:func:`glGetTexGen`

:func:`glGetTexImage`

:func:`glGetTexLevelParameter`

:func:`glGetTexParameter`

:func:`glHint`

:func:`glIsEnabled`

:func:`glIsTexture`

:func:`glLight`

:func:`glLightModel`

:func:`glLineWidth`

:func:`glLoadMatrix`

:func:`glLogicOp`

:func:`glMap1`

:func:`glMap2`

:func:`glMapGrid`

:func:`glMaterial`

:func:`glMultMatrix`

:func:`glNormal3`

:func:`glPixelMap`

:func:`glPixelStore`

:func:`glPixelTransfer`

:func:`glPointSize`

:func:`glPolygonMode`

:func:`glPolygonOffset`

:func:`glRasterPos`

:func:`glReadBuffer`

:func:`glReadPixels`

:func:`glRect`

:func:`glRotate`

:func:`glScale`

:func:`glScissor`

:func:`glStencilFunc`

:func:`glStencilMask`

:func:`glStencilOp`

:func:`glTexCoord`

:func:`glTexEnv`

:func:`glTexGen`

:func:`glTexImage1D`

:func:`glTexImage2D`

:func:`glTexParameter`

:func:`glTranslate`

:func:`glViewport`

:func:`glUseProgram`

:func:`glValidateProgram`

:func:`glLinkProgram`

:func:`glActiveTexture`

:func:`glAttachShader`

:func:`glCompileShader`

:func:`glCreateProgram`

:func:`glCreateShader`

:func:`glDeleteProgram`

:func:`glDeleteShader`

:func:`glDetachShader`

:func:`glGetAttachedShaders`

:func:`glGetProgramInfoLog`

:func:`glGetShaderInfoLog`

:func:`glGetProgramiv`

:func:`glIsShader`

:func:`glIsProgram`

:func:`glGetShaderSource`

:func:`glShaderSource`

:class:`Buffer`

"""

import typing

def glBindTexture(target: typing.Any, texture: int) -> None:

  """

  Bind a named texture to a texturing target

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glBindTexture.xhtml>`_

  """

  ...

def glBlendFunc(sfactor: typing.Any, dfactor: typing.Any) -> None:

  """

  Specify pixel arithmetic

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glBlendFunc.xhtml>`_

  """

  ...

def glClear(mask: typing.Any) -> None:

  """

  Clear buffers to preset values

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glClear.xhtml>`_

  """

  ...

def glClearColor(red: typing.Any, green: typing.Any, blue: typing.Any, alpha: typing.Any) -> None:

  """

  Specify clear values for the color buffers

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glClearColor.xhtml>`_

  """

  ...

def glClearDepth(depth: int) -> None:

  """

  Specify the clear value for the depth buffer

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glClearDepth.xhtml>`_

  """

  ...

def glClearStencil(s: int) -> None:

  """

  Specify the clear value for the stencil buffer

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glClearStencil.xhtml>`_

  """

  ...

def glClipPlane(plane: typing.Any, equation: Buffer) -> None:

  """

  Specify a plane against which all geometry is clipped

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glClipPlane.xhtml>`_

  """

  ...

def glColor(red: typing.Any, green: typing.Any, blue: typing.Any, alpha: typing.Any) -> None:

  """

  B{glColor3b, glColor3d, glColor3f, glColor3i, glColor3s, glColor3ub, glColor3ui, glColor3us,
glColor4b, glColor4d, glColor4f, glColor4i, glColor4s, glColor4ub, glColor4ui, glColor4us,
glColor3bv, glColor3dv, glColor3fv, glColor3iv, glColor3sv, glColor3ubv, glColor3uiv,
glColor3usv, glColor4bv, glColor4dv, glColor4fv, glColor4iv, glColor4sv, glColor4ubv,
glColor4uiv, glColor4usv}

  Set a new color.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glColor.xhtml>`_

  """

  ...

def glColorMask(red: typing.Any, green: typing.Any, blue: typing.Any, alpha: typing.Any) -> None:

  """

  Enable and disable writing of frame buffer color components

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glColorMask.xhtml>`_

  """

  ...

def glCopyTexImage2D(target: typing.Any, level: int, internalformat: int, x: typing.Any, y: typing.Any, width: int, height: int, border: int) -> None:

  """

  Copy pixels into a 2D texture image

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glCopyTexImage2D.xhtml>`_

  """

  ...

def glCullFace(mode: typing.Any) -> None:

  """

  Specify whether front- or back-facing facets can be culled

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glCullFace.xhtml>`_

  """

  ...

def glDeleteTextures(n: int, textures: Buffer) -> None:

  """

  Delete named textures

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteTextures.xhtml>`_

  """

  ...

def glDepthFunc(func: typing.Any) -> None:

  """

  Specify the value used for depth buffer comparisons

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthFunc.xhtml>`_

  """

  ...

def glDepthMask(flag: int) -> None:

  """

  Enable or disable writing into the depth buffer

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthMask.xhtml>`_

  """

  ...

def glDepthRange(zNear: int, zFar: int) -> None:

  """

  Specify mapping of depth values from normalized device coordinates to window coordinates

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDepthRange.xhtml>`_

  """

  ...

def glDisable(cap: typing.Any) -> None:

  """

  Disable server-side GL capabilities

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEnable.xhtml>`_

  """

  ...

def glDrawBuffer(mode: typing.Any) -> None:

  """

  Specify which color buffers are to be drawn into

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDrawBuffer.xhtml>`_

  """

  ...

def glEdgeFlag(flag: typing.Any) -> None:

  """

  B{glEdgeFlag, glEdgeFlagv}

  Flag edges as either boundary or non-boundary

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEdgeFlag.xhtml>`_

  """

  ...

def glEnable(cap: typing.Any) -> None:

  """

  Enable server-side GL capabilities

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEnable.xhtml>`_

  """

  ...

def glEvalCoord(u: typing.Any, v: typing.Any) -> None:

  """

  B{glEvalCoord1d, glEvalCoord1f, glEvalCoord2d, glEvalCoord2f, glEvalCoord1dv, glEvalCoord1fv,
glEvalCoord2dv, glEvalCoord2fv}

  Evaluate enabled one- and two-dimensional maps

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEvalCoord.xhtml>`_

  """

  ...

def glEvalMesh(mode: typing.Any, i1: typing.Any, i2: typing.Any) -> None:

  """

  B{glEvalMesh1 or glEvalMesh2}

  Compute a one- or two-dimensional grid of points or lines

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEvalMesh.xhtml>`_

  """

  ...

def glEvalPoint(i: int, j: int) -> None:

  """

  B{glEvalPoint1 and glEvalPoint2}

  Generate and evaluate a single point in a mesh

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glEvalPoint.xhtml>`_

  """

  ...

def glFeedbackBuffer(size: int, type: typing.Any, buffer: Buffer) -> None:

  """

  Controls feedback mode

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glFeedbackBuffer.xhtml>`_

  """

  ...

def glFinish() -> None:

  """

  Block until all GL execution is complete

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glFinish.xhtml>`_

  """

  ...

def glFlush() -> None:

  """

  Force Execution of GL commands in finite time

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glFlush.xhtml>`_

  """

  ...

def glFog(pname: typing.Any, param: typing.Any) -> None:

  """

  B{glFogf, glFogi, glFogfv, glFogiv}

  Specify fog parameters

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glFog.xhtml>`_

  """

  ...

def glFrontFace(mode: typing.Any) -> None:

  """

  Define front- and back-facing polygons

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glFrontFace.xhtml>`_

  """

  ...

def glGenTextures(n: int, textures: Buffer) -> None:

  """

  Generate texture names

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGenTextures.xhtml>`_

  """

  ...

def glGet(pname: typing.Any, param: typing.Any) -> None:

  """

  B{glGetBooleanv, glGetfloatv, glGetFloatv, glGetIntegerv}

  Return the value or values of a selected parameter

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGet.xhtml>`_

  """

  ...

def glGetError() -> None:

  """

  Return error information

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetError.xhtml>`_

  """

  ...

def glGetLight(light: typing.Any, pname: typing.Any, params: Buffer) -> None:

  """

  B{glGetLightfv and glGetLightiv}

  Return light source parameter values

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetLight.xhtml>`_

  """

  ...

def glGetMap(target: typing.Any, query: typing.Any, v: Buffer) -> None:

  """

  B{glGetMapdv, glGetMapfv, glGetMapiv}

  Return evaluator parameters

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetMap.xhtml>`_

  """

  ...

def glGetMaterial(face: typing.Any, pname: typing.Any, params: Buffer) -> None:

  """

  B{glGetMaterialfv, glGetMaterialiv}

  Return material parameters

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetMaterial.xhtml>`_

  """

  ...

def glGetPixelMap(map: typing.Any, values: Buffer) -> None:

  """

  B{glGetPixelMapfv, glGetPixelMapuiv, glGetPixelMapusv}

  Return the specified pixel map

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetPixelMap.xhtml>`_

  """

  ...

def glGetString(name: typing.Any) -> None:

  """

  Return a string describing the current GL connection

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetString.xhtml>`_

  """

  ...

def glGetTexEnv(target: typing.Any, pname: typing.Any, params: Buffer) -> None:

  """

  B{glGetTexEnvfv, glGetTexEnviv}

  Return texture environment parameters

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexEnv.xhtml>`_

  """

  ...

def glGetTexGen(coord: typing.Any, pname: typing.Any, params: Buffer) -> None:

  """

  B{glGetTexGendv, glGetTexGenfv, glGetTexGeniv}

  Return texture coordinate generation parameters

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexGen.xhtml>`_

  """

  ...

def glGetTexImage(target: typing.Any, level: int, format: typing.Any, type: typing.Any, pixels: Buffer) -> None:

  """

  Return a texture image

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexImage.xhtml>`_

  """

  ...

def glGetTexLevelParameter(target: typing.Any, level: int, pname: typing.Any, params: Buffer) -> None:

  """

  B{glGetTexLevelParameterfv, glGetTexLevelParameteriv}

  return texture parameter values for a specific level of detail

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexLevelParameter.xhtml>`_

  """

  ...

def glGetTexParameter(target: typing.Any, pname: typing.Any, params: Buffer) -> None:

  """

  B{glGetTexParameterfv, glGetTexParameteriv}

  Return texture parameter values

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetTexParameter.xhtml>`_

  """

  ...

def glHint(target: typing.Any, mode: typing.Any) -> None:

  """

  Specify implementation-specific hints

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glHint.xhtml>`_

  """

  ...

def glIsEnabled(cap: typing.Any) -> None:

  """

  Test whether a capability is enabled

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glIsEnabled.xhtml>`_

  """

  ...

def glIsTexture(texture: int) -> None:

  """

  Determine if a name corresponds to a texture

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glIsTexture.xhtml>`_

  """

  ...

def glLight(light: typing.Any, pname: typing.Any, param: typing.Any) -> None:

  """

  B{glLightf,glLighti, glLightfv, glLightiv}

  Set the light source parameters

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLight.xhtml>`_

  """

  ...

def glLightModel(pname: typing.Any, param: typing.Any) -> None:

  """

  B{glLightModelf, glLightModeli, glLightModelfv, glLightModeliv}

  Set the lighting model parameters

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLightModel.xhtml>`_

  """

  ...

def glLineWidth(width: float) -> None:

  """

  Specify the width of rasterized lines.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLineWidth.xhtml>`_

  """

  ...

def glLoadMatrix(m: Buffer) -> None:

  """

  B{glLoadMatrixd, glLoadMatixf}

  Replace the current matrix with the specified matrix

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLoadMatrix.xhtml>`_

  """

  ...

def glLogicOp(opcode: typing.Any) -> None:

  """

  Specify a logical pixel operation for color index rendering

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLogicOp.xhtml>`_

  """

  ...

def glMap1(target: typing.Any, u1: typing.Any, u2: typing.Any, stride: int, order: int, points: Buffer) -> None:

  """

  B{glMap1d, glMap1f}

  Define a one-dimensional evaluator

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glMap1.xhtml>`_

  """

  ...

def glMap2(target: typing.Any, u1: typing.Any, u2: typing.Any, ustride: int, uorder: int, v1: typing.Any, v2: typing.Any, vstride: int, vorder: int, points: Buffer) -> None:

  """

  B{glMap2d, glMap2f}

  Define a two-dimensional evaluator

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glMap2.xhtml>`_

  """

  ...

def glMapGrid(un: int, u1: typing.Any, u2: typing.Any, vn: int, v1: typing.Any, v2: typing.Any) -> None:

  """

  B{glMapGrid1d, glMapGrid1f, glMapGrid2d, glMapGrid2f}

  Define a one- or two-dimensional mesh

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glMapGrid.xhtml>`_

  """

  ...

def glMaterial(face: typing.Any, pname: typing.Any, params: int) -> None:

  """

  Specify material parameters for the lighting model.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glMaterial.xhtml>`_

  """

  ...

def glMultMatrix(m: Buffer) -> None:

  """

  B{glMultMatrixd, glMultMatrixf}

  Multiply the current matrix with the specified matrix

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glMultMatrix.xhtml>`_

  """

  ...

def glNormal3(nx: typing.Any, ny: typing.Any, nz: typing.Any, v: Buffer) -> None:

  """

  B{Normal3b, Normal3bv, Normal3d, Normal3dv, Normal3f, Normal3fv, Normal3i, Normal3iv,
Normal3s, Normal3sv}

  Set the current normal vector

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glNormal.xhtml>`_

  """

  ...

def glPixelMap(map: typing.Any, mapsize: int, values: Buffer) -> None:

  """

  B{glPixelMapfv, glPixelMapuiv, glPixelMapusv}

  Set up pixel transfer maps

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPixelMap.xhtml>`_

  """

  ...

def glPixelStore(pname: typing.Any, param: typing.Any) -> None:

  """

  B{glPixelStoref, glPixelStorei}

  Set pixel storage modes

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPixelStore.xhtml>`_

  """

  ...

def glPixelTransfer(pname: typing.Any, param: typing.Any) -> None:

  """

  B{glPixelTransferf, glPixelTransferi}

  Set pixel transfer modes

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPixelTransfer.xhtml>`_

  """

  ...

def glPointSize(size: float) -> None:

  """

  Specify the diameter of rasterized points

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPointSize.xhtml>`_

  """

  ...

def glPolygonMode(face: typing.Any, mode: typing.Any) -> None:

  """

  Select a polygon rasterization mode

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPolygonMode.xhtml>`_

  """

  ...

def glPolygonOffset(factor: float, units: float) -> None:

  """

  Set the scale and units used to calculate depth values

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glPolygonOffset.xhtml>`_

  """

  ...

def glRasterPos(x: typing.Any, y: typing.Any, z: typing.Any, w: typing.Any) -> None:

  """

  B{glRasterPos2d, glRasterPos2f, glRasterPos2i, glRasterPos2s, glRasterPos3d,
glRasterPos3f, glRasterPos3i, glRasterPos3s, glRasterPos4d, glRasterPos4f,
glRasterPos4i, glRasterPos4s, glRasterPos2dv, glRasterPos2fv, glRasterPos2iv,
glRasterPos2sv, glRasterPos3dv, glRasterPos3fv, glRasterPos3iv, glRasterPos3sv,
glRasterPos4dv, glRasterPos4fv, glRasterPos4iv, glRasterPos4sv}

  Specify the raster position for pixel operations

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glRasterPos.xhtml>`_

  Note: If you are drawing to the 3d view with a Scriptlink of a space handler
the zoom level of the panels will scale the glRasterPos by the view matrix.
so a X of 10 will not always offset 10 pixels as you would expect.To work around this get the scale value of the view matrix and use it to scale your pixel values.

    .. code:: python

      import bgl
      xval, yval= 100, 40
      # Get the scale of the view matrix
      view_matrix = bgl.Buffer(bgl.GL_FLOAT, 16)
      bgl.glGetFloatv(bgl.GL_MODELVIEW_MATRIX, view_matrix)
      f = 1.0 / view_matrix[0]

      # Instead of the usual glRasterPos2i(xval, yval)
      bgl.glRasterPos2f(xval * f, yval * f)

  """

  ...

def glReadBuffer(mode: typing.Any) -> None:

  """

  Select a color buffer source for pixels.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glReadBuffer.xhtml>`_

  """

  ...

def glReadPixels(x: typing.Any, y: typing.Any, width: typing.Any, height: typing.Any, format: typing.Any, type: typing.Any, pixels: Buffer) -> None:

  """

  Read a block of pixels from the frame buffer

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glReadPixels.xhtml>`_

  """

  ...

def glRect(x1: typing.Any, y1: typing.Any, x2: typing.Any, y2: typing.Any, v1: typing.Any, v2: typing.Any) -> None:

  """

  B{glRectd, glRectf, glRecti, glRects, glRectdv, glRectfv, glRectiv, glRectsv}

  Draw a rectangle

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glRect.xhtml>`_

  """

  ...

def glRotate(angle: typing.Any, x: typing.Any, y: typing.Any, z: typing.Any) -> None:

  """

  B{glRotated, glRotatef}

  Multiply the current matrix by a rotation matrix

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glRotate.xhtml>`_

  """

  ...

def glScale(x: typing.Any, y: typing.Any, z: typing.Any) -> None:

  """

  B{glScaled, glScalef}

  Multiply the current matrix by a general scaling matrix

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glScale.xhtml>`_

  """

  ...

def glScissor(x: typing.Any, y: typing.Any, width: typing.Any, height: typing.Any) -> None:

  """

  Define the scissor box

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glScissor.xhtml>`_

  """

  ...

def glStencilFunc(func: typing.Any, ref: int, mask: int) -> None:

  """

  Set function and reference value for stencil testing

  `OpenGL Docs <https://www.opengl.org/sdk/docs/man/docbook4/xhtml/glStencilFunc.xhtml>`_

  """

  ...

def glStencilMask(mask: int) -> None:

  """

  Control the writing of individual bits in the stencil planes

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glStencilMask.xhtml>`_

  """

  ...

def glStencilOp(fail: typing.Any, zfail: typing.Any, zpass: typing.Any) -> None:

  """

  Set stencil test actions

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glStencilOp.xhtml>`_

  """

  ...

def glTexCoord(s: typing.Any, t: typing.Any, r: typing.Any, q: typing.Any, v: Buffer) -> None:

  """

  B{glTexCoord1d, glTexCoord1f, glTexCoord1i, glTexCoord1s, glTexCoord2d, glTexCoord2f,
glTexCoord2i, glTexCoord2s, glTexCoord3d, glTexCoord3f, glTexCoord3i, glTexCoord3s,
glTexCoord4d, glTexCoord4f, glTexCoord4i, glTexCoord4s, glTexCoord1dv, glTexCoord1fv,
glTexCoord1iv, glTexCoord1sv, glTexCoord2dv, glTexCoord2fv, glTexCoord2iv,
glTexCoord2sv, glTexCoord3dv, glTexCoord3fv, glTexCoord3iv, glTexCoord3sv,
glTexCoord4dv, glTexCoord4fv, glTexCoord4iv, glTexCoord4sv}

  Set the current texture coordinates

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexCoord.xhtml>`_

  """

  ...

def glTexEnv(target: typing.Any, pname: typing.Any, param: typing.Any) -> None:

  """

  B{glTextEnvf, glTextEnvi, glTextEnvfv, glTextEnviv}

  Set texture environment parameters

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexEnv.xhtml>`_

  """

  ...

def glTexGen(coord: typing.Any, pname: typing.Any, param: typing.Any) -> None:

  """

  B{glTexGend, glTexGenf, glTexGeni, glTexGendv, glTexGenfv, glTexGeniv}

  Control the generation of texture coordinates

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexGen.xhtml>`_

  """

  ...

def glTexImage1D(target: typing.Any, level: int, internalformat: int, width: int, border: int, format: typing.Any, type: typing.Any, pixels: Buffer) -> None:

  """

  Specify a one-dimensional texture image

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexImage1D.xhtml>`_

  """

  ...

def glTexImage2D(target: typing.Any, level: int, internalformat: int, width: int, height: int, border: int, format: typing.Any, type: typing.Any, pixels: Buffer) -> None:

  """

  Specify a two-dimensional texture image

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexImage2D.xhtml>`_

  """

  ...

def glTexParameter(target: typing.Any, pname: typing.Any, param: typing.Any) -> None:

  """

  B{glTexParameterf, glTexParameteri, glTexParameterfv, glTexParameteriv}

  Set texture parameters

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTexParameter.xhtml>`_

  """

  ...

def glTranslate(x: typing.Any, y: typing.Any, z: typing.Any) -> None:

  """

  B{glTranslatef, glTranslated}

  Multiply the current matrix by a translation matrix

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glTranslate.xhtml>`_

  """

  ...

def glViewport(x: typing.Any, y: typing.Any, width: typing.Any, height: typing.Any) -> None:

  """

  Set the viewport

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glViewport.xhtml>`_

  """

  ...

def glUseProgram(program: int) -> None:

  """

  Installs a program object as part of current rendering state

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glUseProgram.xhtml>`_

  """

  ...

def glValidateProgram(program: int) -> None:

  """

  Validates a program object

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glValidateProgram.xhtml>`_

  """

  ...

def glLinkProgram(program: int) -> None:

  """

  Links a program object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glLinkProgram.xhtml>`_

  """

  ...

def glActiveTexture(texture: int) -> None:

  """

  Select active texture unit.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glActiveTexture.xhtml>`_

  """

  ...

def glAttachShader(program: int, shader: int) -> None:

  """

  Attaches a shader object to a program object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glAttachShader.xhtml>`_

  """

  ...

def glCompileShader(shader: int) -> None:

  """

  Compiles a shader object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glCompileShader.xhtml>`_

  """

  ...

def glCreateProgram() -> int:

  """

  Creates a program object

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateProgram.xhtml>`_

  """

  ...

def glCreateShader(shaderType: typing.Any) -> int:

  """

  Creates a shader object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glCreateShader.xhtml>`_

  """

  ...

def glDeleteProgram(program: int) -> None:

  """

  Deletes a program object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteProgram.xhtml>`_

  """

  ...

def glDeleteShader(shader: int) -> None:

  """

  Deletes a shader object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDeleteShader.xhtml>`_

  """

  ...

def glDetachShader(program: int, shader: int) -> None:

  """

  Detaches a shader object from a program object to which it is attached.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glDetachShader.xhtml>`_

  """

  ...

def glGetAttachedShaders(program: int, maxCount: int, count: Buffer, shaders: Buffer) -> None:

  """

  Returns the handles of the shader objects attached to a program object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetAttachedShaders.xhtml>`_

  """

  ...

def glGetProgramInfoLog(program: int, maxLength: int, length: Buffer, infoLog: Buffer) -> None:

  """

  Returns the information log for a program object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgramInfoLog.xhtml>`_

  """

  ...

def glGetShaderInfoLog(program: typing.Any, maxLength: int, length: Buffer, infoLog: Buffer) -> None:

  """

  Returns the information log for a shader object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetShaderInfoLog.xhtml>`_

  """

  ...

def glGetProgramiv(program: int, pname: int, params: Buffer) -> None:

  """

  Returns a parameter from a program object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetProgram.xhtml>`_

  """

  ...

def glIsShader(shader: int) -> None:

  """

  Determines if a name corresponds to a shader object.

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glIsShader.xhtml>`_

  """

  ...

def glIsProgram(program: int) -> None:

  """

  Determines if a name corresponds to a program object

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glIsProgram.xhtml>`_

  """

  ...

def glGetShaderSource(shader: int, bufSize: int, length: Buffer, source: Buffer) -> None:

  """

  Returns the source code string from a shader object

  `OpenGL Docs <https://khronos.org/registry/OpenGL-Refpages/gl4/html/glGetShaderSource.xhtml>`_

  """

  ...

def glShaderSource(shader: int, shader_string: str) -> None:

  """

  Replaces the source code in a shader object.

  `OpenGL Docs <https://www.opengl.org/sdk/docs/man/html/glShaderSource.xhtml>`_

  """

  ...

class Buffer:

  """

  The Buffer object is simply a block of memory that is delineated and initialized by the
user. Many OpenGL functions return data to a C-style pointer, however, because this
is not possible in python the Buffer object can be used to this end. Wherever pointer
notation is used in the OpenGL functions the Buffer object can be used in it's bgl
wrapper. In some instances the Buffer object will need to be initialized with the template
parameter, while in other instances the user will want to create just a blank buffer
which will be zeroed by default.

  .. code:: python

    import bgl

    myByteBuffer = bgl.Buffer(bgl.GL_BYTE, [32, 32])
    bgl.glGetPolygonStipple(myByteBuffer)

    print(myByteBuffer.dimensions)
    print(myByteBuffer.to_list())

    sliceBuffer = myByteBuffer[0:16]
    print(sliceBuffer)

  """

  dimensions: typing.Any = ...

  """

  The number of dimensions of the Buffer.

  """

  def to_list(self) -> None:

    """

    The contents of the Buffer as a python list.

    """

    ...

  def __init__(self, type: int, dimensions: typing.Any, template: typing.Any = None) -> typing.Any:

    """

    This will create a new Buffer object for use with other bgl OpenGL commands.
Only the type of argument to store in the buffer and the dimensions of the buffer
are necessary. Buffers are zeroed by default unless a template is supplied, in
which case the buffer is initialized to the template.

    """

    ...
