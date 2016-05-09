
function reverseString(str) {
  str1 = str.split(''); // convert a string to an array
  return str1.reverse().join(''); // reverse the array and convert into a string
}

reverseString("hello");
