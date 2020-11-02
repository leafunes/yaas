import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import moment from 'moment';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexDirection: 'column',
  },
  date: {
    color: theme.palette.text.secondary,
    fontSize: 12,
  },
}));

const Details = ({ transaction }) => {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <Typography>{transaction.description}</Typography>
      <Typography className={classes.date}>
        {moment(new Date(transaction.date_created)).format('YYYY-MM-DD HH:mm')}
      </Typography>
    </div>
  );
};

export default Details;
