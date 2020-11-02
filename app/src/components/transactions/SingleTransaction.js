import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Accordion from '@material-ui/core/Accordion';
import AccordionDetails from '@material-ui/core/AccordionDetails';
import AccordionSummary from '@material-ui/core/AccordionSummary';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Overview from './Overview';
import Details from './Details';

const useStyles = makeStyles({
  accordion: ({ type }) => ({
    backgroundColor: type === 'credit' ? '#b2fab4' : '#ffa4a2',
  }),
});

const SingleTransaction = ({ transaction, expanded, handleChange }) => {
  const classes = useStyles(transaction);
  return (
    <Accordion
      className={classes.accordion}
      expanded={expanded === transaction.id}
      onChange={handleChange(transaction.id)}
    >
      <AccordionSummary
        expandIcon={<ExpandMoreIcon />}
        aria-controls="panel1bh-content"
        id="panel1bh-header"
      >
        <Overview transaction={transaction} />
      </AccordionSummary>
      <AccordionDetails>
        <Details transaction={transaction} />
      </AccordionDetails>
    </Accordion>
  );
};

export default SingleTransaction;
