
function palindrome(str) {
  // Good luck!
  var str1 = str.replace(/[^A-Za-z0-9]/g,'').toLowerCase(); // remove all non-alphanumeric characters
  var strArr = str1.split('');
  var reverse = strArr.reverse().join(''); // reverse it
  if (str1==reverse){
  return true;
  }
  return false;
}
palindrome("eye");
