<|det|>header [633, 42, 835, 57]<|/det|>Chapter 1. The Reactive Way • 2
<|det|>text [164, 84, 592, 102]<|/det|>Using RxJS, we would write something like this:
<|det|>text [162, 114, 763, 449]<|/det|>var button = document.getElementById('retrieveDataBtn');
var source1 = Rx.DOM.getJSON('/resource1').pluck('name');
var source2 = Rx.DOM.getJSON('/resource2').pluck('props', 'name');

function getResults(amount) {
    return source1.merge(source2)
    .pluck('names')
    .flatMap(function(array) { return Rx.Observable.from(array); })
    .distinct()
    .take(amount);
}

var clicks = Rx.Observable.fromEvent(button, 'click');
clicks.debug(1000)
    .flatMap(getResults(5))
    .subscribe(
    function(value) { console.log('Received value', value); },
    function(err) { console.error(err); },
    function() { console.log('All values retrieved!'); }
);
<|det|>text [162, 462, 840, 522]<|/det|>Don't worry about understanding what's going on here; let's focus on the 10,000-foot view for now. The first thing you see is that we express more with fewer lines of code. We accomplish this by using Observables.
<|det|>text [161, 534, 840, 636]<|/det|>An Observable represents a stream of data. Programs can be expressed largely as streams of data. In the preceding example, both remote sources are Observables, and so are the mouse clicks from the user. In fact, our program is essentially a single Observable made from a button's click event that we transform to get the results we want.
<|det|>text [161, 648, 840, 793]<|/det|>Reactive programming is expressive. Take, for instance, throttling mouse clicks in our example. Imagine how complex it would be to do that using callbacks or promises: we'd need to reset a timer every second and keep state of whether a second has passed since the last time the user clicked the button. It's a lot of complexity for so little functionality, and the code for it is not even related to your program's actual functionality. In bigger applications, these little complexities add up very quickly to make for a tangled code base.
<|det|>text [161, 804, 840, 886]<|/det|>With the reactive approach, we use the method debounce to throttle the stream of clicks. This ensures that there is at least a second between each click, and discards any clicks in between. We don't care how this happens internally; we just express what we want our code to do, not how to do it.
<|det|>text [161, 897, 839, 937]<|/det|>It gets much more interesting. Next you'll see how reactive programming can help us make our programs more efficient and expressive.
<|det|>footer [838, 984, 970, 995]<|/det|>report erratum • discuss
