import React, { useEffect } from "react";

async function handleSubmit() {
  const googleClientID =
    "1015886605445-kd9c0mrhk84tc5jrkit0r6hqs6jipu8a.apps.googleusercontent.com";
  const scope = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
  ].join(" ");

  var state = "";
  await fetch("http://localhost:8000/authen/google/init_state", {
    method: "POST",
    credentials: "include",
  })
    .then((response) => response.json())
    .then((data) => {
      state = data.state;
    })
    .catch((err) => {
      console.log(err);
    });

  const params = {
    response_type: "code",
    client_id: googleClientID,
    redirect_uri: "http://localhost:8000/authen/google/callback",
    state: state,
    promt: "select_account",
    access_type: "offline",
    include_granted_scopes: "true",
    scope,
  };
  const urlParams = new URLSearchParams(params).toString();
  const url = `https://accounts.google.com/o/oauth2/v2/auth?${urlParams}`;
  console.log(url);

  window.location = url;
}

function Login() {
  return (
    <div>
      <h1>Login</h1>
      <button type="submit" onClick={handleSubmit}>
        Login with Google
      </button>
    </div>
  );
}

export default Login;
