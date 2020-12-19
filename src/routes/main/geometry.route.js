const express = require('express');
const validate = require('../../middlewares/validate');
const geometryValidation = require('../../validations/geometry.validation');
const geometryController = require('../../controllers/geometry.controller');

const router = express.Router();

router
    .route('/')
    .get(validate(geometryValidation.getAddress), geometryController.getAddress);

module.exports = router;