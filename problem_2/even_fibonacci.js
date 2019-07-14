let initial = 1;
let second = 2;
let result = 0;
let sum;

while (initial < 4000000 && second < 4000000) {
  sum = initial + second;
  initial = second;
  second = sum;

  if (initial % 2 === 0) {
    result += initial;
  }
}

console.log(result);
