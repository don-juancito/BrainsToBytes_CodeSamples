require_relative 'parent_level_module'
require_relative 'parent_level_module_prepend'

class ParentClass
     include ParentLevelModule
     prepend ParentLevelModulePrepend
    
     def print_greeting
         puts "Hello, I am a method in ParentClass"
     end
end