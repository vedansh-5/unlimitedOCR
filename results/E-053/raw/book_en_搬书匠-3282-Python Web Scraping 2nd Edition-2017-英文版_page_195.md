<|det|>header [102, 67, 264, 84]<|/det|>Putting It All Together
<|det|>text [100, 107, 897, 127]<|/det|>The structure of the search results can be examined with your browser tools, as shown here:
<|det|>image [104, 135, 898, 507]<|/det|>
<|det|>text [99, 508, 880, 547]<|/det|>Here, we see that the search results are structured as links whose parent element is a <h3> tag with class "r".
<|det|>text [99, 560, 899, 598]<|/det|>To scrape the search results, we will use a CSS selector, which was introduced in Chapter 2, Scraping the Data:
<|det|>text [131, 610, 770, 873]<|/det|>>>> from lxml.html import fromstring
>>> import requests
>>> html = requests.get('https://www.google.com/search?q=test')
>>> tree = fromstring(html.content)
>>> results = tree.cssselect('h3.r a')
>>> results
[<Element a at 0x7f3d9affeaf8>,
    <Element a at 0x7f3d9affe890>,
    <Element a at 0x7f3d9affe8e8>,
    <Element a at 0x7f3d9affeaao>,
    <Element a at 0x7f3d9b1a9e68>,
    <Element a at 0x7f3d9b1a9c58>,
    <Element a at 0x7f3d9b1a9ec0>,
    <Element a at 0x7f3d9b1a9f18>,
    <Element a at 0x7f3d9b1a9f70>,
    <Element a at 0x7f3d9b1a9fc8>]
<|det|>page_number [468, 912, 530, 931]<|/det|>[183]
