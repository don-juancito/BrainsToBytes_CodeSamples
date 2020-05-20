require_relative 'rectangle'
require_relative 'square'

# rectangle = Rectangle.new
# rectangle.set_height(5)
# rectangle.set_width(4)
# raise "Area calculation is off" unless rectangle.get_area == 20

rectangle = Square.new
rectangle.set_height(5)
rectangle.set_width(4)
raise "Area calculation is off" unless rectangle.get_area == 20