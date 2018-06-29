//网页加载速度
var page = require('webpage').create(),
    system = require('system'),
    t, address;

page.onConsoleMessage = function (msg) {
    console.log(msg)
};
if (system.args.length === 1) {
    console.log('Usage: loadspeed.js <some URL>');
    phantom.exit();
}

t = Date.now();
address = system.args[1];
page.open(address, function (status) {
    var title = page.evaluate(function () {
        return document.title;
    });
    console.log('Page title is ' + title);
    if (status !== 'success') {
        console.log('Fail to load the address');
    } else {
        t = Date.now() - t;
        console.log('Loading ' + system.args[1]);
        console.log('LoadTime: ' + t + 'msec');
    }
    phantom.exit();
});