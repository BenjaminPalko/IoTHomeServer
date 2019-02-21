import React, {Component} from 'react'
import {Container, ListGroup} from 'react-bootstrap'
import AddDeviceInput from './AddDeviceInput/AddDeviceInput';
import DeviceType_LED from './DeviceType/DeviceType_LED';
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
                    <ListGroup.Item><DeviceType_LED/></ListGroup.Item>
                    <ListGroup.Item>LED 2</ListGroup.Item>
                    <ListGroup.Item>Temperature 1</ListGroup.Item>
                    <ListGroup.Item>Temperature 2</ListGroup.Item>
                    <ListGroup.Item>Forecast</ListGroup.Item>
                    </ListGroup>
                </Container>
            </Container>
        )
    }
}