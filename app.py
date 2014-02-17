from time import time, sleep

from db_conf import db
from praw_conf import r

idset1 = set()

while True:
    commentlist = [c.json_dict for c in r.get_comments('all', limit=1000)]
    idset2 = set([c['name'] for c in commentlist])
    print "%s overlapped with previous" % str(len(idset1.intersection(idset2)))
    commentlist = filter(lambda c: c['name'] not in idset1, commentlist)
    print "comments to be inserted: %s" % str(len(commentlist))

    if len(commentlist) > 0:
        now = time()

        for c in  commentlist:
            c['last_seen'] = now

        db.comments.insert(commentlist)

    idset1 = idset1.union(idset2)
    print "unique ids: %s" % str(len(idset1))

    sleep(40)
