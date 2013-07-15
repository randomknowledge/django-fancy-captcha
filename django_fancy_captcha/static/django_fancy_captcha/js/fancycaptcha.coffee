class @Cubes
  constructor: (selector) ->
    @selector = selector
    field_id = '#' + @selector.data 'for'
    if field_id
      @field = $(field_id)
      @cubes = []
      @start()

  start: =>
    @value = []
    @selector.find('.cube3d').each (idx, ele) =>
      c = new Cube(idx, $(ele), @)
      @cubes.push c
      @value.push 0
    if @field.val().match(/^[\d,]+$/)
      values = @field.val().split(',')
      i = 0
      for val in values
        val = parseInt(val, 10)
        @cubes[i].rotate val
        i += 1
    @updateField()

  cubeRotated: (cube) =>
    @value[cube.idx] = cube.value()
    @updateField()

  updateField: =>
    @field.val @value.join(",")

class Cube
  constructor: (idx, selector, parent) ->
    @idx = idx
    @selector = selector
    @rotation = 0
    @parent = parent
    @addEvents()

  addEvents: =>
    @selector.click (event) =>
      @rotate 1

  rotate: (direction) =>
    @rotation += direction * 90
    @updateCss()
    @parent.cubeRotated @

  updateCss: =>
    @setVendorCss @selector, 'transform', "rotateX(#{@rotation}deg)"

  value: =>
    r = @rotation % 360
    if r < 0
      r += 360
    return r / 90

  setVendorCss: (obj, prop, val) ->
    obj.css(prop, val)
    for prefix in ['webkit', 'moz', 'o', 'ms']
      obj.css("-#{prefix}-#{prop}", val)

$ ->
  new Cubes $('.cube3d-container')
