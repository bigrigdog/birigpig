import React, { useState } from 'react';
import axios from 'axios';
import { Button, TextField } from '@material-ui/core';

function App() {
  const [input, setInput] = useState('');

  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://localhost:5000/generate', { data: input });
      console.log(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <TextField label="Enter Data" value={input} onChange={(e) => setInput(e.target.value)} />
      <Button onClick={handleSubmit} color="primary" variant="contained">Submit</Button>
    </div>
  );
}

export default App;