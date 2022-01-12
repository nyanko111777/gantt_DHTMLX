var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');
var Promise = require('bluebird');
require("date-format-lite");

var port = 1337;
var app = express();

var cookieSession = require("cookie-session");
app.set('trust proxy', 1)
app.use(
	cookieSession({
	  name: "__session",
	  keys: ["key1"],
		maxAge: 24 * 60 * 60 * 100,
		secure: true,
		httpOnly: true,
		sameSite: 'none'
	})
);

app.use(express.static(path.join(__dirname, "public")));
app.use(bodyParser.urlencoded({extended: true}));

app.listen(port, function () {
	console.log("Server is running on port " + port + "...");
});
