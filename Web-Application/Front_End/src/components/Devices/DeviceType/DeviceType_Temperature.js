import React from 'react';
import {Form, Button} from 'react-bootstrap';

const devicetype_temperature = (object) => {

    // var socket = io.connect('http://127.0.0.1:5000');
    // socket.on('connect', function() {
    //     socket.send('User has connected!');
    // });

    // socket.on('message', function(msg) {
    //     $("#messages").append('<li>'+msg+'</li>');
    //     console.log('Received message');
    // });

    // $('#sendbutton').on('click', function() {
    //     socket.send($('#myMessage').val());
    //     $('#myMessage').val(''); // clears out the msg for new
    // });

    return (
        <div>
            <Form method="POST">
                <Form.Group controlId="temperature">
                    <Form.Label>Temperature Meter</Form.Label>
                    <Form.Control name="temperature" type="temperature" placeholder="Temperature" />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
            {/* <ul id="messages"></ul>
            <input type="text" id="myMessage"/>
            <button id="sendbutton">Send</button>          */}
        </div>
    )
};

export default devicetype_temperature;