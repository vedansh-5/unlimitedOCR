<|det|>header [102, 67, 351, 84]<|/det|>Standing on the Shoulders of Giants
<|det|>text [220, 106, 828, 145]<|/det|>The sink and swim methods were inspired by the book Algorithms by Sedgewick and Wayne, Fourth Edition, Section 2.4.
<|det|>text [99, 196, 896, 256]<|/det|>The structure accepts any type that conforms to the Comparable protocol. The single initializer allows you to optionally specify the sorting order and a list of starting values. The default sorting order is descending and the default starting values are an empty collection:
<|det|>text [132, 266, 866, 463]<|/det|>/// Initialization
var priorityQueue = PriorityQueue<String>(ascending: true)

/// Initializing with starting values
priorityQueue = PriorityQueue<String>(ascending: true, startingValues:
["Coldplay", "OneRepublic", "Maroon 5", "Imagine Dragons", "The Script"])

var x = priorityQueue.pop()
/// Coldplay

x = priorityQueue.pop()
/// Imagine Dragons
<|det|>title [101, 501, 259, 526]<|/det|>Protocols
<|det|>text [99, 536, 899, 575]<|/det|>The PriorityQueue conforms to sequence, collection, and IteratorProtocol, so you can treat it like any other Swift sequence and collection:
<|det|>text [133, 587, 738, 733]<|/det|>extension PriorityQueue: IteratorProtocol {
    public typealias Element = T
    mutating public func next() -> Element? { return pop() }
}

extension PriorityQueue: Sequence {
    public typealias Iterator = PriorityQueue
    public func makeIterator() -> Iterator { return self }
}
<|det|>text [99, 748, 867, 788]<|/det|>This allows you to use Swift standard library functions on a PriorityQueue and iterate through a PriorityQueue like this:
<|det|>text [133, 800, 380, 884]<|/det|>for x in priorityQueue {
    print(x)
}

// Coldplay
<|det|>page_number [478, 910, 521, 927]<|/det|>[97]
