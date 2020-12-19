const Joi = require('@hapi/joi');

const getRecommend = {
  query: Joi.object().keys({ 
    car: Joi.boolean().default(true),
    duration: Joi.number().integer().required(),
    theme: Joi.array(),
    latitude: Joi.number().required(),
    longitude: Joi.number().required(),
  }),
};

const getDetail = {
  query: Joi.object().keys({ 
    id: Joi.string().required(),
  }),
};


module.exports = {
  getRecommend,
  getDetail,
};
