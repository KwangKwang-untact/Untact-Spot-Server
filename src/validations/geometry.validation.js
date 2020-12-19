const Joi = require('@hapi/joi');

const getAddress = {
  query: Joi.object().keys({ 
    latitude: Joi.number().required(),
    longitude: Joi.number().required(),
  }),
};


module.exports = {
  getAddress,
};
