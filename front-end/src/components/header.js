import React from "react";
import logo from "../assets/logo.png";
import "./header.css";

const Header = () => {
  return (
    <div className="header">
      <img
        style={{ cursor: "pointer" }}
        onClick={() => (window.location.href = "./")}
        src={logo}
        width="250px"
        alt="logo"
      />
    </div>
  );
};

export { Header };
