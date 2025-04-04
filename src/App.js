import React, { useState } from "react";
import InputForm from "./components/InputForm";
import NameList from "./components/NameList";
import "./styles/App.css";

const App = () => {
    const [names, setNames] = useState([]);

    return (
        <div className="app-container">
            <InputForm setNames={setNames} />
            <NameList names={names} />
        </div>
    );
};

export default App;
