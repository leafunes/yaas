import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import Transactions from './Transactions';

const useStyles = makeStyles({
  root: {
    minWidth: 275,
    marginTop: '32px',
  },
  title: {
    marginBottom: '8px',
  },
});

const TransactionsCard = () => {
  const classes = useStyles();

  return (
    <Box className={classes.root}>
      <Typography className={classes.title} variant="h5" component="h5">
        Transactions
      </Typography>
      <Transactions />
    </Box>
  );
};

export default TransactionsCard;
