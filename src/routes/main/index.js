const express = require('express');
const recommendRoute = require('./recommend.route');

const router = express.Router();

router.use('/recommend', recommendRoute);
// router.use('/geometry', userRoute);
// router.use('/raw', docsRoute);

module.exports = router;
