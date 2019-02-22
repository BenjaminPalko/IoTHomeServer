import React, {Component} from 'react'
import {Container, Button, Form} from 'react-bootstrap'
// import './Login.css'

export default class Login extends Component {
    render() {
        return (
            <Container className="contentPane">
                <Form action="" method="POST">
                    <h4>Please Login</h4>
                    <Form.Group controlId="formBasicUsername">
                        <Form.Label>Username</Form.Label>
                        <Form.Control type="text" placeholder="Enter username" value="{{request.form.username}}"/>
                    </Form.Group>

                    <Form.Group controlId="formBasicPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="Enter password" value="{{request.form.password}}"/>
                    </Form.Group>
                    <Button variant="primary" type="submit" value="Login">
                        Submit
                    </Button>
                </Form>
            </Container>
        )
    }
}