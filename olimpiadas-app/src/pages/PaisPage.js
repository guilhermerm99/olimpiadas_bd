// src/pages/PaisesPage.js
import React, { useState } from 'react';
import {
  Typography, Container, Button, TextField, Stack, Card, CardContent, CircularProgress, Snackbar, Alert, IconButton
} from '@mui/material';
import axios from 'axios';
import { Delete as DeleteIcon, Edit as EditIcon } from '@mui/icons-material';

function PaisesPage() {
  const [action, setAction] = useState('');
  const [paises, setPaises] = useState([]);
  const [paisData, setPaisData] = useState({});
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [openSnackbar, setOpenSnackbar] = useState(false);

  const handleActionClick = (actionType) => {
    setAction(actionType);
    if (actionType === 'viewAll') {
      fetchPaises();
    }
  };

  const fetchPaises = async () => {
    setLoading(true);
    try {
      const response = await axios.get('/api/pais');
      setPaises(response.data);
    } catch (error) {
      setMessage('Erro ao buscar países.');
      setOpenSnackbar(true);
    }
    setLoading(false);
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setPaisData(prevData => ({ ...prevData, [name]: value }));
  };

  const handleFileChange = (event) => {
    setPaisData(prevData => ({ ...prevData, bandeira: event.target.files[0] }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    const formData = new FormData();
    formData.append('nome', paisData.nome || '');
    formData.append('sigla', paisData.sigla || '');
    if (paisData.bandeira) {
      formData.append('bandeira', paisData.bandeira);
    }
    try {
      if (action === 'add') {
        await axios.post('/api/pais', formData);
        setMessage('País adicionado com sucesso.');
      } else if (action === 'update') {
        await axios.put(`/api/pais/${paisData.id_pais}`, formData);
        setMessage('País atualizado com sucesso.');
      } else if (action === 'delete') {
        await axios.delete(`/api/pais/${paisData.id_pais}`);
        setMessage('País excluído com sucesso.');
      }
      setAction(''); // Reset action after success
      setPaisData({});
    } catch (error) {
      setMessage('Erro ao executar a ação.');
      setOpenSnackbar(true);
    }
    setLoading(false);
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Gerenciar Países
      </Typography>
      <Stack spacing={2}>
        <Button variant="contained" onClick={() => handleActionClick('viewAll')}>
          Visualizar Todos os Países
        </Button>
        <Button variant="contained" onClick={() => handleActionClick('add')}>
          Adicionar País
        </Button>
        <Button variant="contained" onClick={() => handleActionClick('update')}>
          Atualizar País
        </Button>
        <Button variant="contained" onClick={() => handleActionClick('delete')}>
          Excluir País
        </Button>
      </Stack>
      {loading && <CircularProgress />}
      {action === 'viewAll' && (
        <div>
          {paises.length > 0 ? (
            paises.map(pais => (
              <Card key={pais.id} sx={{ margin: 2 }}>
                <CardContent>
                  <Typography variant="h6">
                    Nome: {pais.nome}
                  </Typography>
                  <Typography color="textSecondary">
                    Sigla: {pais.sigla}
                  </Typography>
                  {pais.bandeira_url && (
                    <img src={pais.bandeira_url} alt={`Bandeira de ${pais.nome}`} height={100} />
                  )}
                  <Stack direction="row" spacing={1} sx={{ marginTop: 2 }}>
                    <IconButton onClick={() => {
                      setPaisData(pais);
                      setAction('update');
                    }}>
                      <EditIcon />
                    </IconButton>
                    <IconButton onClick={() => {
                      setPaisData(pais);
                      setAction('delete');
                    }}>
                      <DeleteIcon />
                    </IconButton>
                  </Stack>
                </CardContent>
              </Card>
            ))
          ) : (
            <Typography>Nenhum país encontrado.</Typography>
          )}
        </div>
      )}
      {(action === 'add' || action === 'update' || action === 'delete') && (
        <form onSubmit={handleSubmit}>
          {action !== 'delete' && (
            <>
              <TextField
                name="nome"
                label="Nome"
                value={paisData.nome || ''}
                onChange={handleInputChange}
                required
                fullWidth
              />
              <TextField
                name="sigla"
                label="Sigla"
                value={paisData.sigla || ''}
                onChange={handleInputChange}
                required
                fullWidth
              />
              <input
                type="file"
                name="bandeira"
                accept="image/*"
                onChange={handleFileChange}
              />
            </>
          )}
          {action === 'update' || action === 'delete' ? (
            <TextField
              name="id_pais"
              label="ID do País"
              value={paisData.id_pais || ''}
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

export default PaisesPage;
