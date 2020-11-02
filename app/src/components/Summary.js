import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
  root: {
    minWidth: 275,
    marginTop: '32px',
  },
  descr: {
    marginTop: '4px',
  },
});

const Summary = () => {
  const classes = useStyles();

  return (
    <Card className={classes.root}>
      <CardContent>
        <Typography variant="h3" component="h2">
          $452,78
        </Typography>
        <Typography className={classes.descr} variant="p" component="p">
          Available funds
        </Typography>
      </CardContent>
    </Card>
  );
};

export default Summary;
