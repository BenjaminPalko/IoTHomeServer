import React, { Component } from 'react'
import { Navbar, Nav, NavItem, MenuItem,  NavDropdown } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import './CustomNavbar.css'
import logo from '../../logo_body.svg';

export default class CustomNavbar extends Component {
  render() {
    return (
      <Navbar default collapseOnSelect>
        <Navbar.Header>
          <Navbar.Brand>
            <img className="logo_image" src={logo} alt="logo"/>
            <Link to="/">IOT Controller</Link>
          </Navbar.Brand>
          <Navbar.Toggle />
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav pullRight>
            <NavItem eventKey={1} componentClass={Link} href="/" to="/">
              IOT Device Library
            </NavItem>
            <NavItem eventKey={2} componentClass={Link} href="/raspberrypi" to="/raspberrypi">
              Raspberry Pi Console
            </NavItem>
            <NavItem eventKey={3} componentClass={Link} href="/controlsetting" to="/controlsetting">
              Control Settings
            </NavItem>
            <NavDropdown eventKey={4} title="Account" id="basic-nav-dropdown">
              <MenuItem eventKey={4.1}>Configuration</MenuItem>
              <MenuItem eventKey={4.2}>Change Password</MenuItem>
              <MenuItem divider />
              <MenuItem eventKey={4.3}>Log Out</MenuItem>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    )
  }
}