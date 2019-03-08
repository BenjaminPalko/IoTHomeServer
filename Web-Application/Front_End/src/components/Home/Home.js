import React, {Component} from 'react'
import {Jumbotron, Container} from 'react-bootstrap'
import './Home.css'
// import DeviceType_LED from '../Devices/DeviceType/DeviceType_LED';
// import DeviceType_Temperature from '../Devices/DeviceType/DeviceType_Temperature';

export default class Home extends Component {

    render() {
        return (
            <div>
                <Container>
                    <Jumbotron className="text-center">
                        <h1>IoT Web Controller</h1>
                        <h5>Simple IoT platform that controls Arduino devices remotely.</h5>
                        <h6>Press "Find Out More!" to learn more about each device. </h6>
                    </Jumbotron>
                    {/* <Container> */}
                        {/* <Row>
                            <h2>Development Testing Area</h2>
                        </Row>
                        <Row>
                            <Col>
                                <Card >
                                    
                                </Card>
                            </Col>
                        </Row>
                        <br/>
                        <Row>
                            <Col>
                                <Card >
                                    <Card.Body>
                                        <Card.Title>Card Title</Card.Title>
                                        <Card.Text>
                                        Some quick example text to build on the card title and make up the bulk of
                                        the card's content.
                                        </Card.Text>
                                        <Button variant="primary">Go somewhere</Button>
                                    </Card.Body>
                                </Card>
                            </Col>
                        </Row>
                        <br/>
                        <Row>
                            <Col>
                                <Card >
                                    <Card.Body>
                                        <Card.Title>Card Title</Card.Title>
                                        <Card.Text>
                                        Some quick example text to build on the card title and make up the bulk of
                                        the card's content.
                                        </Card.Text>
                                        <Button variant="primary">Go somewhere</Button>
                                    </Card.Body>
                                </Card>
                            </Col>
                        </Row>
                        <br/> */}
                    {/* </Container>
                    <ListGroup variant="flush">
                        <ListGroup.Item> */}
                                {/* <DeviceType_Temperature/> */}
                        {/* </ListGroup.Item>
                        <ListGroup.Item> */}
                            {/*<DeviceType_LED/> */}
                            {/* LED Light Toggles */}
                        {/* </ListGroup.Item>
                        <ListGroup.Item></ListGroup.Item>
                    </ListGroup> */}
                </Container>
            </div>
        )
    }
}   