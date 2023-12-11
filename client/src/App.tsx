import { useState } from 'react';
import './App.css';

const formFieldData = [
  { label: 'Nome Completo', name: 'Attribute19', type: 'text' },
  { label: 'Duração em meses', name: 'Attribute2', type: 'number' },
  { label: 'Propósito', name: 'Attribute4', type: 'text' },
  { label: 'Quanto você quer pegar emprestado?', name: 'Attribute5', type: 'select', options: [500, 1000, 5000, 10000] },
];

function App() {
  const [formData, setFormData] = useState(
    formFieldData.reduce((acc, field) => ({ ...acc, [field.name]: field.type === 'number' ? 1 : '' }), {})
  );

  const [response, setResponse] = useState('');

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    try {
      const response = await fetch('http://localhost:5000/v1/analyze_credit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      setResponse(data.class);
    } catch (error) {
      console.error('Error:', error);
      setResponse('Error occurred');
    }
  };

  return (
    <>
      <div>
        <a href="#" target="_blank">
          <img src="https://img.freepik.com/vetores-premium/logotipo-de-financiamento-de-credito-de-emprestimo-em-dinheiro-icone-ilustracao-identidade-da-marca_7109-752.jpg?w=1380" className="logo" alt="Vite logo" />
        </a>
      </div>
      <h1>Credifácil</h1>
      <div className="card">
        <form onSubmit={handleSubmit}>
          {/* Render form fields based on formFieldData */}
          {formFieldData.map((field) => (
            <div key={field.name}>
              <label>{field.label}:</label><br/>
              {field.type === 'select' ? (
                <select
                  value={formData[field.name]}
                  onChange={(e) => setFormData({ ...formData, [field.name]: e.target.value })}
                >
                  {field.options.map((option) => (
                    <option key={option} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              ) : (
                <input
                  type={field.type}
                  value={formData[field.name]}
                  onChange={(e) => setFormData({ ...formData, [field.name]: e.target.value })}
                />
              )}
            </div>
          ))}
          <button type="submit">Analisar</button>
        </form>
        <p>Response: {response}</p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;

