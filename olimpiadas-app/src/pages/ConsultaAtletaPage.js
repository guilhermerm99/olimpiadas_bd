// src/pages/ConsultaAtletaPage.js
import React, { useState } from 'react';
import { Typography, Container, CircularProgress, Snackbar, Alert, TextField, Button, Card, CardContent, CardMedia, Grid } from '@mui/material';
import axios from 'axios';

const ConsultaAtletaPage = () => {
  const [idAtleta, setIdAtleta] = useState('');
  const [atleta, setAtleta] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    if (!idAtleta) return; // Não fazer a requisição se o ID estiver vazio

    setLoading(true);
    setAtleta(null);
    setError(null);

    try {
      const response = await axios.get(`/api/atleta/${idAtleta}`);
      setAtleta(response.data);
    } catch (err) {
      setError('Erro ao carregar os dados.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Detalhes do Atleta
      </Typography>

      <Grid container spacing={2} alignItems="center" style={{ marginBottom: '20px' }}>
        <Grid item xs={12} sm={8}>
          <TextField
            label="ID do Atleta"
            variant="outlined"
            fullWidth
            value={idAtleta}
            onChange={(e) => setIdAtleta(e.target.value)}
          />
        </Grid>
        <Grid item xs={12} sm={4}>
          <Button
            variant="contained"
            color="primary"
            fullWidth
            onClick={handleSearch}
          >
            Buscar
          </Button>
        </Grid>
      </Grid>

      {loading && <CircularProgress />}

      {error && (
        <Snackbar open={true} autoHideDuration={6000}>
          <Alert severity="error">{error}</Alert>
        </Snackbar>
      )}

      {atleta && (
        <Card style={{ marginTop: '20px' }}>
          {atleta.pais.bandeira ? (
            <CardMedia
              component="img"
              image={`data:image/png;base64,${atleta.pais.bandeira}`}
              alt="Bandeira"
              style={{ width: '100px', height: 'auto' }}
            />
          ) : (
            <Typography variant="body2" color="textSecondary">
              Bandeira não disponível
            </Typography>
          )}
          <CardContent>
            <Typography variant="h6">Atleta</Typography>
            <Typography variant="body1">Nome: {atleta.atleta.nome}</Typography>
            <Typography variant="body1">Gênero: {atleta.atleta.genero}</Typography>
            <Typography variant="body1">Data de Nascimento: {atleta.atleta.data_nasc}</Typography>

            <Typography variant="h6">Modalidade</Typography>
            <Typography variant="body1">Nome: {atleta.atleta.modalidade.nome}</Typography>

            <Typography variant="h6">Confederação</Typography>
            <Typography variant="body1">Nome: {atleta.confederacao.nome}</Typography>

            <Typography variant="h6">País</Typography>
            <Typography variant="body1">Nome: {atleta.pais.nome}</Typography>
            <Typography variant="body1">Sigla: {atleta.pais.sigla}</Typography>
          </CardContent>
        </Card>
      )}

      {!loading && !atleta && idAtleta && (
        <Typography variant="h6">Nenhum dado encontrado para o ID fornecido.</Typography>
      )}
    </Container>
  );
};

export default ConsultaAtletaPage;
