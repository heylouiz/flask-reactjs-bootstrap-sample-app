/**
@file sample_app.jsx

@brief Flask ReactJS Bootstrap script.
*/

require('./sample_app.less');

require('babel-polyfill');

import React from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, hashHistory } from 'react-router';
import { Button, ButtonToolbar } from 'react-bootstrap';
import { Jumbotron } from 'react-bootstrap';

// App interface root class.
function App() {
  return (
    <main>
      <Jumbotron>
        <h1>Hello, world!</h1>
        <p>This is a project using Flask, ReactJS, ReactRouter
          and Bootstrap (react-bootstrap module).
        </p>
        <p>Read more about the projects.</p>
        <ButtonToolbar>
        <Button bsStyle="primary" href="https://flask.pocoo.org/">Flask</Button>
        <Button bsStyle="primary" href="https://github.com/ReactTraining/react-router">
          ReactRouter
        </Button>
        <Button bsStyle="primary" href="https://facebook.github.io/react/">ReactJS</Button>
        <Button bsStyle="primary" href="https://getbootstrap.com/">Bootstrap</Button>
        <Button bsStyle="primary" href="https://react-bootstrap.github.io/">React-Bootstrap</Button>
        </ButtonToolbar>
  </Jumbotron>
    </main>
  );
}

// App interface routes.
const ROUTES = (
    <Router history={hashHistory}>
      <Route path="/" component={App} />
    </Router>
);

ReactDOM.render(ROUTES, document.getElementById('content'));
