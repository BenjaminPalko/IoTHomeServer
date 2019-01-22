import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Well } from 'react-bootstrap';


import UserInput from './UserInput/UserInput';
import UserOutput from './UserOutput/UserOutput';
import ToolBar from './components/ToolBar/ToolBar';
import SideDrawer from './components/SideDrawer/SideDrawer';
import Backdrop from './components/Backdrop/Backdrop';
import Navbar from './components/CustomNavbar/CustomNavbar';
import DeviceListContent from './components/DeviceListContent/DeviceListContent';
import RaspberryPiConsole from './components/RaspberryPiConsole/RaspberryPiConsole';
import ControlSetting from './components/ControlSetting/ControlSetting';



class App extends Component {
  state = {
    sideDrawerOpen: false,
    username: "Andrew_Nguyen"
  };

  drawerToggleClickHandler = () => {
    this.setState((prevState) => {
      return {sideDrawerOpen: !prevState.sideDrawerOpen};
    });
  };

  backdropClickHanlder = () => {
    this.setState({sideDrawerOpen: false});
  };

  usernameChangedHandler = (event) => {
    this.setState({username: event.target.value});
  }

  render() {
    let backdrop;

    if(this.state.sideDrawerOpen){
      backdrop = <Backdrop click={this.backdropClickHanlder}/>
    }
    return (
      <div style={{height: '100%'}}>
        {/* <ToolBar drawerClickHandler={this.drawerToggleClickHandler}/> */}
        {/* BootStrap Below*/}
        <Router>
          <div>
          <Navbar />
          <Route exact path="/" component={DeviceListContent} />
          <Route path="/raspberrypi" component={RaspberryPiConsole} />
          <Route path="/controlsetting" component={ControlSetting} />
          </div>
        </Router>
        {/* Bootstrap Above */}
        <SideDrawer show={this.state.sideDrawerOpen}/>
        {backdrop}
        <main style={{marginTop: '64px'}}>

        </main>
      </div>
    );
  }
}

export default App;
