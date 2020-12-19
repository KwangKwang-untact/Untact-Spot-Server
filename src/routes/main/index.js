const express = require('express');
const recommendRoute = require('./recommend.route');
const geometryRoute = require('./geometry.route');

const router = express.Router();

router.use('/recommend', recommendRoute);
router.use('/geometry', geometryRoute);
// router.use('/raw', docsRoute);

module.exports = router;
