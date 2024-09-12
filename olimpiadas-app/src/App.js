// src/App.js
import React, { useState, useMemo } from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import {
  Container,
  Button,
  Typography,
  Grid,
  Paper,
  IconButton,
  CssBaseline,
} from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { Brightness4, Brightness7 } from "@mui/icons-material";
import AtletaPage from "./pages/AtletaPage";
import ConfederacaoPage from "./pages/ConfederacaoPage";
import PaisPage from "./pages/PaisPage";
import CorrelacionarPage from "./pages/CorrelacionarPage";
import ConsultaAtletaPage from "./pages/ConsultaAtletaPage";

function App() {
  const [darkMode, setDarkMode] = useState(false);

  // Criação do tema com base no modo escuro/claro
  const theme = useMemo(
    () =>
      createTheme({
        palette: {
          mode: darkMode ? "dark" : "light",
          background: {
            default: darkMode ? "#303030" : "#f5f5f5",
            paper: darkMode ? "#424242" : "#ffffff",
          },
        },
      }),
    [darkMode]
  );

  // Função para alternar entre o modo claro e escuro
  const toggleDarkMode = () => {
    setDarkMode((prevMode) => !prevMode);
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Container
          maxWidth="md"
          style={{
            minHeight: "100vh",
            backgroundColor: theme.palette.background.default,
            paddingTop: "20px",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          {/* Botões e título colados na parte superior */}
          <Paper
            style={{
              padding: "20px",
              position: "sticky", // Mantém o Paper fixo na parte superior
              top: 0, // Coloca o Paper no topo da tela
              zIndex: 1, // Mantém o Paper acima de outros elementos
              width: "100%", // Garante que o Paper ocupe toda a largura
              textAlign: "center",
              backgroundColor: theme.palette.background.paper,
              borderRadius: 0, // Remove as bordas arredondadas
            }}
          >
            {/* Botão de alternância de tema */}
            <IconButton
              onClick={toggleDarkMode}
              style={{ position: "absolute", top: 10, right: 10 }}
              color="inherit"
            >
              {darkMode ? <Brightness7 /> : <Brightness4 />}
            </IconButton>

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

          {/* Rotas da aplicação */}
          <Routes>
            <Route path="/atleta" element={<AtletaPage />} />
            <Route path="/confederacao" element={<ConfederacaoPage />} />
            <Route path="/pais" element={<PaisPage />} />
            <Route path="/correlacionar" element={<CorrelacionarPage />} />
            <Route
              path="/consulta-atleta/:id_atleta"
              element={<ConsultaAtletaPage />}
            />
          </Routes>
        </Container>
      </Router>
    </ThemeProvider>
  );
}

export default App;
