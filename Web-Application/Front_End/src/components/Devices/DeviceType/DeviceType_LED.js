import React from 'react';
import {Form, ButtonToolbar, Button} from 'react-bootstrap';
import './DeviceType_LED.css';

const devicetype_led = (object) => {
    return (
        <div>
            
            <Form method="POST">
                <input id="colorpicker" name="ledSwitch" type="color"/>
                <Button className="button" type="submit" variant="primary">Submit</Button>
            </Form>

            {/* <Form method="POST">
                <ButtonToolbar>
                    <Button className="button" type="submit" name="ledSwitch" variant="danger" value="red">
                        Red
                    </Button>
                    <Button className="button" type="submit" name="ledSwitch" variant="success" value="green">
                        Green
                    </Button>
                    <Button className="button" type="submit" name="ledSwitch" variant="primary" value="blue">
                        Blue
                    </Button>
                    <Button className="button" type="submit" name="ledSwitch" variant="secondary" value="off">
                        Off
                    </Button>
                </ButtonToolbar>
            </Form> */}
        </div>
    )
};

export default devicetype_led;