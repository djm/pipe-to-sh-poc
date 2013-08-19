pipe-to-sh Proof of Concept
===========================

The problem:

    curl -s <insert_URL_here>/install.sh | sh

Piping direct to sh from the web has its *obvious* dangers along with some
*not so obvious* hidden ones..

This project showcases a non-obvious problem with that workflow by
sniffing the browser's user agent string to change a served .sh file dependent
on whether or not the browser is curl/libcurl. This could allow a malicious
person to point a user to a perfectly reasonable looking .sh file in their
browser, while in the background providing a different, perhaps evil, .sh file
to the user when downloading via [curl/libcurl](http://curl.haxx.se/).

This source [is running on a (sole) heroku worker](http://pipe-to-sh-poc.herokuapp.com)
so you can see for yourself. First visit the URL in a browser, then run the line
below to see what curl would see:

    curl -s http://pipe-to-sh-poc.herokuapp.com/install.sh | cat

N.B Piping to `cat` not `sh`; the file *is* harmless...but why are trusting me?

This is a proof of concept; no damaging code is contained within.

For more on this please see the post on [djm.org.uk](http://www.djm.org.uk/protect-yourself-from-non-obvious-dangers-curl-url-pipe-sh/ "Darian Moody, Python Developer, London").
