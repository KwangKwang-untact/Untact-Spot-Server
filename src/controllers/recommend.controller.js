const httpStatus = require('http-status');
const catchAsync = require('../utils/catchAsync');
const { recommendService } = require('../services');

const getRecommend = catchAsync(async (req, res) => {
  const result = await recommendService.getRecommend(req);
  res.status(httpStatus.OK).send(JSON.stringify(result));
});


module.exports = {
  getRecommend,
};
