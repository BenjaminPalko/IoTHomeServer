import React, {Component} from 'react'
import {Jumbotron, Container, ListGroup, Button} from 'react-bootstrap'
import './Home.css'
import DeviceType_LED from '../Devices/DeviceType/DeviceType_LED';
import DeviceType_Temperature from '../Devices/DeviceType/DeviceType_Temperature';

export default class Home extends Component {

    render() {
        return (
            <div>
                <Container>
                    <Jumbotron>
                        <h2>Welcome to IoT Web Controller</h2>
                        <p>The Website is in Development.</p>
                    </Jumbotron>
                    <div>
                        <h2>Development Testing Area</h2>
                        <ListGroup variant="flush">
                            <ListGroup.Item>
                                 <DeviceType_Temperature/>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                {/*<DeviceType_LED/> */}
                                LED Light Toggles
                            </ListGroup.Item>
                            <ListGroup.Item></ListGroup.Item>
                        </ListGroup>
                    </div>
                </Container>
            </div>
        )
    }
}   