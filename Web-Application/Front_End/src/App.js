import React, { Component } from 'react';
import './App.css';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import Home from './components/Home/Home';
import Navbar from './components/CustomNavbar/CustomNavbar';
// import Login from './components/Login/Login';
// import About from './components/About/About';
// import Devices from './components/Devices/Devices';

class App extends Component {

  render() {
      return (
        <Router>
          <div>
            <Navbar/>
            <Route exact path="/" component={Home} />
            {/* <Route path="/login/" component={Login} />  */}
          </div>
        </Router>
      );
  }
}

export default App;
