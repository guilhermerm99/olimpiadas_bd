// src/pages/AtletasPage.js
import React, { useState } from 'react';
import {
  Typography, Container, Button, TextField, Stack, Card, CardContent, CircularProgress, Snackbar, Alert
} from '@mui/material';
import api from '../services/api'; // Utilizando o Axios configurado para a baseURL

function AtletasPage() {
  const [action, setAction] = useState('');
  const [atletas, setAtletas] = useState([]);
  const [atletaData, setAtletaData] = useState({});
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [openSnackbar, setOpenSnackbar] = useState(false);

  const handleActionClick = (actionType) => {
    setAction(actionType);
    if (actionType === 'viewAll') {
      fetchAtletas();
    }
  };

  const fetchAtletas = async () => {
    setLoading(true);
    try {
      const response = await api.get('/api/atleta'); // Utilizando o Axios configurado
      setAtletas(response.data);
    } catch (error) {
      setMessage('Erro ao buscar atletas.');
      setOpenSnackbar(true);
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setAtletaData(prevData => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    try {
      if (action === 'add') {
        await api.post('/api/atleta', atletaData); // Utilizando a baseURL configurada no Axios
        setMessage('Atleta adicionado com sucesso.');
        fetchAtletas(); // Atualiza a lista após a adição
      } else if (action === 'update') {
        await api.put(`/api/atleta/${atletaData.id_atleta}`, atletaData);
        setMessage('Atleta atualizado com sucesso.');
        fetchAtletas(); // Atualiza a lista após a atualização
      } else if (action === 'delete') {
        await api.delete(`/api/atleta/${atletaData.id_atleta}`);
        setMessage('Atleta excluído com sucesso.');
        fetchAtletas(); // Atualiza a lista após a exclusão
      }
      setAction('');
      setAtletaData({});
    } catch (error) {
      setMessage('Erro ao executar a ação.');
      setOpenSnackbar(true);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Gerenciar Atletas
      </Typography>
      <Stack spacing={2}>
        <Button variant="contained" onClick={() => handleActionClick('viewAll')}>
          Visualizar Todos os Atletas
        </Button>
        <Button variant="contained" onClick={() => handleActionClick('add')}>
          Adicionar Atleta
        </Button>
        <Button variant="contained" onClick={() => handleActionClick('update')}>
          Atualizar Atleta
        </Button>
        <Button variant="contained" onClick={() => handleActionClick('delete')}>
          Excluir Atleta
        </Button>
      </Stack>
      {loading && <CircularProgress />}
      {action === 'viewAll' && (
        <div>
          {atletas.length > 0 ? (
            atletas.map(atleta => (
              <Card key={atleta.id} sx={{ margin: 2 }}>
                <CardContent>
                  <Typography variant="h6">
                    Nome: {atleta.nome}
                  </Typography>
                  <Typography color="textSecondary">
                    Gênero: {atleta.genero}
                  </Typography>
                  <Typography color="textSecondary">
                    Data de Nascimento: {new Date(atleta.data_nasc).toLocaleDateString()}
                  </Typography>
                </CardContent>
              </Card>
            ))
          ) : (
            <Typography>Nenhum atleta encontrado.</Typography>
          )}
        </div>
      )}
      {(action === 'add' || action === 'update' || action === 'delete') && (
        <form onSubmit={handleSubmit}>
          <TextField
            name="nome"
            label="Nome"
            value={atletaData.nome || ''}
            onChange={handleInputChange}
            required={action !== 'delete'}
            fullWidth
          />
          <TextField
            name="genero"
            label="Gênero"
            value={atletaData.genero || ''}
            onChange={handleInputChange}
            required={action !== 'delete'}
            fullWidth
          />
          <TextField
            name="data_nasc"
            label="Data de Nascimento"
            type="date"
            value={atletaData.data_nasc || ''}
            onChange={handleInputChange}
            required={action !== 'delete'}
            InputLabelProps={{ shrink: true }}
            fullWidth
          />
          {action !== 'delete' && (
            <TextField
              name="id_confederacao"
              label="ID da Confederação"
              value={atletaData.id_confederacao || ''}
              onChange={handleInputChange}
              required
              fullWidth
            />
          )}
          {action === 'update' && (
            <TextField
              name="id_atleta"
              label="ID do Atleta"
              value={atletaData.id_atleta || ''}
              onChange={handleInputChange}
              required
              fullWidth
            />
          )}
          <Button type="submit" variant="contained" color="primary">
            {action === 'add' ? 'Adicionar' : action === 'update' ? 'Atualizar' : 'Excluir'}
          </Button>
        </form>
      )}
      <Snackbar open={openSnackbar} autoHideDuration={6000} onClose={() => setOpenSnackbar(false)}>
        <Alert onClose={() => setOpenSnackbar(false)} severity={message.includes('Erro') ? 'error' : 'success'}>
          {message}
        </Alert>
      </Snackbar>
    </Container>
  );
}

export default AtletasPage;
