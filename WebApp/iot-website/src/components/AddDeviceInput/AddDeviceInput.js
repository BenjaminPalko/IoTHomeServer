import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import {Button, Modal, Render} from 'react-bootstrap';
import './AddDeviceInput.css'


class AddDeviceInput extends React.Component {
    constructor(props, context) {
      super(props, context);
  
      this.handleHide = this.handleHide.bind(this);
  
      this.state = {
        show: false
      };
    }
  
    handleHide() {
      this.setState({ show: false });
    }
    render() {
      return (
        <div className="modal-container" >
          <Button
            bsStyle="primary"
            bsSize="medium"
            onClick={() => this.setState({ show: true })}
          >
            + Add Device
          </Button>
  
          <Modal
            show={this.state.show}
            onHide={this.handleHide}
            container={this}
            aria-labelledby="contained-modal-title"
          >
            <Modal.Header closeButton>
              <Modal.Title id="contained-modal-title">
                Input The Device Settings
              </Modal.Title>
            </Modal.Header>
            <Modal.Body>
              ADD DEVICE CONTENT
            </Modal.Body>
            <Modal.Footer>
              <Button onClick={this.handleHide}>Close</Button>
            </Modal.Footer>
          </Modal>
        </div>
      );
    }
}
  
export default AddDeviceInput;