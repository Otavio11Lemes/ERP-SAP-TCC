import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FerramentasList = () => {
  const [ferramentas, setFerramentas] = useState([]);

  useEffect(() => {
    axios.get('/api/ferramentas')
      .then(response => setFerramentas(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h1>Ferramentas</h1>
      <ul>
        {ferramentas.map(ferramenta => (
          <li key={ferramenta.id}>{ferramenta.nome} - {ferramenta.tipo}</li>
        ))}
      </ul>
    </div>
  );
};

export default FerramentasList;
