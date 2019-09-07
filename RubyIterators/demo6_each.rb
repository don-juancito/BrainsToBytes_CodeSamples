class Array
    def my_each
        counter = 0
        until counter == self.size
            # We will pass into the code block each element of the array, one by one
            yield self[counter]
            counter += 1
        end
        self # Just like the normal each method, we return self at the end
    end
end

test_array = [1, 10, 100, 1000, 10000, 100000]

# This is how we specify the argument passed to the code block
# In this case, we decide to call it 'element', but the names are up to you
test_array.my_each do |element|
    puts "The test array contains the number #{element}"
end