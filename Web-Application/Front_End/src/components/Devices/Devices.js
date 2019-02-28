import React, {Component} from 'react'
import {Container, ListGroup, Button, Collapse, Col, Row} from 'react-bootstrap'
import AddDeviceInput from './AddDeviceInput/AddDeviceInput';
import DeviceType_LED from './DeviceType/DeviceType_LED';
import DeviceType_Doorlock from './DeviceType/DeviceType_Doorlock';
import DeviceType_Geolocation from './DeviceType/DeviceType_Geolocation';
import DeviceType_Temperature from './DeviceType/DeviceType_Temperature';
import './Devices.css'

export default class Devices extends Component {
    constructor(props, context) {
        super(props, context);
    
        this.state = {
          open: false,
        };
      }

    render() {
        const { open } = this.state;
        return (
            <Container className="contentPane">
                <div className="headerlayout">
                    <h2 className="title">Devices </h2>
                    <div className="spacer"></div>
                    <AddDeviceInput/>
                </div>
                <Container className="contentList">
                    <ListGroup>
                    <ListGroup.Item>
                        <Row>
                            <Col><h4>LED Control</h4></Col>
                            <Col>
                                <Button
                                    onClick={() => this.setState({ open: !open })}
                                    aria-controls="device_LED"
                                    aria-expanded={open}
                                    >
                                    Expand
                                </Button>
                            </Col>
                        </Row>
                        <Row>
                            <Collapse in={this.state.open}>
                                <div id="device_LED">
                                    <DeviceType_LED/>
                                </div>
                            </Collapse>
                        </Row>
                    </ListGroup.Item>
                    <ListGroup.Item><h4>Temperature</h4><DeviceType_Temperature/></ListGroup.Item>
                    <ListGroup.Item><h4>Doorlock Control</h4><DeviceType_Doorlock/></ListGroup.Item>
                    <ListGroup.Item><h4>Weather Forecast</h4><DeviceType_Geolocation/></ListGroup.Item>
                    </ListGroup>
                </Container>
            </Container>
        )
    }
}