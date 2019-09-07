class Array
    def my_mapper
        mapped_array = []
        counter = 0

        until counter == self.size
            mapped_value = yield self[counter]
            mapped_array.push(mapped_value)
            counter += 1
        end
        # we want to return the mapped array in the end
        mapped_array
    end
end

test_array = [1,2,3,4,5,6,7,8,9]

# Let's generate an array with the squares of test_array

squares =   test_array.my_mapper do |element|
                element * element
            end

puts squares