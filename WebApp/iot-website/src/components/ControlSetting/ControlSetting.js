import React, { Component } from 'react';
import { Grid, Col, Image } from 'react-bootstrap';
import './ControlSetting.css';

export default class ControlSetting extends Component {
  render() {
    return (
      <div>
        <Image src="assets/dog-people.jpg" className="header-image" />
        <Grid>
          <Col xs={12} sm={8} smOffset={2}>
            <Image src="assets/person-1.jpg" className="about-profile-pic" rounded />
            <h3>CONTROL SETTING</h3>
            <p>THIS IS THE CONTROL SETTING PAGE </p>
          </Col>
        </Grid>
      </div>
    )
  }
}