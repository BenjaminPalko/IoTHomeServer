import React, {Component} from 'react'

import {Jumbotron, Container, ListGroup, Button} from 'react-bootstrap'
import './Home.css'

export default class Home extends Component {
    render() {
        return (
            <div>
                <Container>
                    <Jumbotron>
                        <h2>Welcome to IoT Web Controller</h2>
                        <p>The Website is in Development.</p>
                        <p>My Token connection: {window.token}</p>
                    </Jumbotron>
                    <div>
                        <h2>Development Testing Area</h2>
                        <ListGroup variant="flush">
                            <ListGroup.Item>
                                <Button variant="primary">B</Button>
                                <Button variant="danger">R</Button>
                                <Button variant="warning">Y</Button>
                                <Button className="spacing" variant="secondary">Off</Button>
                                LED Light Toggles
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <input className="spacing" type="text"></input>
                                <Button className="spacing" variant="primary" type="submit">
                                    Submit
                                </Button>
                                Temperature
                            </ListGroup.Item>
                            <ListGroup.Item></ListGroup.Item>
                            <ListGroup.Item></ListGroup.Item>
                        </ListGroup>
                    </div>
                </Container>
            </div>
        )
    }
}   