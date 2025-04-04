import React from "react";
import "./../styles/App.css";

const NameList = ({ names }) => {
    return (
        <div className="name-list">
            <h3>Generated Product Names</h3>
            {names.length === 0 ? (
                <p>No names generated yet.</p>
            ) : (
                <ul>
                    {names.map((name, index) => (
                        <li key={index}>{name}</li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default NameList;
