require_relative 'rectangle'

class Square < Rectangle
    def set_width(width)
        set_side(width)
    end
    
    def set_height(height)
        set_side(height)
    end
    
    def set_side(side_length)
        @height = side_length
        @width = side_length
    end

end