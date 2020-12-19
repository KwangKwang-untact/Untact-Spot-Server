const mongoose = require('mongoose');
const { toJSON, paginate } = require('./plugins');

const trafficSchema = mongoose.Schema(
    {
        name: {
            type: String,
            required: true,
        },
        code: {
            type: String,
            required: true,
        },
        location: {
            type: { type: String },
            coordinates: []
        },
        longitude: {
            type: Number,
            required: true,
        },
        latitude: {
            type: Number,
            required: true,
        },
    },
    {
        timestamps: true,
    }
);

trafficSchema.plugin(toJSON);
trafficSchema.plugin(paginate);
trafficSchema.index({ location: "2dsphere" });

trafficSchema.pre('save', async (next) => {
    next();
});

/**
 * @typedef Traffic
 */
const Traffic = mongoose.model('Traffic', trafficSchema);

module.exports = Traffic;
