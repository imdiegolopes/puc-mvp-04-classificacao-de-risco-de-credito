import { useState } from 'react';
import './App.css';

const formFieldData = [
  { label: 'Você é nosso cliente?', name: 'Attribute1', type: 'select', options: ["Não", "Sim"] },
  { label: 'Nome Completo', name: 'Attribute19', type: 'text' },
  { label: 'Quantos anos você tem?', name: 'Attribute13', type: 'number' },
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

      console.log(formData.Attribute1)
      formData.Attribute1 = formData?.Attribute1 == '' || formData?.Attribute1 == 'Não' ? 'A11' : 'A13' // Define o tipo de conta
      formData.Attribute8 = 3; // Define a taxa de 8% para todos os clientes
      formData.Attribute11 = 3;
      formData.Attribute16 = 0; // Define o numero de credito para 0
      formData.Attribute18 = 0; // Define o numero de pessoas obrigadas a fornecer sustento para 0
      formData.Attribute5 = formData?.Attribute5 == 0 ? 500 : formData?.Attribute5 // Define o valor do emprestimo

      const response = await fetch('http://localhost:5000/v1/analyze_credit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();
      alert('Resposta da Análise de Crédito: ' + (data.class == 'Bad' ? 'Reprovado!' : 'Aprovado!') + '!')
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
      <h3>Análise de crédito de forma rápida, simples e fácil.</h3>
      <p>Para ter a sua análise de crédito feita, basta preencher as suas informações abaixo com alguns dos seus dados que o processo é automático.</p>
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
        {response && (
          <p>Resposta da Análise de Crédito: {response == 'Bad' ? 'Negativa! Reprovado' : 'Aprovado!'}</p>

        )}
      </div>
    </>
  );
}

export default App;

