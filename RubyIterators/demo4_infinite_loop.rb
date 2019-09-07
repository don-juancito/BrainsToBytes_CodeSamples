def infinite_loop
    while true
        yield
    end
end

infinite_loop do
    puts "This message will appear infinite times"
end