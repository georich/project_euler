# frozen_string_literal: true

def prime?(factor)
  (factor - 2...1).step(-2).each do |x|
    return false if (factor % x).zero?
  end
  true
end

def largest_prime_factor(target)
  primes = []
  (3..Integer.sqrt(target)).step(2).each do |i|
    if (target % i).zero?
      primes.push(i) if prime?(i)
    end
  end
  primes.pop
end

number = 600_851_475_143
puts "The largets prime factor of #{number} is #{largest_prime_factor(number)}"
