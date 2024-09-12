// src/pages/ConfederacoesPage.js
import React, { useState } from 'react';
import {
  Typography, Container, Button, TextField, Stack, Card, CardContent, CircularProgress, Snackbar, Alert
} from '@mui/material';
import axios from 'axios';

function ConfederacoesPage() {
  const [action, setAction] = useState('');
  const [confederacoes, setConfederacoes] = useState([]);
  const [confederacaoData, setConfederacaoData] = useState({});
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [openSnackbar, setOpenSnackbar] = useState(false);

  const handleActionClick = (actionType) => {
    setAction(actionType);
    if (actionType === 'viewAll') {
      fetchConfederacoes();
    }
  };

  const fetchConfederacoes = async () => {
    setLoading(true);
    try {
      const response = await axios.get('/api/confederacao');
      setConfederacoes(response.data);
    } catch (error) {
      setMessage('Erro ao buscar confederações.');
      setOpenSnackbar(true);
    }
    setLoading(false);
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setConfederacaoData(prevData => ({ ...prevData, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    try {
      if (action === 'add') {
        await axios.post('/api/confederacao', confederacaoData);
        setMessage('Confederação adicionada com sucesso.');
      } else if (action === 'update') {
        await axios.put(`/api/confederacao/${confederacaoData.id_confederacao}`, confederacaoData);
        setMessage('Confederação atualizada com sucesso.');
      } else if (action === 'delete') {
        await axios.delete(`/api/confederacao/${confederacaoData.id_confederacao}`);
        setMessage('Confederação excluída com sucesso.');
      }
      setAction(''); // Reseta a ação após o sucesso
      setConfederacaoData({});
    } catch (error) {
      setMessage('Erro ao executar a ação.');
      setOpenSnackbar(true);
    }
    setLoading(false);
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Gerenciar Confederações
      </Typography>
      <Stack spacing={2}>
        <Button variant="contained" onClick={() => handleActionClick('viewAll')}>
          Visualizar Todas as Confederações
        </Button>
        <Button variant="contained" onClick={() => handleActionClick('add')}>
          Adicionar Confederação
        </Button>
        <Button variant="contained" onClick={() => handleActionClick('update')}>
          Atualizar Confederação
        </Button>
        <Button variant="contained" onClick={() => handleActionClick('delete')}>
          Excluir Confederação
        </Button>
      </Stack>
      {loading && <CircularProgress />}
      {action === 'viewAll' && (
        <div>
          {confederacoes.length > 0 ? (
            confederacoes.map(conf => (
              <Card key={conf.id} sx={{ margin: 2 }}>
                <CardContent>
                  <Typography variant="h6">
                    Nome: {conf.nome}
                  </Typography>
                  <Typography color="textSecondary">
                    ID do País: {conf.id_pais}
                  </Typography>
                </CardContent>
              </Card>
            ))
          ) : (
            <Typography>Nenhuma confederação encontrada.</Typography>
          )}
        </div>
      )}
      {(action === 'add' || action === 'update' || action === 'delete') && (
        <form onSubmit={handleSubmit}>
          {action !== 'delete' && (
            <TextField
              name="nome"
              label="Nome"
              value={confederacaoData.nome || ''}
              onChange={handleInputChange}
              required
              fullWidth
            />
          )}
          {action !== 'delete' && (
            <TextField
              name="id_pais"
              label="ID do País"
              value={confederacaoData.id_pais || ''}
              onChange={handleInputChange}
              required
              fullWidth
            />
          )}
          {action === 'update' || action === 'delete' ? (
            <TextField
              name="id_confederacao"
              label="ID da Confederação"
              value={confederacaoData.id_confederacao || ''}
              onChange={handleInputChange}
              required
              fullWidth
            />
          ) : null}
          <Button type="submit" variant="contained" color="primary">
            {action === 'add' ? 'Adicionar' : action === 'update' ? 'Atualizar' : action === 'delete' ? 'Excluir' : 'Submeter'}
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

export default ConfederacoesPage;
