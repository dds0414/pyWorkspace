var express = require('express');
var router = express.Router();
var exec = require('child_process').exec;
var request = require('request');
var cheerio = require('cheerio');

var listModel = require('../models/listModel');
var DListModel = require('../models/dListModel');

/* GET users listing. */
router.get('/', function (req, res, next) {
    listModel.find(function(error,v){
        res.send(v);
    }).select("name");
});

router.get('/add/:key', function (req, res, next) {
    var data = {};
    data.name = req.params.key;
    listModel.create(data,function(err,v){
        if(err){
            res.send("mongod create list faile!");
        }

        exec("cd douban && scrapy crawl doubanspider  -a key=\""+encodeURI(req.params.key)+"|"+v._id+"\" --nolog", function(err,stdout,stderr){
            if(err) {
                listModel.remove({_id:v._id}, function(error){
                    if(error) {
                        console.log(error);
                    } else {
                        console.log('delete ok!');
                    }
                });
                console.log('get books api error:'+stderr);
                res.send("faile");
            } else {
                res.send("success");
            }
        });
    });
});



router.get('/getDList/:tag', function (req, res, next) {
    var map = {};
    map.key = req.params.tag;
    DListModel.find(map,function(err,v){
        if(err){
            res.send("mongod create list faile!");
        }
        res.send(v);
    }).sort({"star":-1}).limit(50).select("title star desc");
});


router.get('/down/:title/:anthor', function (req, res, next) {

    var data = [];
    request({
        method : "GET",
        url : "http://www.wangpansou.cn/s.php?wp=0&ty=gn&op=gn&q="+encodeURI(req.params.title)+"+pdf"
    },function(error, response, body){
        if(error){
            console.log(error)
        }
        var $ =  cheerio.load(body);
        $(".cse-search-result_content_item_top_a").each(function(i,e){
            var d = {};
            d.title = $(e).text().replace(/[\t\n]/g,"");
            d.href = $(e).attr("href");
            data.push(d);
        });
        res.json(data);
    });

});




module.exports = router;
