import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const [data, setdata] = useState({
    message: ""
  });

  useEffect(() => {
    fetch('/message').then((res) => 
      res.json().then((data) => {
        setdata({message: data.message})
      }));
  }, []);

  return (
    <h1>{data.message}</h1>
  );
}

export default App;
