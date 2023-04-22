import React from "react";
import {Link} from "react-router-dom";
import "./navbar.css";

export const Navbar = () => {
    return (
    <div className="navbar">

        <div className="logo">
            <Link to="/"> Main</Link>
        </div>

        <div className="links">           
            <Link to="/cart"> Cart</Link>
            <Link to="/admin"> Admin</Link>
        </div>    

    </div>
    )
};