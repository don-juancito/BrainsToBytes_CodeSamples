def simplest_yielding_method
    puts "I am at the simplest yielding method, after this, execution will move into the code block"
    yield
    puts "I am back at the simplest yielding method"
 end


simplest_yielding_method do
    puts "Currently executing the code block"
end