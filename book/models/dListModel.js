/**
 * Created by yangbo on 2016-4-16.
 */
var mongoose = require("mongoose");
var Schema = mongoose.Schema;
var dListSchema = new Schema({
    title: String,
    star: String,
    key: String,
    desc: String
});
module.exports = mongoose.model('dlist', dListSchema);