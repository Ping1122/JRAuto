import React from "react";
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";

function NewTask(props) {
  const { show, handleClose, handleInsert, handlePut } = props;
  return (
    <Modal
      show={show}
      onHide={handleClose}
      dialogClassName="new-task"
      className="new-task"
    >
      <Modal.Header closeButton>
        <Modal.Title>Assign Task</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        Add the task to the task queue. To add to the front, click "Insert". To
        add to the end of the queue, click "Put"
      </Modal.Body>
      <Modal.Footer>
        <Button variant="secondary" onClick={handleClose}>
          Close
        </Button>
        <Button variant="primary" onClick={handleInsert}>
          Insert
        </Button>
        <Button variant="primary" onClick={handlePut}>
          Put
        </Button>
      </Modal.Footer>
    </Modal>
  );
}

export default NewTask;
