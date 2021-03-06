const mongoose = require('mongoose');
const { toJSON, paginate } = require('./plugins');

const spotSchema = mongoose.Schema(
    {
        title: {
            type: String,
            required: true,
        },
        detail: {
            type: String,
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
        price: {
            type: String,
            default: "무료",
        },
        address: {
            type: String,
            required: true,
        },
        time: {
            type: String,
            default: "정보 없음"
        },
        facilityRating: {
            type: Number,
            required: true
        },
        images: {
            type: Array,
        },
        dataTier: {
            type: Number,
            enum: [1, 2, 3],
        },
        tag: {
            type: Array, 
        },
    },
    {
        timestamps: true,
    }
);

spotSchema.plugin(toJSON);
spotSchema.plugin(paginate);
spotSchema.index({ location: "2dsphere" });

spotSchema.pre('save', async (next) => {
    this.updated = Date.now();
    next();
});

/**
 * @typedef Spot
 */
const Spot = mongoose.model('Spot', spotSchema);

module.exports = Spot;
