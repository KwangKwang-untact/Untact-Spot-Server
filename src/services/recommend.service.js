const { default: Axios } = require('axios');
const mongoose = require('mongoose');
const { Spot, Traffic } = require('../models');
const logger = require('../config/logger');
const { data } = require('../config/logger');

/**
 * get user point balance
 * @param {Object} user
 * @returns {Promise<Object>}
 */
const getRecommend = async (req) => {

    const { car, duration, theme, latitude, longitude } = req.query;
    let distance;
    
    if (car) {
        distance = 50000 * duration / 60
    } else {
        distance = 10000 * duration / 60
    }
    const dataTolgate = await Traffic.find({
        location : {
            $near : {
                $maxDistance : distance,
                $geometry : {
                    type: "Point",
                    coordinates: [longitude, latitude]
                }
            }
        }
    });
    logger.debug(dataTolgate);

    const dataSpot = await Spot.find({
        location: {
            $near: {
                $maxDistance: distance,
                $geometry: {
                    type: "Point",
                    coordinates: [longitude, latitude]
                }
            }
        }
    });

    for (let i = 0; i < dataTolgate.length; i++) {
        logger.debug(dataTolgate[i].code);
        const response = await Axios.get('http://data.ex.co.kr/openapi/trafficapi/trafficIc?key=4625471897&type=json&tmType=2&unitCode='+dataTolgate[i].code+'&numOfRows=99&pageNo=1')
        logger.info(response.data.count);

        for (let j = 0; j < dataSpot.length; j++) {
            
        }
    }
    
    
  return dataSpot;
};

const getDetail = async (req) => {

    const { id } = req.query;
    logger.debug(id);

    const dataSpot = await Spot.findOne({
        pk: id
    });

    return dataSpot;
};

const computeDistance = async (startCoords, destCoords) => {
    const startLatRads = degreesToRadians(startCoords.latitude);
    const startLongRads = degreesToRadians(startCoords.longitude);
    const destLatRads = degreesToRadians(destCoords.latitude);
    const destLongRads = degreesToRadians(destCoords.longitude);

    const Radius = 6371; //지구의 반경(km)
    const distance = Math.acos(Math.sin(startLatRads) * Math.sin(destLatRads) + 
                    Math.cos(startLatRads) * Math.cos(destLatRads) *
                    Math.cos(startLongRads - destLongRads)) * Radius;

    return distance;
}

// const datas = await Spot.find({});
//     logger.info(datas[0].id);
//     for (let i = 0; i < datas.length; i++) {
//         datas[i].location = {
//                 type: "Point",
//                 coordinates: [datas[i].latitude, datas[i].longitude]
//         }
//         logger.info(datas[i]);
//         await datas[i].save();
//     }

// /**
//  * get your point history
//  * @param {Object} user
//  * @param {Object} options - Query options
//  * @param {string} [options.sortBy] - Sort option in the format: sortField:(desc|asc)
//  * @param {number} [options.limit] - Maximum number of results per page (default = 10)
//  * @param {number} [options.page] - Current page (default = 1)
//  * @returns {Promise<Object>}
//  */
// const getHistory = async (user, options) => {
//   const { _id } = user;
//   const history = await Point.paginate({ user: _id }, options);

//   return history;
// };

// const swapPoint = async (user, amount) => {
//   if (user.balance < amount) {
//     return {
//       status: false,
//       msg: 'Not enough balance',
//     };
//   }
//   if (amount <= 0) {
//     return {
//       status: false,
//       msg: 'Invalid swap amount',
//     };
//   }

//   const response = await Axios.post('https://api2.foblgate.com/ticker/marketList');
//   const { nowPrice } = response.data.data['CTT/KRW'];

//   const amountData = new BigNumber(amount).dividedBy(new BigNumber(nowPrice).times(1.1)).toString().split('.');
//   const amountNumber = new BigNumber(`${amountData[0]}.${amountData[1].substring(0, 8)}`).toNumber();

//   const pointweet = await Axios.post(
//     'https://api.pointweet.castjam.io/pointweet/v1/users/sync',
//     {
//       phone: user.phone,
//       amount: amountNumber,
//     },
//     {
//       headers: {
//         apikey: '0744416c-2906-4936-aea1-9969afa9c0f6',
//       },
//     }
//   ).catch((error) => {
//     logger.error(error);
//     return {
//       status: false,
//       msg: '포인트윗(Pointweet)에 등록되지 않은 사용자입니다.',
//     };
//   });
//   logger.debug(pointweet);

//   await Point.create({
//     user: mongoose.Types.ObjectId(user._id),
//     type: 'spend',
//     title: 'CTT 교환',
//     value: amount,
//   });

//   return {
//     status: false,
//     msg: 'CTT 교환 완료',
//   };
// };

module.exports = {
    getRecommend,
    getDetail,
};
