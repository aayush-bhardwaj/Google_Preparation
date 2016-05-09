
function findLongestWord(str) {
  var newArr = str.split(' ');
  var lenArr=[];
  for (var i=0;i<newArr.length ; i++){
    lenArr.push(newArr[i].length);
  }
  lenArr.sort(function(a,b){
    return b-a;
  });
  return lenArr[0];
}

findLongestWord("The quick brown fox jumped over the lazy dog");
