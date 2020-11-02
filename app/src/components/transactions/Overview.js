import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles((theme) => ({
  transactionType: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '33.33%',
    flexShrink: 0,
  },
  transactionAmount: {
    fontSize: theme.typography.pxToRem(15),
  },
}));

const TrType = ({ transaction }) => (transaction.type === 'credit' ? 'Credit' : 'Debit');
const TrAmount = ({ transaction }) => `$${transaction.type === 'credit' ? ' ' : ' -'}${transaction.amount}`;

const Overview = ({ transaction }) => {
  const classes = useStyles();

  return (
    <>
      <Typography className={classes.transactionType}>
        <TrType transaction={transaction} />
      </Typography>
      <Typography className={classes.transactionAmount}>
        <TrAmount transaction={transaction} />
      </Typography>
    </>
  );
};

export default Overview;
