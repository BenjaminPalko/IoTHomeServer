import React from 'react';
import {Form, Col, Button} from 'react-bootstrap';
// import './DeviceType_Doorlock.css';

const devicetype_geolocation = (object) => {
    return (
        <div>
            <Form method="POST">
                <Form.Group controlId="exampleForm.ControlTextarea1">
                <Form.Row>
                    <Col>
                        <Form.Control type="text" name="cityName" placeholder="Example: Ottawa" />
                    </Col>
                    <Col>
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                    </Col>
                </Form.Row>
                </Form.Group>
            </Form>
        </div>
    )
};

export default devicetype_geolocation;