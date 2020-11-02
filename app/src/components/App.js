import React from 'react';
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import Header from './Header';
import Summary from './Summary';

export default function App() {
  return (
    <Container maxWidth="sm">
      <Box my={0}>
        <Header />
        <Summary />
      </Box>
    </Container>
  );
}
