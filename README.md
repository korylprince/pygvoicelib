pygvoicelib

https://github.com/korylprince/pygvoicelib

#History#

I searched long and hard for a python library that could interface with Google Voice **and** work with Two-Factor authentication.

I finally stumbled upon pygvoicelib: http://code.google.com/p/pygvoicelib/ , an excellent library that works by using an application-specific password.

However it did not come with sms support, which I required. Therefore I modified the code and added an auxilary script. I publish this modification here for others to use. Credit for this work goes to Ehsan Foroughi.

The code works very well, and the service is very reliable as long as you don't attempt to send too many texts close together.

#Installing#

Copy the code to where ever you want to run it from. Included is the simplejson library and json.py wrapper if you are using python 2.4. If you are using python 2.5 or higher, the only file you need is pygvoicelib.py.

Included is a script, get\_auth.py that can retrieve authentication settings for you.

First create an application-specific password: https://accounts.google.com/b/0/IssuedAuthSubTokens

Then run the script and input your username and the one time password (the spaces around the password do not matter.)

The script will output a new script that can be used to send text messages (it includes all needed keys.)

If you have any issues or questions, email the email address below, or open an issue at:
https://github.com/korylprince/pygvoicelib/issues

#Usage#

The main file that you will need is:
* pygvoicelib.py

All the functions are documented inside the code. For a quick documentation, just do:

    $ python
    >>> import pygvoicelib
    >>> help(pygvoicelib)

They have full text that guides you through and very simple source. Please refer to them as an example of proper usage of the library.

#Copyright Information#

Most code is Copyright 2010, TELTUB Inc, author Ehsan Foroughi. This code is licensed as GPLv3.

The simplejson library may have it's own license.

The pygvoicelib.py was modified and get\_auth.py script was written by Kory Prince (korylprince at gmail dot com.)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
