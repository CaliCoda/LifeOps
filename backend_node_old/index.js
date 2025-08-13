/**
 * LifeOps backend entrypoint.
 */
const express = require('express');
const healthRouter = require('./app/routes/health');

const app = express();

app.use('/healthz', healthRouter);

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log(`LifeOps backend listening on port ${PORT}`);
});