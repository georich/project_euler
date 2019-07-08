# frozen_string_literal: true

result = 0

(1..999).each do |x|
  (1..999).each do |y|
    product = x * y
    result = product if product > result && product.to_s == product.to_s.reverse
  end
end

puts result
