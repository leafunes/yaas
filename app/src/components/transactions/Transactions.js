import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import useAxios from 'axios-hooks';
import Skeleton from 'react-loading-skeleton';
import SingleTransaction from './SingleTransaction';

const useStyles = makeStyles(() => ({
  root: {
    width: '100%',
  },
}));

const Transactions = () => {
  const classes = useStyles();
  const [expanded, setExpanded] = React.useState(false);
  const [{ data, loading }] = useAxios('http://localhost:5000/transactions');

  const handleChange = (panel) => (event, isExpanded) => {
    setExpanded(isExpanded ? panel : false);
  };

  if (loading) return <Skeleton count={6} />;

  return (
    <div className={classes.root}>
      {data.map((t) => (
        <SingleTransaction
          key={t.id}
          transaction={t}
          expanded={expanded}
          handleChange={handleChange}
        />
      ))}
    </div>
  );
};

export default Transactions;
