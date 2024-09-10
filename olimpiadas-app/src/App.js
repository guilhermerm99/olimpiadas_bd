// src/App.js
import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import { Container, Button, Typography, Grid, Paper } from "@mui/material";
import AtletaPage from "./pages/AtletaPage";
import ConfederacaoPage from "./pages/ConfederacaoPage";
import PaisPage from "./pages/PaisPage";
import CorrelacionarPage from "./pages/CorrelacionarPage";
import ConsultaAtletaPage from "./pages/ConsultaAtletaPage";

function App() {
  return (
    <Router>
      <Container maxWidth="md">
        <Paper
          style={{ padding: "20px", marginTop: "20px", textAlign: "center" }}
        >
          <Typography variant="h2" gutterBottom>
            Olimpíadas
          </Typography>
          <Typography variant="h6" gutterBottom>
            Escolha uma opção para fazer requisições:
          </Typography>
          <Grid container spacing={2} justifyContent="center">
            <Grid item xs={12} sm={6} md={4}>
              <Link to="/atleta" style={{ textDecoration: "none" }}>
                <Button variant="contained" color="primary" fullWidth>
                  Atletas
                </Button>
              </Link>
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              <Link to="/confederacao" style={{ textDecoration: "none" }}>
                <Button variant="contained" color="secondary" fullWidth>
                  Confederações
                </Button>
              </Link>
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              <Link to="/pais" style={{ textDecoration: "none" }}>
                <Button variant="contained" color="success" fullWidth>
                  Países
                </Button>
              </Link>
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              <Link to="/consulta-atleta/1" style={{ textDecoration: "none" }}>
                <Button variant="contained" color="warning" fullWidth>
                  Consulta Atleta
                </Button>
              </Link>
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              <Link to="/correlacionar" style={{ textDecoration: "none" }}>
                <Button variant="contained" color="info" fullWidth>
                  Correlacionar
                </Button>
              </Link>
            </Grid>
          </Grid>
        </Paper>

        <Routes>
          <Route path="/atleta" element={<AtletaPage />} />
          <Route path="/confederacao" element={<ConfederacaoPage />} />
          <Route path="/pais" element={<PaisPage />} />
          <Route path="/correlacionar" element={<CorrelacionarPage />} />
          <Route path="/consulta-atleta/:id_atleta" element={<ConsultaAtletaPage />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;
