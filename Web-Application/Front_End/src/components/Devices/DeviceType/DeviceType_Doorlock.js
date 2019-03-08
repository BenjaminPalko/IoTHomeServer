import React from 'react';
import {Form, Button, Col, ButtonToolbar, ButtonGroup} from 'react-bootstrap';
import Doorlock_Input from '../Doorlock_Privilege/Doorlock_Input';
// import './DeviceType_Doorlock.css';


// Doorlock
// Indicate - "Passcode is set"
// Privilege passcode to access pin
// Pin 4
// 1 2 3
// input saves into variable

// onSubmit={pin_submit(this.value)}

const devicetype_doorlock = (object) => {
    return (
        <div>
            <Form method="POST">
                <Form.Row>
                    <Col>
                        <Form.Control type="text" name="pinCombo" pattern="[1-3]{4}" maxlength="4" placeholder="Set Pin Code" />
                    </Col>
                    <Col>
                        <Button variant="primary" type="submit">
                            Validate
                        </Button>
                    </Col>
                </Form.Row>
            </Form>
        </div>
    )
};

export default devicetype_doorlock;