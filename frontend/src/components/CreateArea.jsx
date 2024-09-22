import React, { useState } from "react";

function CreateArea(props) {
  var [title, setTitle] = useState("");
  var [content, setContent] = useState("");

  function handleValueTitle(event) {
    title = event.target.value;
    setTitle(title);
  }

  function handleValueContent(event) {
    content = event.target.value;
    setContent(content);
  }

  function handleClick(event) {
    event.preventDefault();
  }

  return (
    <div>
      <form onSubmit={handleClick}>
        <input
          onChange={handleValueTitle}
          name="title"
          placeholder="Title"
          value={title}
        />
        <textarea
          onChange={handleValueContent}
          name="content"
          placeholder="Take a note..."
          rows="3"
          value={content}
        />
        <button
          onClick={() => {
            props.addItem(title, content);
            setTitle("");
            setContent("");
          }}
        >
          Add
        </button>
      </form>
    </div>
  );
}

export default CreateArea;
