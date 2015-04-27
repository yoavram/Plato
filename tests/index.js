define(function (require) {
  var registerSuite = require('intern!object');
  var assert = require('intern/chai!assert');

  registerSuite({
    name: 'index',

    'github button': function () {
      return this.remote
        .get(require.toUrl('src/index.html'))
        .setFindTimeout(5000)
        .findByClassName('octicon-mark-github')
        .click()
        .sleep(5000)
        .getPageTitle()
        .then(function (text) {
           assert.strictEqual(text, 'yoavram/Plato');
        })
        .end();
        
        
        // .findById('greeting')
        //   .getVisibleText()
        //   .then(function (text) {
        //     assert.strictEqual(text, 'Hello, Elaine!',
        //       'Greeting should be displayed when the form is submitted');
        //   });
    }
  });
});