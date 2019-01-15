import React, { Component } from 'react';
import { Grid, Col, Image } from 'react-bootstrap';
import './RaspberryPiConsole.css';

export default class RaspberryPiConsole extends Component {
  render() {
    return (
      <div>
        <Image src="assets/dog-people.jpg" className="header-image" />
        <Grid>
          <Col xs={12} sm={8} smOffset={2}>
            <Image src="assets/person-1.jpg" className="about-profile-pic" rounded />
            <h3>RASPBERRY PI</h3>
            <p>THIS IS THE PI CONSOLE </p>
          </Col>
        </Grid>
      </div>
    )
  }
}