import React, { useState } from "react";
import { generateNames } from "../api";
import "./../styles/Form.css";  

const InputForm = ({ setNames }) => {
    const [description, setDescription] = useState("");
    const [tone, setTone] = useState("Innovative"); 
    const [numNames, setNumNames] = useState(5); 
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        const names = await generateNames(description, tone, numNames);
        setNames(names);
        setLoading(false);
    };

    return (
        <div className="form-container">
            <h2>AI Product Name Generator</h2>
            <form onSubmit={handleSubmit}>
                <label>Product Description:</label>
                <textarea 
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Describe your product..."
                    required
                />

                <label>Brand Tone:</label>
                <select value={tone} onChange={(e) => setTone(e.target.value)}>
                    <option value="Innovative">Innovative</option>
                    <option value="Luxury">Luxury</option>
                    <option value="Minimalist">Minimalist</option>
                    <option value="Playful">Playful</option>
                    <option value="Professional">Professional</option>
                </select>

                <label>Number of Names:</label>
                <select value={numNames} onChange={(e) => setNumNames(e.target.value)}>
                    {[...Array(10).keys()].map((i) => (
                        <option key={i + 1} value={i + 1}>{i + 1}</option>
                    ))}
                </select>

                <button type="submit" disabled={loading}>
                    {loading ? "Generating..." : "Generate Names"}
                </button>
            </form>
        </div>
    );
};

export default InputForm;
