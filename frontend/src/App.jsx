import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import Home from "./pages/Home";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route exact path="/login" element={Login()} />
        <Route exact path="/notes" element={Home()} />
      </Routes>
    </Router>
  );
};

export default App;
