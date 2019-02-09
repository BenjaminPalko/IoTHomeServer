import React, { Component } from 'react'
import { Navbar, Nav, NavDropdown} from 'react-bootstrap';
import './CustomNavbar.css'
import logo from '../../logo_body.svg';

export default class CustomNavbar extends Component {
  render() {
    return (
        <Navbar bg="light" expand="lg">
            <Navbar.Brand href="/">
                <img className="logo_image" src={logo} alt="logo"/> {'IoT Web Controller'}
            </Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link href="/about">About</Nav.Link>
                    <Nav.Link href="/devices">Devices</Nav.Link>
                    <NavDropdown title="Account" id="basic-nav-dropdown">
                        <NavDropdown.Item href="https://github.com/BenjaminPalko/IoTHomeServer" target="_blank">GitHub Source Code</NavDropdown.Item>
                        <NavDropdown.Item href="/account/configuration">Configuration</NavDropdown.Item>
                        <NavDropdown.Item href="/account/change_password">Change Password</NavDropdown.Item>
                        <NavDropdown.Divider />
                        <NavDropdown.Item href="/logging_out">Log Out</NavDropdown.Item>
                    </NavDropdown>
                </Nav>
                <Navbar.Text>
                    Signed in as: <a href="#login">Andrew Nguyen</a>
                </Navbar.Text>
            </Navbar.Collapse>
        </Navbar>
    )
  }
}