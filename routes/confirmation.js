const express = require('express');
const { sendEmailsforOD } = require('../controllers/onDutyFunctions');

const router = express.Router();

router.get('/onduty-email', async (req, res) => {
  try {
    await sendEmailsforOD();
    res.status(200).send('Sent successfully');
  } catch (error) {
    res.status(500).send(`Error rejecting participant: ${error.message}`);
  }
});

module.exports = router;