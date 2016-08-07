# Anonymous-browser
We present Anonymous Browser, a Facebook application that increases the anonymity of a user's
browser by reducing its 'device fingerprinting' that is transmitted to websites, via the version and
configuration information, upon request. This fingerprint of the user's web browser can be
used to track it (associating activities of browser at different times and with different websites
) on the Internet. When you visit a website, you are allowing that site to access a lot of
information about your browser's version and configuration information. When combined with
other information like IP address etc., this information can create a kind of signature that could
be used to identify your computer. The Electronic Frontier Foundation (EFF) made a test side,
panopticlick.eff.org, where they observed user traffic for analyzing their browser’s fingerprints.
As an outcome to their efforts, they got a distribution of user fingerprint containing at
least 18.1 bits of entropy, meaning that if you pick a browser at random, at best you expect that
only one in 286,777 (more than 218) other browsers will share its fingerprint. Among browsers
that support Flash or Java, the situation was worse, with the average browser carrying at least
18.8 bits of identifying information. 94.2 % of browsers with Flash or Java were unique in their
(EFF’s) collected samples. So keeping this all into mind we are developing our project
“Anonymous Browser”, which will try and implement a strategy for making the 'device
fingerprint' of a user's browser more anonymous in a distributed environment.
