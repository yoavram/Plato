# Plato
[![Build Status](https://travis-ci.org/yoavram/Plato.svg?branch=master)](https://travis-ci.org/yoavram/Plato)

![Plato](https://raw.githubusercontent.com/yoavram/plato/master/public/plato.png)

A tiny web app to design microplates and download them as a dataframe CSV.

## Usage

Open the app at <http://plato.yoavram.com/> or run locally by downloading `index.html` or cloning the repo and double clicking `index.html`.

## Testing

The app can be tested using the test suite. You will need Python 2.7, virtualenv, Chrome browser, 
and [Selenium Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) which should be in the path or in the repo folder.

1. Clone the repo: `git clone https://github.com/yoavram/plato.git && cd plato`.
2. Create a virtalenv: `virtualenv venv`.
3. Activate the virtualenv: Windows - `venv\scripts\activate`; Linux - `source venv/bin/activate`.
4. Install the requirements: `pip install -r requirements.txt`.
5. Get the Chromedriver for Selenium if you didn't already. See link above.
6. Start a local web server in the `public` folder: `cd public & python -m SimpleHTTPServer 8080`
6. Run the tests: `nosetests`.

Testing is currently only done on Windows 7 with latest Chrome (but see issue #6).

## Acknowledgments

- [Brian Connelly](https://github.com/briandconnelly) for suggestions and testing
- [BrowserStack](http://www.browserstack.com), a cross-browser testing tool on a cloud infrastructure of desktop and mobile browsers. Used for manual testing on other platforms and browsers.
- [Travis](https://travis-ci.org/yoavram/Plato) and [SauceLabs](https://saucelabs.com) used for continuous integration and automatic testing.

## License

Author: Yoav Ram <yoavram@gmail.com>

License: CC-BY-SA 3.0

Date: May 2015
