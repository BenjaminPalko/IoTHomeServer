import {Button, Modal, Render} from 'react-bootstrap';
import React, { Component } from 'react';

class Doorlock_Input extends React.Component {
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
          aria-labelledby="contained-modal-title-vcenter"
        >
          <Modal.Header closeButton>
            <Modal.Title id="contained-modal-title-vcenter">
              Modal heading
            </Modal.Title>
          </Modal.Header>
          <Modal.Body>
            <h4>Centered Modal</h4>
            <p>
              Cras mattis consectetur purus sit amet fermentum. Cras justo odio,
              dapibus ac facilisis in, egestas eget quam. Morbi leo risus, porta
              ac consectetur ac, vestibulum at eros.
            </p>
          </Modal.Body>
          <Modal.Footer>
            <Button onClick={this.props.onHide}>Close</Button>
          </Modal.Footer>
        </Modal>
        </div>
      );
    }
  }

export default Doorlock_Input;