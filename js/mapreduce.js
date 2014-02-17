var mapFunction = function() {
    // remove some keys
    delete this['link_title']
    delete this['body_html']
    delete this['author_flair_text']
    delete this['author_flair_css_class']
    delete this['_id']
    delete this['created']
    delete this['saved']

    emit(this.name, this);
};

var reduceFunction = function(key, documents) {

    var maximum = function(values, key) {
        var max_res;

        for (var i = 0; i < values.length; i++) {
            var val = values[i];

            if (max_res == undefined || max_res == null || max_res[key] < val[key]) {
                max_res = val;
            }
        }

        return max_res;
    };

    return maximum(documents, 'last_seen');
};

db.comments.mapReduce(mapFunction, reduceFunction, {
    out: {'reduce': 'reduced_comments'}
});
