var page = require('webpage').create();
// 屏幕捕获
page.viewportSize = {width: 1024, height: 768};
page.clipRect = {top: 0, left: 0, width: 1024, height: 768};

//网络监听
page.onResourceRequested = function(request) {
  console.log('Request ' + JSON.stringify(request, undefined, 4));
};
page.onResourceReceived = function(response) {
  console.log('Receive ' + JSON.stringify(response, undefined, 4));
};

page.open('http://cuiqingcai.com', function (status) {
    console.log("Status: " + status);
    if (status === 'success') {
        console.log('保存图片');
        page.render('./example.png');
    }
    phantom.exit();
});