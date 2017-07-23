var pn532 = require('pn532');
var SerialPort = require('serialport');

var serialPort = new SerialPort('/dev/ttyUSB0', { baudrate: 115200 });

var options = {
  pollInterval: 500
};

var rfid = new pn532.PN532(serialPort, options);

console.log('Initialising...');

rfid.on('ready', function() {
  console.log('PN532 initialised');

  rfid.on('tag', function(tag) {
    console.log('tag:', tag);
  });
});
