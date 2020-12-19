const express = require('express');
const validate = require('../../middlewares/validate');
const recommendValidation = require('../../validations/recommend.validation');
const recommendController = require('../../controllers/recommend.controller');

const router = express.Router();

router
    .route('/')
    .get(validate(recommendValidation.getRecommend), recommendController.getRecommend);

module.exports = router;