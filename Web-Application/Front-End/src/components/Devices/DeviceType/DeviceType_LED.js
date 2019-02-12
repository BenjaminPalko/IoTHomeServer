import React from 'react';
import {Form, Button} from 'react-bootstrap';
import './DeviceType_LED.css';

const devicetype_led = (object) => {
    return (
        <div>
            <Form method="POST">
                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter email" />
                    <Form.Text className="text-muted">
                    We'll never share your email with anyone else.
                    </Form.Text>
                </Form.Group>

                <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control name="passwordName" type="password" placeholder="Password" />
                </Form.Group>
                <Form.Group controlId="formBasicChecbox">
                    <Form.Check type="checkbox" label="Check me out" />
                </Form.Group>
                <Button name="red-led" variant="primary" >
                    Red
                </Button>
                <Button name="green-led" variant="primary" >
                    Green
                </Button>
                <Button name="blue-led" variant="primary" >
                    Blue
                </Button>
                <Button name="off-led" variant="primary" >
                    Off
                </Button>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
        </div>
    )
};

export default devicetype_led;