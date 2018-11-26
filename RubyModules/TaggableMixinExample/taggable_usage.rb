require_relative 'post'
require_relative 'quotes'

first_post = Post.new('This is an article on how to use ruby modules', 'Juan Orozco Villalobos')
first_post.add_tag('Software development')
first_post.add_tag('Ruby programming')
first_post.add_tag('Programming languages')

first_post.print_post_summary
puts "We have a total of #{first_post.tag_count} tags"


quotes = Quotes.new
quotes.add_tag('bullshit')
quotes.add_tag('pseudointellectual ')

quotes.add_quote('Wholeness unfolds through species specific marvel')
quotes.add_quote('The mind creates spontaneous happiness')
quotes.add_quote('The ego is an ingredient of the flow of balance')
quotes.add_quote('Perception fears karmic success')

quotes.print_all_quotes