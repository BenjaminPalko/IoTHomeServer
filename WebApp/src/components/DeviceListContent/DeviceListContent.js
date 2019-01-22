import React, { Component } from 'react';
import { Well, Button } from 'react-bootstrap';
import './DeviceListContent.css'
import AddDeviceInput from '../AddDeviceInput/AddDeviceInput';

export default class DeviceListContent extends Component {
    render() {
      return (
        <Well className="contentPane">
            <div className="headerlayout">
              <h2 className="title">IoT Devices </h2>
              <div className="spacer"></div>
              <AddDeviceInput/>
              
            </div>
            <Well className="contentList">
              <p>This is the page content!</p>
            </Well>
        </Well>
      )
    }
  }