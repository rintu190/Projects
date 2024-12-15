const express = require('express');
const bodyParser = require('body-parser');
const UserRouter = require('./router/user.router');

const app = express();
app.use(bodyParser.json());
app.use('/',UserRouter);

module.exports =  app;