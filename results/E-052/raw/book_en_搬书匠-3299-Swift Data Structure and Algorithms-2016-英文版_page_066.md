<|det|>header [102, 67, 430, 84]<|/det|>Working with Commonly Used Data Structures
<|det|>title [100, 109, 582, 143]<|/det|>Implementing subscripting
<|det|>text [99, 147, 868, 225]<|/det|>Subscripts can be defined for classes, structures, and enumerations. They are used to provide a shortcut to elements in collections, lists, and sequence types by allowing terser syntax. They can be used to set and get elements by specifying an index instead of using separate methods to set or retrieve values.
<|det|>title [100, 262, 377, 293]<|/det|>Subscript syntax
<|det|>text [99, 298, 875, 375]<|/det|>You can define a subscript that accepts one or more input parameters, the parameters can be of different types, and their return value can be of any type. Use the subscript keyword to define a subscript, which can be defined as read-only, or provide a getter and setter to access elements:
<|det|>text [130, 386, 812, 729]<|/det|>class MovieList {
    private var tracks = ["The Godfather", "The Dark Knight", "Pulp Fiction"]
    subscript(index: Int) -> String {
    get {
    return self.tracks[index]
    }
    set {
    self.tracks[index] = newValue
    }
    }
}

var movieList = MovieList()

var aMovie = movieList[0]
// The Godfather

movieList[1] = "Forest Gump"
aMovie = movieList[1]
// Forest Gump
<|det|>title [100, 767, 391, 798]<|/det|>Subscript options
<|det|>text [99, 802, 886, 860]<|/det|>Classes and structures can return as many subscript implementations as needed. The support for multiple subscripts is known as subscript overloading, the correct subscript to be used will be inferred based on the subscript value types.
<|det|>page_number [478, 910, 521, 927]<|/det|>[52]
