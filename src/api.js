import axios from "axios";

const API_BASE_URL = "https://abhigyankulavi-product-name-generator.hf.space";  

export const generateNames = async (productDescription, brandTone, numNames) => {
    try {
        const response = await axios.post(
            `${API_BASE_URL}/api/predict`, 
            {
                description: productDescription,
                tone: brandTone,
                num_names: numNames
            }, 
            { headers: { "Content-Type": "application/json" } }
        );

        console.log("API Response:", response.data);
        return response.data.names || [];  
    } catch (error) {
        console.error("Error generating product names:", error);
        return [];
    }
};
