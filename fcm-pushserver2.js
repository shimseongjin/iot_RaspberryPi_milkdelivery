var admin = require("firebase-admin");
var serviceAccount = require("/home/pi/serviceAccountKey.json");
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  //databaseURL: "https://pushservice-ea7d5.firebaseio.com"
  databaseURL: "https://pushservice-ea7d5.firebaseio.com"
});

// This registration token comes from the client FCM SDKs.
var registrationToken = "djT8vCXMnbQ:APA91bGZKwd2ha5Ss_gQltsXcktZjtcCTfyWb8W6OzO5Hw7Btf1exrTX_N7zrwRZUcrpOtqV9XluTmuN1wURVE9r7RCqtGDoYmc8U2-HlPGZKnTfPhILxx5CVbQbbexRe5pl4Uk7SQQC";
var state = 'none';
var temp = 0;
var hum = 0;
var cnt=0;

process.argv.forEach(function (val, index, array) {
	if (index == 2) {
		// value: m_on, m_off
		if (val == 'm_on') state = '우유가 들어왔습니다.';
		if (val == 'm_off') state = '우유를 가져갔습니다.';
			
	}
	if (index == 3) {
		// value: temp
		temp = val;
		state = '온도는 ' + temp;
	}
	if (index == 4) {
		// value: temp
		hum = val;
		state += ' 습도는 ' + hum;
	}
});

var payload = {
  notification: {
    title: "Milk Status",
    body: state
  }
};
// Send a message to the device corresponding to the provided registration token.
admin.messaging().sendToDevice(registrationToken, payload)
  .then(function(response) {
    console.log("Successfully sent message:", response);
	process.exit(-1);
  })
  .catch(function(error) {
    console.log("Error sending message:", error);
  });
