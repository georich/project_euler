# frozen_string_literal: true

sum = 0

(1..999).each do |i|
  sum += i if (i % 5).zero? || (i % 3).zero?
end

puts sum
