// src/pages/CorrelacionarPage.js
import React, { useState } from 'react';
import { Typography, Container, CircularProgress, Snackbar, Alert, Button, Card, CardContent, CardMedia} from '@mui/material';
import axios from 'axios';

const CorrelacionarPage = () => {
  const [correlacionados, setCorrelacionados] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleCorrelacionar = async () => {
    setLoading(true);
    setError(null);
    setCorrelacionados([]);

    try {
      const response = await axios.get('/api/correlacionar');
      setCorrelacionados(response.data);
    } catch (err) {
      setError('Erro ao buscar os dados correlacionados.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Correlacionar Atleta, Confederação, País e Modalidade
      </Typography>

      <Button
        variant="contained"
        color="primary"
        onClick={handleCorrelacionar}
        style={{ marginBottom: '20px' }}
      >
        Correlacionar
      </Button>

      {loading && <CircularProgress />}

      {error && (
        <Snackbar open={true} autoHideDuration={6000}>
          <Alert severity="error">{error}</Alert>
        </Snackbar>
      )}

      {correlacionados.length > 0 && correlacionados.map((item, index) => (
        <Card key={index} style={{ marginTop: '20px' }}>
          {item.pais.bandeira && (
            <CardMedia
              component="img"
              image={`data:image/png;base64,${item.pais.bandeira}`}
              alt="Bandeira"
              style={{ width: '100px', height: 'auto' }}
            />
          )}
          <CardContent>
            <Typography variant="h6">Atleta</Typography>
            <Typography variant="body1">Nome: {item.atleta.nome}</Typography>
            <Typography variant="body1">Gênero: {item.atleta.genero}</Typography>
            <Typography variant="body1">Data de Nascimento: {item.atleta.data_nasc}</Typography>

            <Typography variant="h6">Modalidade</Typography>
            <Typography variant="body1">Nome: {item.atleta.modalidade.nome}</Typography>

            <Typography variant="h6">Confederação</Typography>
            <Typography variant="body1">Nome: {item.confederacao.nome}</Typography>

            <Typography variant="h6">País</Typography>
            <Typography variant="body1">Nome: {item.pais.nome}</Typography>
            <Typography variant="body1">Sigla: {item.pais.sigla}</Typography>
          </CardContent>
        </Card>
      ))}

      {correlacionados.length === 0 && !loading && !error && (
        <Typography variant="h6">Nenhum dado encontrado.</Typography>
      )}
    </Container>
  );
};

export default CorrelacionarPage;
