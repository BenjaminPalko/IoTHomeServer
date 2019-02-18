import React, {Component} from 'react'
import {Container, ListGroup} from 'react-bootstrap'
import AddDeviceInput from './AddDeviceInput/AddDeviceInput';
import './Devices.css'

export default class Devices extends Component {
    render() {
        return (
            <Container className="contentPane">
                <div className="headerlayout">
                    <h2 className="title">Devices </h2>
                    <p>My Token connection: {window.token}</p>
                    <div className="spacer"></div>
                    <AddDeviceInput/>
                
                </div>
                <Container className="contentList">
                    <ListGroup>
                    <ListGroup.Item>LED 1</ListGroup.Item>
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