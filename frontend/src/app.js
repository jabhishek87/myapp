import React from 'react';
import Router, {Route} from 'react-router';
import AuthenticatedApp from './js/components/AuthenticatedApp'
import Login from './js/components/Login';
import Signup from './js/components/Signup';
import Home from './js/components/Home';
//import Quote from './js/components/Quote';
import RouterContainer from './js/services/RouterContainer';
import LoginActions from './js/actions/LoginActions';

var routes = (
  <Route handler={AuthenticatedApp}>
    <Route name="login" handler={Login}/>
    <Route name="signup" handler={Signup}/>
    <Route name="home" path="/" handler={Home}/>
//    <Route name="quote" handler={Quote}/>
  </Route>
);

var router = Router.create({routes});
RouterContainer.set(router);

let jwt = localStorage.getItem('jwt');
if (jwt) {
  LoginActions.loginUser(jwt);
}

router.run(function (Handler) {
  React.render(<Handler />, document.getElementById('content'));
});

