require_relative 'parent_class'
require_relative 'child_level_module'
require_relative 'child_level_module_prepend'

class ChildClass < ParentClass
    include ChildLevelModule
    prepend ChildLevelModulePrepend
    
    def print_greeting
        puts "Hello, I am a method in ChildClass"
    end
end