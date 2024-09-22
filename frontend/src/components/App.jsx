import React, { useEffect, useState } from "react";
import Header from "./Header";
import Footer from "./Footer";
import Note from "./Note";
import CreateArea from "./CreateArea";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

export default function App() {
  var [items, setItems] = useState([{ title: "test", content: "test too" }]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/notes/")
      .then((response) => response.json())
      .then((data) => {
        setItems(data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  function addItem(title, content) {
    fetch("http://127.0.0.1:8000/notes/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: title,
        text: content,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        setItems((preItems) => {
          return [...preItems, data];
        });
      })
      .catch((err) => {
        console.log(err);
      });
  }

  function deleteItem(id) {
    fetch(`http://127.0.0.1:8000/notes/${id}`, {
      method: "DELETE",
    }).then((response) => {
      if (response.status === 200) {
        setPosts(
          posts.filter((post) => {
            return post.id !== id;
          })
        );
      } else {
        return;
      }
    });

    setItems((preItems) => {
      return preItems.filter((item, index) => id !== index);
    });
  }

  return (
    <div>
      <Header />
      <CreateArea addItem={addItem} />
      {items.map((item, index) => {
        return (
          <Note
            key={index}
            id={index}
            title={item.title}
            content={item.content}
            deleteItem={deleteItem}
          />
        );
      })}
      <Footer />
    </div>
  );
}
