import React, {Component} from 'react'
import {Container} from 'react-bootstrap'
import './About.css'

export default class About extends Component {
    render() {
        return (
            <Container className="contentPane">
                <div className="headerlayout">
                    <div className="spacer">
                        <h2 className="title">About </h2>
                        <p>My Token connection: {window.token}</p>
                        <p>The goal of this project is the research and development into current and future applications of IoT technology. 
                        Over the course of the Fall Semester we have researched current technologies and software used in IoT. We have 
                        considered various options and have mitigated our list then decided on the most appropriate task. </p>
                        <p>Our project aims to create a home IoT network utilizing the raspberry pi as a central server, various devices can be added 
                        to this network and accessed/controlled through a companion web application with the potential of expanding to 
                        other application platforms. </p>
                        <p>Our project aims to explore containerization for optimization, we have researched 
                        both Docker and Kubernetes as candidates. Various TCP options were investigated and support for existing devices 
                        will be a topic of research as progress is made. </p>
                    </div>
                </div>   
            </Container>
        )
    }
}