/**
 * Created by yangbo on 2016-4-16.
 */
var mongoose = require("mongoose");
var Schema = mongoose.Schema;
var listSchema = new Schema({
    name: String
});
module.exports = mongoose.model('list', listSchema);