import React, {Component} from 'react'
import {Jumbotron, Container, ListGroup, Button} from 'react-bootstrap'
import './Home.css'
import DeviceType_LED from '../Devices/DeviceType/DeviceType_LED';

export default class Home extends Component {
   
//    Testing purposes for api calling
    constructor(props) {
        super(props);
        this.state = {
            items: [],
            isLoaded: false,
        }
      }
    
      componentDidMount() {
        fetch('https://jsonplaceholder.typicode.com/users')
            .then(res => res.json())
            .then(json => {
                this.setState({
                    isLoaded: true,
                    items: json,
                })
            });
      }

    render() {

        var {isLoaded, items} = this.state;

    if(!isLoaded){
        return <div>Loading...</div>
    }
    else {
        return (
            <div>
                <Container>
                    <Jumbotron>
                        <h2>Welcome to IoT Web Controller</h2>
                        <p>The Website is in Development.</p>
                    </Jumbotron>
                    <div>
                        <h2>Development Testing Area</h2>
                        <ListGroup variant="flush">
                            <ListGroup.Item>
                                <input className="spacing" type="text"></input>
                                <Button className="spacing" variant="primary" type="submit">
                                    Submit
                                </Button>
                                Temperature
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <DeviceType_LED/> 
                                LED Light Toggles
                                <p>My Token connection: {window.token}</p>
                            </ListGroup.Item>
                            <ListGroup.Item></ListGroup.Item>
                        </ListGroup>
                    </div>
                    <div>
                        <ul>
                        {items.map(item => (
                            <li key={item.id}>
                            Name: {item.name} | Email: {item.email}
                            </li>
                        ))};
                        </ul>
                    </div>
                </Container>
            </div>
        )
    }}
}   