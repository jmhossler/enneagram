# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

questions = Array.new

File.open('questions.txt', 'r') do |f|
  f.each_line do |line|
    questions << line.split('|')
  end
end

questions.each do |question, ans1, ans2|
  Question.create(test: question, ans1: ans1, ans2: ans2)
end
