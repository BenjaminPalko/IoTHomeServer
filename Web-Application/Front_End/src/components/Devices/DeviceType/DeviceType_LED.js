import React from 'react';
import {Form, Button} from 'react-bootstrap';
import './DeviceType_LED.css';

const devicetype_led = (object) => {
    return (
        <div>
            <Form method="POST">
                <Button type="submit" name="ledSwitch" variant="danger" value="red">
                    Red
                </Button>
                <Button type="submit" name="ledSwitch" variant="success" value="green">
                    Green
                </Button>
                <Button type="submit" name="ledSwitch" variant="primary" value="blue">
                    Blue
                </Button>
                <Button type="submit" name="ledSwitch" variant="secondary" value="off">
                    Off
                </Button>
            </Form>
        </div>
    )
};

export default devicetype_led;