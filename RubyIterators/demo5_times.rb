class Integer
    def run_times
        counter = 0
        until counter == self
            yield
            counter += 1
        end
    end
end

5.run_times do
    puts "This message will appear exactly 5 times"
end