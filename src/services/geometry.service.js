const { default: Axios } = require('axios');

/**
 * get user point balance
 * @param {Object} user
 * @returns {Promise<Object>}
 */
const getAddress = async (req) => {

    const { latitude, longitude } = req.query;
    const response = await Axios.get('https://dapi.kakao.com/v2/local/geo/coord2address.json?x=' + longitude + '&y=' + latitude + '&input_coord=WGS84', {
        headers: {
            Authorization: 'KakaoAK 33b6248b144cca3b1c04efcfb742d497',
        },
    });
        
    return response.data.documents[0].address.address_name;
}

module.exports = {
    getAddress
};