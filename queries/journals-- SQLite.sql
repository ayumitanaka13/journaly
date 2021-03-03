-- SQLite

DELETE FROM journals;

INSERT INTO journals (id, from_user_id, start_date, end_date, country, city, title, comment, picture_path)
VALUES (1, 1, "2020-12-15 00:00:00.000000", "2020-12-18 00:00:00.000000", "Canada",	"Vancouver", "Bright days, Vancouver!",	
    "I went to the lighthouse park in Vancouver. Awesome park with great viewpoints on the different spots. If you love spending time out at the seashore and love hiking, watching the sun rises and sets. I swear this place is the best to visit for you. I had a great time out there enjoying the decent views and got a chance to see the beautiful sunset view there.",
    "image_journal/1_1614706085.jpg");

INSERT INTO journals (id, from_user_id, start_date, end_date, country, city, title, comment, picture_path)
VALUES (2, 2, "2018-05-10 00:00:00.000000",	"2018-05-12 00:00:00.000000", "Japan", "Kyoto", "Just love the serenity of Toji",
    "Yeah, I just love this place. It's away from the crowds, has a great garden and significant historical importance. Here are the tombs of all 15 Ashikaga Shoguns who ruled Japan in the fourteenth and early fifteenth centuries. The azaleas were a sight in late May and the view to the shrine across the pond is something to savor. I'll visit here again.",
    "image_journal/2_1614726398.jpg");

INSERT INTO journals (id, from_user_id, start_date, end_date, country, city, title, comment, picture_path)
VALUES (3, 3, "2010-08-08 00:00:00.000000",	"2010-08-10 00:00:00.000000", "Singapore", "Singapore", "A place that you should visit",
    "Gardens by the Bay, such a fantastic place to visit if you like gardening, flowers, and scenery, this is the most relaxing garden I have ever visited. Everywhere you looked was pristine with healthy tropical plants. When you enter you are faced with a huge waterfall, so powerful. We all loved it and my daughter was able to take lots of photos for IG.",
    "image_journal/3_1614798467.jpg");

INSERT INTO journals (id, from_user_id, start_date, end_date, country, city, title, comment, picture_path)
VALUES (4, 1, "2016-03-03 00:00:00.000000",	"2016-03-9 00:00:00.000000", "Spain", "Barcelona", "Oh my, Can’t describe...",
    "An amazing once-in-a-lifetime experience. You can look at photographs all the time but being there in person is a total experience. The energy of being inside this majestic beautiful basilica is euphoric. We walked by it by night as well. I think it’s looked even more astonishing! We also went to the nearby rooftop and were mesmerized like we were in there.",
    "image_journal/1_1614799387.jpg");
