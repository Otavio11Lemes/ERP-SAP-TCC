import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import FerramentasList from './components/FerramentasList';
import SuprimentosList from './components/SuprimentosList';
import Home from './components/Home'; // Opcional, pode ser a página inicial

function App() {
  return (
    <Router>
      <div className="App">
        <header>
          <h1>Gerenciamento de Ferramentas e Suprimentos</h1>
          {/* Adicione um menu de navegação se desejar */}
        </header>
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/ferramentas" element={<FerramentasList />} />
            <Route path="/suprimentos" element={<SuprimentosList />} />
            {/* Adicione outras rotas conforme necessário */}
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
