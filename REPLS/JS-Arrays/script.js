//This function is called when the "Run Function" button is pressed
function usingArrays()
{ 
    var favoriteFood = ["Pizza", "Meatballs", "Tacos"]
    console.log(favoriteFood)
    console.log(favoriteFood.toString())
    var length = favoriteFood.length;

    for (var i = 0; i < length; i++) {
        console.log("index " + i + ": " + favoriteFood[i]);
    }
    var indexOfPizza = indexOf("Pizza")
    console.log("index of Pizza " + indexOfPizza)
}