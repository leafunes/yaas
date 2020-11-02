import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import useAxios from 'axios-hooks';
import Skeleton from 'react-loading-skeleton';

const useStyles = makeStyles({
  root: {
    minWidth: 275,
    marginTop: '32px',
  },
  descr: {
    marginTop: '4px',
  },
});

const WithLoading = ({ text, loading }) => {
  if (loading) return <Skeleton />;
  return text();
};

const Summary = () => {
  const classes = useStyles();

  const [{ data, loading }] = useAxios('http://localhost:5000/account');

  return (
    <Card className={classes.root}>
      <CardContent>
        <Typography variant="h3" component="h2">
        <WithLoading loading={loading} text={() => `$${data.summary}`}/>
        </Typography>
        <Typography className={classes.descr} variant="p" component="p">
          Available funds
        </Typography>
      </CardContent>
    </Card>
  );
};

export default Summary;
