import React, { useEffect, useState } from 'react';
import './App.css';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import {Navbar} from './components/navbar';
import {Footer} from "./components/footer"
import {Admin} from "./pages/admin/admin";
import {Cart} from "./pages/cart/cart";
import {Shop} from "./pages/shop/shop";
import { ItemsGallery } from './components/itemsGallery';

function App() {

  //TODO remove temporary smrud
  const [data, setdata] = useState({
    message: ""
  });

  useEffect(() => {
    fetch('/message').then((res) => 
      res.json().then((data) => {
        setdata({message: data.message})
      }));
  }, []);

  // app goes between <Router> tags
  // TODO add variable route for products
  // TODO remove message  
  return (
    <div className="App">

      <Router>
        <Navbar />

        <Routes>
          <Route path="/" element={<Shop />}/>
          <Route path="/cart" element={<Cart />}/>
          <Route path="/admin" element={<Admin />} />
        </Routes>
        
        <ItemsGallery/>
        <h1>{data.message}</h1>
        <Footer />
      </Router>      

    </div>
  );
}

export default App;
