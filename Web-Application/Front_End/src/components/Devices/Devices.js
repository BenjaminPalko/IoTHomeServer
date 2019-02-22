import React, {Component} from 'react'
import {Container, ListGroup} from 'react-bootstrap'
import AddDeviceInput from './AddDeviceInput/AddDeviceInput';
import DeviceType_LED from './DeviceType/DeviceType_LED';
import DeviceType_Doorlock from './DeviceType/DeviceType_Doorlock';
import DeviceType_Geolocation from './DeviceType/DeviceType_Geolocation';
import './Devices.css'

export default class Devices extends Component {
    render() {
        return (
            <Container className="contentPane">
                <div className="headerlayout">
                    <h2 className="title">Devices </h2>
                    <div className="spacer"></div>
                    <AddDeviceInput/>
                </div>
                <Container className="contentList">
                    <ListGroup>
                    <ListGroup.Item><h4>LED Control</h4><DeviceType_LED/></ListGroup.Item>
                    <ListGroup.Item><h4>Temperature</h4></ListGroup.Item>
                    <ListGroup.Item><h4>Doorlock Control</h4><DeviceType_Doorlock/></ListGroup.Item>
                    <ListGroup.Item><h4>Weather Forecast</h4><DeviceType_Geolocation/></ListGroup.Item>
                    </ListGroup>
                </Container>
            </Container>
        )
    }
}