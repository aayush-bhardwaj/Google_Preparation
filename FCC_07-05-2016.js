//Regukar Expression .

var testString = "Ada Lovelace and Charles Babbage designed the first computer and the software that would have run on it.";

var expressionToGetSoftware = /software/gi;
var softwareCount = testString.match(expressionToGetSoftware).length;

var expression = /and/gi;  // Change this Line

var andCount = testString.match(expression).length;


//Constructor Functions 

var Bike = function() {
  var gear;
  
  this.getGear = function(){
    return gear;
  };
  
  this.setGear = function(change){
    gear = change;
  };
};
var myBike = new Bike();

