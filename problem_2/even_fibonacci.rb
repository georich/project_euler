# frozen_string_literal: true

first = 1
second = 2
sum = 0

begin
  new = first + second
  first = second
  second = new

  sum += first if (first % 2).zero?
end while (first < 4000000 and second < 4000000)

puts sum
