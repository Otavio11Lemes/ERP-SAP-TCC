import React, { useEffect, useState } from 'react';
import axios from 'axios';

const SuprimentosList = () => {
  const [suprimentos, setSuprimentos] = useState([]);

  useEffect(() => {
    axios.get('/api/suprimentos')
      .then(response => setSuprimentos(response.data))
      .catch(error => console.error('Erro ao buscar suprimentos:', error));
  }, []);

  return (
    <div>
      <h2>Lista de Suprimentos</h2>
      <ul>
        {suprimentos.map(suprimento => (
          <li key={suprimento.id}>{suprimento.nome} - {suprimento.tipo}</li>
        ))}
      </ul>
    </div>
  );
};

export default SuprimentosList;
