function isPalindrome(number) {
  const str = `${number}`;
  for (let i = 0; i < str.length; i++) {
    if (str[i] != str[str.length - 1 - i]) {
      return false;
    }
  }
  return true;
}

const tests = [121, 122, 66, 1991, 1];
for (let test of tests) {
  console.log(`${test}: ${isPalindrome(test)}`);
}

