const httpStatus = require('http-status');
const catchAsync = require('../utils/catchAsync');
const { geometryService } = require('../services');

const getAddress = catchAsync(async (req, res) => {
  const result = await geometryService.getAddress(req);
  res.status(httpStatus.OK).send(result);
});


module.exports = {
  getAddress,
};
